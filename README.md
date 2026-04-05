# BMad Plugins Marketplace

The official registry of BMad modules. This repository is the single source of truth for what modules are available, their versions, and their trust status.

## Submit Your Module

Built a BMad module and want to share it? Here's the short version:

1. Build and validate your module with [BMad Builder](https://bmad-builder-docs.bmad-method.org/)
2. Push to GitHub with a `.claude-plugin/marketplace.json` manifest and a tagged release
3. Open a PR to this repo adding a YAML entry to `registry/community/your-module.yaml`
4. Your module goes through automated validation and manual review

Full details in [CONTRIBUTING.md](CONTRIBUTING.md). Before submitting, review the [GOVERNANCE.md](GOVERNANCE.md) to understand what we accept, and choose a category from [categories.yaml](categories.yaml).

## How It Works

The registry contains a YAML entry for each module, organized into three directories:

| Category | Directory | Description |
| -------- | --------- | ----------- |
| **Official** | `registry/official/` | Core BMad modules maintained by the BMad team — always tracks main |
| **Utility** | `registry/utility/` | BMad ecosystem tools and utilities — always tracks main |
| **Community** | `registry/community/` | Modules built by community members — pinned to approved version tag + commit SHA |

Each module also declares a `category` and `subcategory` from [categories.yaml](categories.yaml) for discoverability.

Browse all available modules in the **[Module Index](INDEX.md)** (auto-generated).

The BMad installer resolves module versions from this registry.

## Trust Tiers

| Tier | Meaning |
| ---- | ------- |
| **Unverified** | Automated checks passed |
| **Community Reviewed** | A trusted community reviewer approved |
| **BMad Certified** | BMad team reviewed and endorses |

Every community submission and update goes through automated validation (Validate Module, manifest verification, security scanning) and manual review (prompt content audit, script behavior check).

## Install a Module

All registered modules can be installed through the BMad installer:

```bash
npx bmad-method install
```

### Claude Code Plugin Integration

```json
{
  "extraKnownMarketplaces": {
    "bmad-plugins": {
      "source": {
        "source": "github",
        "repo": "bmad-code-org/bmad-plugins-marketplace"
      }
    }
  }
}
```

## Related

- [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD) — Core framework
- [BMad Builder](https://github.com/bmad-code-org/bmad-builder) — Build custom modules
- [Distribute Your Module](https://bmad-builder-docs.bmad-method.org/how-to/distribute-your-module) — Repo setup guide

## Community

- [Discord](https://discord.gg/gk8jAdXWmj) — Get help, share ideas, collaborate
- [YouTube](https://youtube.com/@BMadCode) — Tutorials, master class, and more
- [X / Twitter](https://x.com/BMadCode)
- [Website](https://bmadcode.com)

## Support BMad

BMad is free for everyone and always will be. Star this repo, [buy me a coffee](https://buymeacoffee.com/bmad), or email contact@bmadcode.com for corporate sponsorship.

## License

MIT
