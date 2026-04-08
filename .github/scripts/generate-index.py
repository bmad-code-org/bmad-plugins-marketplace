#!/usr/bin/env python3
"""Generate INDEX.md and community-index.yaml from registry YAML files."""

import yaml
from datetime import datetime, timezone
from pathlib import Path

REGISTRY_DIR = Path("registry")
CATEGORIES_FILE = Path("categories.yaml")
OUTPUT_FILE = Path("INDEX.md")
COMMUNITY_INDEX_FILE = REGISTRY_DIR / "community-index.yaml"


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def load_categories():
    data = load_yaml(CATEGORIES_FILE)
    return data.get("categories", {})


def load_modules():
    modules = []
    for directory in ["official", "utility", "community"]:
        dir_path = REGISTRY_DIR / directory
        if not dir_path.exists():
            continue
        for yaml_file in sorted(dir_path.glob("*.yaml")):
            if yaml_file.name == "registry-schema.yaml":
                continue
            module = load_yaml(yaml_file)
            module["_directory"] = directory
            modules.append(module)
    return modules


def tier_badge(tier):
    badges = {
        "bmad-certified": "BMad Certified",
        "community-reviewed": "Community Reviewed",
        "unverified": "Unverified",
    }
    return badges.get(tier, tier)


def generate_community_index(modules):
    """Generate community-index.yaml from community modules."""
    community = [m for m in modules if m.get("_directory") == "community"]

    # Strip internal _directory key before writing
    clean_modules = []
    for mod in community:
        clean = {k: v for k, v in mod.items() if k != "_directory"}
        clean_modules.append(clean)

    index_data = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "modules": clean_modules,
    }

    content = "# Auto-generated from registry/community/*.yaml - do not edit manually\n"
    content += yaml.dump(index_data, default_flow_style=False, sort_keys=False, allow_unicode=True)
    COMMUNITY_INDEX_FILE.write_text(content)
    print(f"Generated {COMMUNITY_INDEX_FILE} with {len(clean_modules)} community modules")


def main():
    categories = load_categories()
    modules = load_modules()

    # Generate community-index.yaml
    generate_community_index(modules)

    # Group modules by category
    by_category = {}
    for mod in modules:
        cat = mod.get("category", "uncategorized")
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(mod)

    lines = [
        "# BMad Marketplace Module Index",
        "",
        f"*Auto-generated from registry entries. {len(modules)} modules registered.*",
        "",
    ]

    # Summary by directory
    official = [m for m in modules if m["_directory"] == "official"]
    utility = [m for m in modules if m["_directory"] == "utility"]
    community = [m for m in modules if m["_directory"] == "community"]

    lines.append(f"**Official:** {len(official)} | **Utility:** {len(utility)} | **Community:** {len(community)}")
    lines.append("")

    # Alphabetical categories
    for cat_slug in sorted(by_category.keys()):
        cat_info = categories.get(cat_slug, {})
        cat_name = cat_info.get("name", cat_slug)
        cat_modules = by_category[cat_slug]

        lines.append(f"## {cat_name}")
        lines.append("")
        lines.append("| Module | Type | Subcategory | Trust | Description |")
        lines.append("| ------ | ---- | ----------- | ----- | ----------- |")

        subcategories = cat_info.get("subcategories", {})

        for mod in sorted(cat_modules, key=lambda m: m.get("name", "")):
            name = mod.get("name", "unknown")
            repo = mod.get("repository", "")
            directory = mod["_directory"]
            subcat_slug = mod.get("subcategory", "")
            subcat_name = subcategories.get(subcat_slug, {}).get("name", subcat_slug)
            trust = tier_badge(mod.get("trust_tier", ""))
            desc = mod.get("description", "")

            link = f"[{name}]({repo})" if repo else name
            lines.append(f"| {link} | {directory} | {subcat_name} | {trust} | {desc} |")

        lines.append("")

    OUTPUT_FILE.write_text("\n".join(lines))
    print(f"Generated {OUTPUT_FILE} with {len(modules)} modules")


if __name__ == "__main__":
    main()
