# Test Provisioning v0.2

## Setup

```bash
# Dans ~/Bureau/tools/bmad-provisioner/src
source venv-bp/bin/activate

# Copier le skill-generator à côté
cp -r /path/to/bmad-skill-generator ./
```

## Test 1: Provision dry-run

```bash
python bmad_provisioner.py \
  --config templates/skills-manifest-bmad-provisioner.yaml \
  --generator-script bmad-skill-generator/scripts/init_bmad_skill.py \
  --mode provision \
  --dry-run
```

**Expected**: Preview sans changements

## Test 2: Provision REAL

```bash
python bmad_provisioner.py \
  --config templates/skills-manifest-bmad-provisioner.yaml \
  --generator-script bmad-skill-generator/scripts/init_bmad_skill.py \
  --mode provision
```

**Expected**:
- ✅ Backup custom-skills
- 🔨 Generate dev-leader
- 🔨 Generate qa-leader  
- 🔨 Generate cis-leader
- ✅ Summary

## Test 3: Verify

```bash
# Check generated files
ls -la ~/Bureau/tools/bmad-provisioner/_bmad/custom-skills/

# Should see:
# - dev-leader/
# - qa-leader/
# - cis-leader/

# Check customize files
ls -la ~/Bureau/tools/bmad-provisioner/_bmad/_config/agents/

# Should see:
# - custom-dev-leader.customize.yaml
# - custom-qa-leader.customize.yaml
# - custom-cis-leader.customize.yaml
```

## Test 4: Re-analyze

```bash
python bmad_provisioner.py \
  --config templates/skills-manifest-bmad-provisioner.yaml \
  --mode analyze
```

**Expected**: ✅ All leaders up to date

## Troubleshooting

**"Generator script not found"**
- Check path with --generator-script
- Or copy bmad-skill-generator to current directory

**"Could not find bmad-skill-generator"**
- Provisioner auto-detects in: ../, ../../, ~/bmad-tools/
- Specify manually with --generator-script

**Permission issues**
- chmod +x bmad-skill-generator/scripts/init_bmad_skill.py
