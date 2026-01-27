---
name: bmad-skill-generator
description: Generate skills following BMAD v6 alpha methodology for healthcare AI projects. Use when creating skills that need BMAD directory structure (governance, products, shared infrastructure), separation of concerns between vision (Claude Web) and implementation (Claude Code), comprehensive non-functional requirements, and compliance-first approach. Triggers on requests like "create a BMAD skill", "generate skill with BMAD structure", or healthcare AI development needing proper governance framework.
---

# BMAD Skill Generator

## Overview

Generate skills following BMAD v6 alpha methodology - a comprehensive framework for healthcare AI development emphasizing separation of concerns, compliance-first approach, and proper governance structure.

## Workflow

### Step 1: Understand Skill Requirements

Ask user:
- Skill name and purpose
- Target product line (HealthAI-Platform, other)
- Required compliance level (HIPAA, RGPD, etc.)
- Vision vs implementation scope

### Step 2: Generate Base Structure

Execute `scripts/init_bmad_skill.py` with parameters:
```bash
python scripts/init_bmad_skill.py <skill-name> --product <product-line> --compliance <level>
```

### Step 3: Populate References

Read `references/bmad-v6-methodology.md` for complete methodology details.

Add to skill's references/:
- Compliance requirements
- Architecture constraints
- Security guidelines
- Integration patterns

### Step 4: Create Scripts

Add automation scripts for:
- Directory structure validation
- Compliance checks
- Documentation generation
- Template instantiation

### Step 5: Configure Assets

Include templates:
- README.md structure
- .gitkeep files
- Docker configurations
- CI/CD pipelines

### Step 6: Validate & Package

Run validation then package:
```bash
scripts/package_skill.py <path/to/skill>
```

## Resources

### scripts/
- `init_bmad_skill.py`: Generate BMAD-compliant skill structure

### references/
- `bmad-v6-methodology.md`: Complete BMAD v6 alpha methodology
- `directory-structure.md`: Standard directory templates
- `compliance-requirements.md`: Healthcare compliance guidelines

### assets/
- `templates/`: Boilerplate files for skills
- `configs/`: Docker, Git, CI/CD configurations
