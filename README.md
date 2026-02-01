# BMad Plugins Marketplace

Official plugin marketplace for [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD) - an AI-driven agile development framework.

## Quick Start

```bash
# From any BMad project directory
claude plugin marketplace add bmad-code-org/bmad-plugins-marketplace
claude plugin install --scope project <plugin-name>@bmad-plugins
```

## Understanding Installation Scope

When installing plugins, you can choose between **project scope** or **user scope**:

### Project Scope (Recommended for Teams)

```bash
claude plugin install --scope project <plugin-name>@bmad-plugins
```

- Configuration saved to `.claude/settings.json` (in your project)
- Can be committed to git
- Available to all contributors who clone the repo
- **Use this for BMad modules you work on with a team**

### User Scope (Default)

```bash
claude plugin install <plugin-name>@bmad-plugins
```

- Configuration saved to `~/.claude/settings.json` (your home directory)
- Available across all your personal projects
- **Use this for personal projects**

## Available Plugins

| Plugin | Description | Install Command |
|--------|-------------|-----------------|
| **bmad-utility-skills** | Issue triage, changelog drafting, and release automation | `claude plugin install --scope project bmad-utility-skills@bmad-plugins` |

---

### bmad-utility-skills

Utility skills for BMad Method contributors.

**Skills included:**
- `gh-triage` - AI-powered GitHub issue triage with deep analysis
- `draft-changelog` - Generate changelog drafts for BMad projects
- `release-bmad-module` - Automate BMad module releases

**Install:**
```bash
claude plugin install --scope project bmad-utility-skills@bmad-plugins
```

**Usage (after restarting Claude Code):**
```bash
bmad-utility-skills:gh-triage
bmad-utility-skills:draft-changelog bmad-builder
bmad-utility-skills:release-bmad-module cis
```

---

## Auto-Enable Plugins for Your Team

To automatically prompt contributors to install plugins when they clone your BMad module, add to your project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "bmad-plugins": {
      "source": {
        "source": "github",
        "repo": "bmad-code-org/bmad-plugins-marketplace"
      }
    }
  },
  "enabledPlugins": {
    "bmad-utility-skills@bmad-plugins": true
  }
}
```

Then commit to your repository:
```bash
git add .claude/settings.json
git commit -m "Configure bmad-plugins marketplace"
git push
```

## Commands Reference

```bash
# Add the marketplace
claude plugin marketplace add bmad-code-org/bmad-plugins-marketplace

# List available plugins from the marketplace
claude plugin marketplace list

# Install a plugin (project scope)
claude plugin install --scope project <plugin-name>@bmad-plugins

# List installed plugins
claude plugin list

# Uninstall a plugin
claude plugin uninstall <plugin-name>@bmad-plugins

# Update the marketplace
claude plugin marketplace update bmad-plugins
```

## For Plugin Developers

To add a new plugin to this marketplace:

1. **Create your plugin** in a separate GitHub repo:
   ```
   your-plugin/
   ├── .claude-plugin/
   │   └── plugin.json          # Plugin manifest
   ├── skills/                  # Agent Skills (optional)
   │   └── your-skill/
   │       └── SKILL.md
   ├── agents/                  # Custom agents (optional)
   └── commands/                # Commands (optional)
   ```

2. **Add to marketplace.json** in this repo:
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

3. **Update this README** to include your plugin in the Available Plugins table

4. **Submit a PR** to this marketplace

## License

MIT

## Author

bmad-code-org

## Related Links

- [BMad Method Framework](https://github.com/bmad-code-org/BMAD-METHOD)
- [BMad Builder](https://github.com/bmad-code-org/bmad-builder)
- [BMad Creative Intelligence Suite](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite)
- [BMad Game Dev Studio](https://github.com/bmad-code-org/bmad-module-game-dev-studio)
