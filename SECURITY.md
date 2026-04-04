# Security Policy

## Reporting a Vulnerability in a Marketplace Module

If you discover a security issue in a module listed in the BMad Marketplace, **do not open a public issue.** Instead:

1. **Open a GitHub Security Advisory** on this repository using the "Report a vulnerability" button under the Security tab
2. Include the module name, a description of the vulnerability, and steps to reproduce
3. If the issue is in the module's source repo (not the registry itself), also report it directly to the module author

The BMad team will:

- Acknowledge the report within **5 business days**
- Coordinate with the module author if applicable
- Remove or flag the module if the author does not respond within a reasonable timeframe
- Notify the reporter of the resolution

## Reporting a Vulnerability in the Marketplace Itself

For security issues in the registry infrastructure, CI workflows, or governance processes, follow the same process above.

## Responsible Disclosure

We ask that you:

- Give us reasonable time to address the issue before public disclosure
- Do not exploit the vulnerability beyond what is necessary to demonstrate it
- Do not access or modify other users' data

## Supported Versions

The marketplace registry on the `main` branch is the only supported version. Historical tags are not maintained.
