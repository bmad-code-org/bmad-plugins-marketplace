# Contributing a Module to the BMad Marketplace

## Registry Structure

| Category | Directory | Description | SHA Required | Updates |
| -------- | --------- | ----------- | ------------ | ------- |
| **Official** | `registry/official/` | Core BMad modules maintained by the BMad team | No — always tracks main | Managed internally |
| **Utility** | `registry/utility/` | BMad ecosystem tools and utilities | No — always tracks main | Managed internally |
| **Community** | `registry/community/` | Modules built and maintained by community members | Yes — pinned to tag + SHA | Author submits update PRs |

## Before You Submit

1. **Build your module** using [BMad Builder](https://bmad-builder-docs.bmad-method.org/)
2. **Validate it** — run Validate Module (VM) and fix all critical findings
3. **Publish to GitHub** — your repo must contain a valid `.claude-plugin/marketplace.json` manifest
4. **Tag a release** — use semantic versioning (e.g., `v1.0.0`)

See the [BMad Builder docs: Distribute Your Module](https://bmad-builder-docs.bmad-method.org/how-to/distribute-your-module/) for full guidance on repo structure and the marketplace.json format.

## Submission Process

### New Community Module

1. Fork this repository
2. Add a YAML entry for your module in `registry/community/your-module-name.yaml`:

   ```yaml
   name: your-module-name
   description: What your module does in one sentence
   repository: https://github.com/your-org/your-module
   author: your-name-or-org
   license: MIT
   default_selected: false
   type: community
   category: <category slug from categories.yaml>
   subcategory: <subcategory slug from categories.yaml>
   keywords:
     - bmad
     - your-domain

   version: "1.0.0"
   approved_tag: v1.0.0
   approved_sha: <full commit SHA of the tag>
   trust_tier: unverified
   approved_date: "<today's date>"
   reviewer: pending
   ```

   Choose your `category` and `subcategory` slugs from [categories.yaml](categories.yaml). If none fit, open a GitHub issue to propose a new one.

3. Open a PR using the **New Module** template
4. A reviewer validates your module and audits the content
5. Once approved, your module appears in the marketplace

### Version Update (Community Modules)

1. Tag the new version in your repo
2. Update your registry YAML with the new version, tag, SHA, and date
3. Open a PR using the **Version Update** template
4. A reviewer validates the new version and audits what changed
5. Once merged, the update is live

## Trust Tiers

| Tier | Meaning | How to Achieve |
| ---- | ------- | -------------- |
| **Unverified** | Automated checks passed | Submit to registry, pass CI |
| **Community Reviewed** | A trusted reviewer approved | Reviewer signs off on PR |
| **BMad Certified** | BMad team reviewed and endorses | BMad team review + ongoing update re-vetting |

New community submissions start at **Unverified**. Trust tier upgrades happen through consistent quality and community engagement.

## What Gets Reviewed

- **Prompt content** — what the skills instruct the AI to do (this matters most)
- **Script behavior** — file access patterns, network calls, external commands
- **Manifest accuracy** — skill paths resolve, descriptions match actual behavior
- **Security** — no prompt injection patterns, no data exfiltration, no obfuscated code

## Policies

- **Removal:** Modules may be removed for security issues, author request, or prolonged abandonment
- **Disputes:** Open an issue to discuss — the BMad team makes final decisions
- **Updates:** Authors are responsible for submitting version update PRs. Outdated modules are not automatically removed but may be flagged
