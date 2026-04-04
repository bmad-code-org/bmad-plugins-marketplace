# Marketplace Governance

This document defines what the BMad Marketplace will and will not accept, how modules are evaluated, and how decisions are made.

## What We Accept

- Modules built with [BMad Builder](https://bmad-builder-docs.bmad-method.org/) that follow the BMad skill structure
- Modules that provide genuine value to BMad Method platform users
- Modules that pass Validate Module (VM) with no critical findings
- Modules with a clear `.claude-plugin/marketplace.json` manifest and tagged release
- Modules hosted on GitHub in a public repository
- Modules that declare a valid category and subcategory from [categories.yaml](categories.yaml)

## What We Will Not Accept

- Modules that contain malicious behavior — prompt injection, data exfiltration, unauthorized network calls, obfuscated code
- Modules that attempt to override, disable, or circumvent BMad core behavior
- Modules that duplicate functionality already provided by an official module without meaningful differentiation
- Modules that exist primarily to advertise or promote unrelated products or services
- Modules with deceptive descriptions — the description must accurately reflect what the module does
- Modules that require excessive permissions or file system access beyond what their purpose justifies
- Modules without a license (for example as MIT)

## Evaluation Criteria

When reviewing a submission, reviewers assess:

| Criteria | What We Look For |
| -------- | ---------------- |
| **Purpose** | Does the module solve a real problem or fill a genuine gap? |
| **Quality** | Does it follow BMad best practices? Are prompts well-crafted and scripts robust? |
| **Security** | Are file access patterns appropriate? Are there suspicious network calls or obfuscated logic? |
| **Prompt Safety** | Do the prompts instruct the AI to behave as described? No hidden instructions or deceptive patterns? |
| **Accuracy** | Do the help entries, descriptions, and marketplace.json match actual behavior? |
| **Completeness** | Does the module pass VM validation? Are all required files present? |

## Decision Authority

- **Community submissions:** Reviewed by BMad team members or designated trusted reviewers. At least one approval required to merge.
- **Trust tier upgrades:** Decided by the BMad team based on module quality, track record, and community feedback.
- **Removals:** The BMad team may remove a module at any time for security issues, policy violations, or author request. The author will be notified via GitHub issue when possible.
- **Disputes:** Open a GitHub issue. The BMad team makes final decisions.

## Update Policy

- **Official and Utility modules** are maintained by the BMad team and always track main. No external review required.
- **Community modules** are pinned to a specific version tag and commit SHA. Authors submit update PRs which go through the same review process as new submissions. Reviewers focus on the diff between the previously approved version and the new one.
- **Stale modules** that have not been updated in over 12 months may be flagged with a notice. They are not automatically removed.

## Revocation

A module may be revoked (removed from the registry) if:

- A security vulnerability is discovered and the author does not respond within a reasonable timeframe
- The module is found to violate policies that were not caught during initial review
- The author requests removal
- The source repository is deleted or made inaccessible

Revoked modules are removed from the registry. Users who have already installed the module are not affected, but will no longer receive updates.

## Review Timeline

We aim to provide initial feedback on submissions within **14 business days**. Complex modules may take longer. If you have not received any response after 30 days, comment on your PR to bump it.

## Author Identity

Authors are identified by their GitHub account. The PR submission itself serves as proof of identity. We may reach out via GitHub for security-related communications.

In the future, we plan to offer Discord-linked verification for enhanced trust and faster communication.

## Changes to This Policy

This governance document may be updated as the marketplace evolves. Significant changes will be communicated through the repository's release notes.
