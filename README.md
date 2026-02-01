# BMad Plugins Marketplace

Official plugin marketplace for [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD) - an AI-driven agile development framework.

## Installation

Add this marketplace to any BMad project:

```bash
claude plugin marketplace add github:bmad-code-org/bmad-plugins-marketplace
```

## Available Plugins

| Plugin | Description | Install |
|--------|-------------|---------|
| **bmad-utility-skills** | Issue triage, changelog drafting, and release automation | `claude plugin install bmad-utility-skills@bmad-plugins` |

### bmad-utility-skills

Utility skills for BMad Method contributors.

**Skills included:**
- `gh-triage` - AI-powered GitHub issue triage with deep analysis
- `draft-changelog` - Generate changelog drafts for BMad projects
- `release-bmad-module` - Automate BMad module releases

**Install:**
```bash
claude plugin install bmad-utility-skills@bmad-plugins
```

**Usage:**
```bash
bmad-utility-skills:gh-triage
bmad-utility-skills:draft-changelog bmad-builder
bmad-utility-skills:release-bmad-module cis
```

## For Plugin Developers

To add a new plugin to this marketplace:

1. Create your plugin in a separate GitHub repo with the standard structure:
   ```
   your-plugin/
   ├── .claude-plugin/
   │   └── plugin.json
   └── skills/ (or agents/, commands/, etc.)
   ```

2. Add an entry to `.claude-plugin/marketplace.json`:
   ```json
   {
     "name": "your-plugin",
     "source": {
       "source": "github",
       "repo": "bmad-code-org/your-plugin"
     },
     "description": "Your plugin description",
     "version": "1.0.0"
   }
   ```

3. Update this README to include your plugin in the table

4. Submit a PR

## License

MIT

## Author

bmad-code-org
