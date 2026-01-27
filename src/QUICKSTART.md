# BMAD Provisioner - Quick Start

## Installation (1 minute)

```bash
# Extract
unzip bmad-provisioner-v0.1-alpha.zip
cd bmad-provisioner

# Install (creates venv-bp automatically)
bash install.sh

# Test
source venv-bp/bin/activate
python bmad_provisioner.py --help

# Or use wrapper
./run.sh --help
```

## First Run (2 minutes)

### 1. Create manifest

```bash
# Use template
cp templates/skills-manifest-healthai.yaml my-manifest.yaml

# Edit for your project
nano my-manifest.yaml
# Change: root: ~/projects/YOUR-PROJECT
```

### 2. Validate

```bash
# With venv activated
python bmad_provisioner.py \
  --config my-manifest.yaml \
  --mode validate

# Or with wrapper
./run.sh --config my-manifest.yaml --mode validate
```

### 3. Analyze

```bash
./run.sh --config my-manifest.yaml --mode analyze
```

Output:
```
📊 Gap Analysis Report
==================================================

BMAD Version: v6.2.1

❌ dev-leader: Not installed
❌ qa-leader: Not installed
❌ cis-leader: Not installed

💡 Recommendations:
   - Install 3 missing leaders
```

## Two Ways to Run

### Option 1: With wrapper (easier)
```bash
./run.sh --config manifest.yaml --mode analyze
```

### Option 2: Manual venv activation
```bash
source venv-bp/bin/activate
python bmad_provisioner.py --config manifest.yaml --mode analyze
deactivate  # when done
```

## Common Commands

### Check what's missing
```bash
./run.sh --config manifest.yaml --mode analyze
```

### See what would change
```bash
./run.sh --config manifest.yaml --mode diff
```

### Provision (when implemented)
```bash
# Dry run
./run.sh --config manifest.yaml --mode provision --dry-run

# Real
./run.sh --config manifest.yaml --mode provision
```

## Manifest Template

Minimal example:

```yaml
project:
  name: MyProject
  bmad_version: v6.x
  root: ~/projects/MyProject
  
  leaders:
    - name: dev-leader
      domain: generic
      specialists:
        - id: frontend
          name: Frontend Dev
          domain: React
          skills: [UI, components]
```

Full example: `templates/skills-manifest-healthai.yaml`

## Next Steps

1. ✅ Create manifest for your project
2. ✅ Run analyze to see current state
3. 🚧 Wait for v0.2 with actual provisioning
4. 📚 Read README.md for details

## Troubleshooting

**"Project root does not exist"**
- Check `root:` path in manifest
- Or use `--project-root /path/to/project`

**"BMAD not installed"**
- Install BMAD first: `npx bmad-method@alpha install`
- Or ignore if testing manifest

**"Module not found"**
- Run: `pip install -r requirements.txt`

## Support

- Full docs: `README.md`
- Example: `templates/skills-manifest-healthai.yaml`
- Issues: Check manifest validation first
