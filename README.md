# BMAD Skill Factory

[![Version](https://img.shields.io/badge/version-0.5.0-blue.svg)](https://github.com/khzd/bmad-skill-factory)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-brightgreen.svg)](https://www.python.org/)
[![BMAD](https://img.shields.io/badge/BMAD-v6.x-orange.svg)](https://github.com/bmad-code-org/BMAD-METHOD)

**Infrastructure as Code for BMAD Skills**

Industrial-grade custom skill provisioning, smart merging, and automated workflow generation for BMAD Method.

> 🏭 **Factory Pattern** - Not just copy-paste, but industrialized skill creation with repeatable quality and scalability.

---

## ✨ Why Skill Factory?

Traditional approach: Manual skill creation, copy-paste, no versioning
❌ Time-consuming
❌ Error-prone  
❌ No consistency
❌ Hard to scale

**BMAD Skill Factory approach: Infrastructure as Code**
✅ Declarative YAML manifests
✅ Automated generation
✅ Smart merging preserves customizations
✅ Version controlled
✅ Scales from 5 to 500 skills

---

## ✨ Features

- 🎯 **Declarative Configuration** - YAML-based skill manifests
- 🔄 **Smart CSV Merging** - Preserve custom data during re-provisioning
- 🤖 **Leader-Specialists Pattern** - Automated agent generation
- 📋 **Advanced Workflows** - Multi-step coordination with validation
- 🛡️ **Gap Analysis** - Detect missing/outdated skills
- 💾 **Automatic Backups** - Safe re-provisioning with rollback
- 📦 **Multi-Project Support** - Manage skills across projects

---

## 🚀 Quick Start

### Installation
```bash
# Clone repository
git clone https://github.com/khzd/bmad-provisioner.git
cd bmad-provisioner/src

# Install dependencies
bash install.sh
source venv-bp/bin/activate
```

### Basic Usage
```bash
# Validate manifest
python bmad_provisioner.py \
  --config templates/skills-manifest-example.yaml \
  --mode validate

# Analyze gaps
python bmad_provisioner.py \
  --config templates/skills-manifest-example.yaml \
  --mode analyze

# Provision skills
python bmad_provisioner.py \
  --config templates/skills-manifest-example.yaml \
  --generator-script bmad-skill-generator/scripts/init_bmad_skill.py \
  --mode provision
```

---

## 📋 Architecture
```
User defines skills-manifest.yaml
         ↓
   Gap Analysis
         ↓
   Generate Skills
         ↓
  Smart CSV Merge
         ↓
   Provision to _bmad/
```

### Generated Structure
```
_bmad/custom-skills/
├── business-analyst-leader/
│   ├── agents/
│   │   ├── leader-business-analyst.md
│   │   ├── leader-business-analyst.agent.yaml
│   │   ├── specialist-healthcare-ba.md
│   │   └── specialist-healthcare-ba.agent.yaml
│   ├── workflows/
│   │   ├── route-to-specialist.yaml
│   │   ├── business-analyst-complete.yaml
│   │   └── business-analyst-multi.yaml
│   └── references/
│       └── routing-rules.md
```

---

## 🎯 Use Cases

### 1. Healthcare AI Platform
```yaml
project:
  name: HealthAI-Platform
  leaders:
    - name: business-analyst-leader
      specialists:
        - healthcare-ba: HIPAA, PHI, FHIR expert
    
    - name: architect-leader
      specialists:
        - risk-arch: Security & compliance
    
    - name: dev-leader
      specialists:
        - frontend: React + FHIR dashboards
        - backend: FastAPI + medical data
```

### 2. Multi-Domain Development

5 pre-configured leaders:
- 📊 **business-analyst-leader** - Domain expertise (healthcare, finance, marketing)
- 🏗️ **architect-leader** - System architecture (system, integration, risk)
- 💻 **dev-leader** - Development (frontend, backend, middleware)
- 🧪 **qa-leader** - Quality assurance (unit, integration, e2e, performance)
- 💡 **cis-leader** - Creative intelligence (innovation, research, storytelling)

---

## 🔧 Configuration

### Skills Manifest Format
```yaml
project:
  name: my-project
  bmad_version: v6.x
  root: ~/projects/my-project
  
  leaders:
    - name: dev-leader
      domain: generic
      phase: 4-implementation
      specialists:
        - id: frontend
          name: Frontend Developer
          domain: React, Vue, CSS
          skills: [UI development, styling, components]
  
  customizations:
    dev-leader:
      memories:
        - "Project uses React + TypeScript"
        - "Prefer functional components"
      
      principles:
        - "Follow React best practices"
        - "Write comprehensive tests"
```

---

## 🛠️ Advanced Features

### Smart CSV Merging

Automatically preserves user modifications during re-provisioning:
```csv
# User adds custom row
My Custom Check,Custom validation,DONE

# Re-provision → Custom row preserved!
```

### Agent .yaml Generation

Generates BMAD-compliant agent metadata:
```yaml
name: specialist-frontend
type: specialist
leader: dev-leader
expertise:
  domain: React, Vue, CSS
  skills: [UI development, styling]
triggers: [/frontend]
```

### Advanced Workflows

Multi-step workflows with validation:
```yaml
steps:
  - analyze-request
  - route-to-specialist
  - leader-review
  - finalize (conditional)
```

---

## 📊 CLI Modes

| Mode | Description |
|------|-------------|
| `validate` | Validate manifest syntax and structure |
| `analyze` | Gap analysis (detect missing/outdated) |
| `diff` | Preview changes before provisioning |
| `provision` | Generate and install skills |

---

## 🏗️ Development

### Project Structure
```
bmad-provisioner/
├── src/
│   ├── bmad_provisioner.py      # CLI entry point
│   ├── models/
│   │   └── manifest.py           # Data models
│   ├── core/
│   │   ├── analyzer.py           # Gap analysis
│   │   ├── generator.py          # Skill generation
│   │   └── csv_merger.py         # Smart merging
│   ├── bmad-skill-generator/
│   │   └── scripts/
│   │       └── init_bmad_skill.py
│   └── templates/
│       └── skills-manifest-*.yaml
├── docs/                         # Documentation
└── _bmad/                        # BMAD integration
```

### Running Tests
```bash
# Test provisioning on fresh BMAD install
python bmad_provisioner.py \
  --config templates/skills-manifest-bmad-provisioner.yaml \
  --mode provision

# Verify all skills up to date
python bmad_provisioner.py \
  --config templates/skills-manifest-bmad-provisioner.yaml \
  --mode analyze
```

---

## 🤝 Contributing

Contributions welcome! Please read [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) - Breakthrough Method for Agile AI-Driven Development
- Leader-Specialists pattern inspired by enterprise software architecture

---

## 📚 Documentation

- [Architecture Guide](docs/architecture.md)
- [Development Guide](docs/development-guide.md)
- [User Guide](docs/user-guide.md)
- [PRD](docs/PRD.md)

---

## 🔗 Links

- **GitHub**: https://github.com/khzd/bmad-provisioner
- **Issues**: https://github.com/khzd/bmad-provisioner/issues
- **BMAD Method**: https://github.com/bmad-code-org/BMAD-METHOD

---

**Built with ❤️ for the BMAD community**