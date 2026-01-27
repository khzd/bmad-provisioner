# BMAD Provisioner

**Infrastructure as Code for BMAD Custom Skills**

Manage custom BMAD leaders across multiple projects with declarative configuration.
Survives BMAD version updates by re-provisioning from manifest.

## Features

- ✅ **Declarative Configuration**: Define skills in `skills-manifest.yaml`
- ✅ **Gap Analysis**: Compare desired vs actual state
- ✅ **Multi-Project**: Manage multiple BMAD projects
- ✅ **Version-Safe**: Survive BMAD updates
- ✅ **Smart CSV Merge**: Preserve custom data
- ✅ **Dry Run**: Preview changes before applying

## Quick Start

### 1. Create skills-manifest.yaml

```yaml
project:
  name: HealthAI-Platform
  bmad_version: v6.x
  root: ~/projects/HealthAI-Platform

  leaders:
    - name: dev-leader
      domain: generic
      specialists:
        - id: frontend
          name: Frontend Developer
          domain: React, Vue
          skills: [UI, styling]
```

### 2. Analyze Current State

```bash
python bmad_provisioner.py \
  --config skills-manifest.yaml \
  --mode analyze
```

Output:
```
📊 Gap Analysis Report
==================================================

BMAD Version: v6.2.1

❌ dev-leader: Not installed
✅ qa-leader: Up to date
⚠️  cis-leader: Needs update
   ⚠️  data/creative-methods.csv: 2 rows missing

💡 Recommendations:
   - Install 1 missing leaders: dev-leader
   - Update 1 outdated leaders: cis-leader
```

### 3. Preview Changes

```bash
python bmad_provisioner.py \
  --config skills-manifest.yaml \
  --mode diff
```

### 4. Provision Skills

```bash
# Dry run first
python bmad_provisioner.py \
  --config skills-manifest.yaml \
  --mode provision \
  --dry-run

# Apply for real
python bmad_provisioner.py \
  --config skills-manifest.yaml \
  --mode provision
```

## Usage

### Modes

**analyze** - Gap analysis (default)
```bash
bmad_provisioner.py --config manifest.yaml --mode analyze
```

**diff** - Show what would change
```bash
bmad_provisioner.py --config manifest.yaml --mode diff
```

**provision** - Deploy skills
```bash
bmad_provisioner.py --config manifest.yaml --mode provision
```

**validate** - Validate manifest only
```bash
bmad_provisioner.py --config manifest.yaml --mode validate
```

### Options

**--project-root** - Override project root from manifest
```bash
bmad_provisioner.py --config manifest.yaml \
  --project-root ~/projects/HealthAI-Platform
```

**--dry-run** - Preview without changes
```bash
bmad_provisioner.py --mode provision --dry-run
```

**--verbose** - Detailed output
```bash
bmad_provisioner.py --mode analyze --verbose
```

## Workflow: BMAD Update Scenario

```bash
# 1. Before BMAD update - analyze current state
python bmad_provisioner.py --config manifest.yaml --mode analyze
# Output: All skills up to date ✅

# 2. Update BMAD (may overwrite configs)
cd ~/projects/HealthAI-Platform
npx bmad-method@alpha install --update

# 3. Re-analyze after update
python bmad_provisioner.py --config manifest.yaml --mode analyze
# Output: 3 leaders need update ⚠️

# 4. Re-provision custom skills
python bmad_provisioner.py --config manifest.yaml --mode provision
# Output: All skills restored ✅
```

## Manifest Structure

### Complete Example

See `templates/skills-manifest-healthai.yaml` for complete example.

### Key Sections

**project** - Project configuration
```yaml
project:
  name: HealthAI-Platform
  bmad_version: v6.x
  root: ~/projects/HealthAI-Platform
```

**leaders** - Leader definitions
```yaml
leaders:
  - name: dev-leader
    domain: healthcare
    phase: 4-implementation
    specialists:
      - id: frontend
        name: Frontend Developer
        domain: React, Vue
        skills: [UI, styling]
```

**customizations** - Agent customizations
```yaml
customizations:
  dev-leader:
    memories:
      - "HealthAI uses React + FastAPI"
    principles:
      - "Always check HIPAA compliance"
```

**integration** - Workflow integration
```yaml
integration:
  workflows:
    - phase: 4-implementation
      name: healthai-dev-workflow
      sequence: [sm, dev-leader, specialist, qa-leader]
```

## Architecture

```
bmad-provisioner/
├── bmad_provisioner.py       # CLI entry point
├── models/
│   └── manifest.py            # Manifest parsing
├── core/
│   └── analyzer.py            # Gap analysis
├── templates/
│   └── skills-manifest-*.yaml # Example manifests
└── tests/
    └── test_*.py              # Unit tests
```

## Current Status

### ✅ Implemented (v0.1-alpha)

- Manifest parsing and validation
- Gap analysis (detect missing/outdated)
- CLI with multiple modes
- BMAD version detection
- File status checking
- Recommendations engine

### 🚧 TODO (v0.2)

- Actual provisioning (generator integration)
- Smart CSV merging
- Backup/restore
- Workflow integration generation
- Multi-project support

### 🔮 Future (v1.0)

- CI/CD integration
- Web UI dashboard
- Version migration helpers
- Skills marketplace integration

## Development

### Requirements

```bash
pip install pyyaml  # For YAML parsing
```

### Testing

```bash
# Validate manifest
python bmad_provisioner.py --config test-manifest.yaml --mode validate

# Analyze with test project
python bmad_provisioner.py \
  --config test-manifest.yaml \
  --project-root /tmp/test-project \
  --mode analyze
```

## Integration with bmad-skill-generator

Next step: Connect provisioner with existing `bmad-skill-generator` to actually generate files.

```python
# In core/generator.py (TODO)
from bmad_skill_generator.scripts.init_bmad_skill import generate_skill

def provision_leader(leader_config):
    generate_skill(
        name=leader_config.name,
        domain=leader_config.domain,
        specialists=leader_config.specialists,
        output=project_root / "_bmad/custom-skills"
    )
```

## License

MIT

## Author

Created during epic Claude + Khaled car session 🚗☕
