# BMAD Provisioner - Documentation Index

## Project Overview

**BMAD Provisioner** is a Python CLI tool designed to manage custom BMAD (Business Model Architecture Design) skills across multiple projects with declarative configuration. It provides infrastructure-as-code capabilities for BMAD skill management, ensuring configurations survive framework updates.

### Project Metadata

- **Type:** CLI Tool (Command Line Interface)
- **Language:** Python 3.11+
- **Framework:** BMAD v6.x compatible
- **Architecture:** Monolith with modular components
- **License:** MIT
- **Version:** 1.0

### Quick Reference

- **Primary Technology:** Python CLI with YAML configuration
- **Entry Point:** `src/bmad_provisioner.py`
- **Architecture Pattern:** Modular CLI with separation of concerns
- **Repository Type:** Monolith (single cohesive project)

### Project Structure Summary

```
bmad-provisioner/
├── src/                          # Main source code
│   ├── bmad_provisioner.py       # CLI entry point
│   ├── models/                   # Data models and validation
│   ├── core/                     # Core business logic
│   ├── templates/               # Configuration examples
│   └── tests/                   # Test files
├── docs/                         # Documentation (this directory)
└── _bmad/                        # BMAD integration (if present)
```

## Generated Documentation

### 📋 Project Documentation

- [Project Overview](./project-overview.md) - Executive summary and project metadata
- [Architecture](./architecture.md) - Technical architecture and system design
- [Development Guide](./development-guide.md) - Developer setup and coding guidelines
- [User Guide](./user-guide.md) - End-user instructions and usage examples

### 📚 Existing Documentation

- [Product Requirements Document](./PRD.md) - Business requirements and specifications

## Getting Started

### For Developers

1. **Setup:** Follow the [Development Guide](./development-guide.md) for environment setup
2. **Architecture:** Review the [Architecture](./architecture.md) document for system understanding
3. **Contribution:** Check coding standards and contribution guidelines

### For Users

1. **Installation:** See [User Guide](./user-guide.md) for quick start instructions
2. **Basic Usage:** Learn CLI commands and operation modes
3. **Configuration:** Understand skills manifest structure and customization

### For Project Managers

1. **Requirements:** Review [PRD.md](./PRD.md) for business context
2. **Architecture:** Understand technical decisions in [Architecture](./architecture.md)
3. **Documentation:** Use this index as primary reference point

## Documentation Navigation

### By Role

#### 🧑‍💻 Developers
- [Development Guide](./development-guide.md) - Setup, coding standards, testing
- [Architecture](./architecture.md) - System design and component interactions
- [Project Overview](./project-overview.md) - Technical context

#### 👥 End Users
- [User Guide](./user-guide.md) - Usage instructions and examples
- [Project Overview](./project-overview.md) - Product understanding

#### 👔 Project Managers
- [PRD.md](./PRD.md) - Business requirements and specifications
- [Architecture](./architecture.md) - Technical overview
- [Project Overview](./project-overview.md) - Executive summary

### By Topic

#### 🛠️ Technical Topics
- **Architecture:** [Architecture](./architecture.md)
- **Development:** [Development Guide](./development-guide.md)
- **System Design:** [Architecture](./architecture.md)

#### 📖 Usage Topics
- **Getting Started:** [User Guide](./user-guide.md)
- **Configuration:** [User Guide](./user-guide.md)
- **Examples:** [User Guide](./user-guide.md)

#### 📊 Business Topics
- **Requirements:** [PRD.md](./PRD.md)
- **Project Context:** [Project Overview](./project-overview.md)
- **Specifications:** [PRD.md](./PRD.md)

## Key Concepts

### CLI Tool Architecture
The BMAD Provisioner follows a modular CLI architecture with clear separation between:
- **Configuration Management** (`models/`)
- **Core Logic** (`core/`)
- **User Interface** (`bmad_provisioner.py`)

### BMAD Integration
- **Framework Compatibility:** BMAD v6.x
- **Workflow Support:** Quick Flow (Phase 0-1-2-3-4)
- **Pattern Support:** Leader-Specialists architecture

### Declarative Configuration
- **Format:** YAML manifests
- **Validation:** Schema-based validation
- **Versioning:** Configuration version management

## Next Steps

### For New Team Members
1. Read [Project Overview](./project-overview.md) for context
2. Follow [Development Guide](./development-guide.md) for setup
3. Review [Architecture](./architecture.md) for system understanding

### For Users
1. Start with [User Guide](./user-guide.md) for basic usage
2. Explore [Project Overview](./project-overview.md) for product context
3. Refer to [User Guide](./user-guide.md) for advanced features

### For Contributors
1. Review [Development Guide](./development-guide.md) for standards
2. Understand [Architecture](./architecture.md) for design decisions
3. Check [PRD.md](./PRD.md) for business context

## Documentation Maintenance

This documentation is automatically generated and maintained as part of the project. For updates or corrections:

1. **Content Updates:** Modify the relevant source files
2. **Structure Changes:** Update this index accordingly
3. **New Documentation:** Add to appropriate sections and update this index

## Contact and Support

For questions about this documentation:

- **Development Questions:** Refer to [Development Guide](./development-guide.md)
- **Usage Questions:** See [User Guide](./user-guide.md)
- **Business Questions:** Check [PRD.md](./PRD.md)

## Version Information

- **Documentation Version:** 1.0
- **Last Updated:** 28/01/2026
- **Generated By:** BMAD Provisioner Documentation Workflow

---

**This index serves as your primary entry point for understanding and working with the BMAD Provisioner project.**