# BMAD Provisioner - User Guide

## Overview

This user guide provides comprehensive instructions for using the BMAD Provisioner to manage custom BMAD skills across multiple projects. Whether you're a developer, team lead, or project manager, this guide will help you get the most out of the tool.

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Basic Usage](#2-basic-usage)
3. [Configuration](#3-configuration)
4. [Advanced Features](#4-advanced-features)
5. [Best Practices](#5-best-practices)
6. [Troubleshooting](#6-troubleshooting)
7. [Examples](#7-examples)

## 1. Getting Started

### 1.1 Installation

#### Prerequisites
- Python 3.11 or higher
- Git (for cloning the repository)
- Access to BMAD framework

#### Quick Start
```bash
# Clone the repository
git clone <repository-url>
cd bmad-provisioner

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python bmad_provisioner.py --help
```

### 1.2 Understanding the Tool

The BMAD Provisioner is designed to:

1. **Analyze** your current BMAD configuration
2. **Compare** it against your desired state (defined in YAML)
3. **Provision** missing or outdated skills automatically
4. **Backup** your configurations for safety

## 2. Basic Usage

### 2.1 Command Line Interface

#### Basic Commands
```bash
# Show help
python bmad_provisioner.py --help

# Analyze current state
python bmad_provisioner.py --config skills-manifest.yaml --mode analyze

# Show what would change (dry run)
python bmad_provisioner.py --config skills-manifest.yaml --mode diff

# Provision skills (dry run first)
python bmad_provisioner.py --config skills-manifest.yaml --mode provision --dry-run

# Provision skills for real
python bmad_provisioner.py --config skills-manifest.yaml --mode provision
```

#### Command Options
- `--config, -c`: Path to skills manifest YAML file
- `--mode, -m`: Operation mode (analyze, provision, diff, validate)
- `--project-root, -p`: Override project root from manifest
- `--dry-run`: Preview changes without applying
- `--verbose, -v`: Verbose output
- `--generator-script, -g`: Path to bmad-skill-generator script

### 2.2 Operation Modes

#### Analyze Mode (Default)
Analyzes your current BMAD setup and compares it with your desired configuration.

```bash
python bmad_provisioner.py --config skills-manifest.yaml --mode analyze
```

**Output:**
```
📊 Analyzing project: HealthAI-Platform
   Root: /home/user/projects/HealthAI-Platform

🔍 Gap Analysis Report
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

#### Provision Mode
Automatically provisions missing or outdated skills.

```bash
# Dry run first (recommended)
python bmad_provisioner.py --config skills-manifest.yaml --mode provision --dry-run

# For real
python bmad_provisioner.py --config skills-manifest.yaml --mode provision
```

#### Diff Mode
Shows exactly what would change without making any modifications.

```bash
python bmad_provisioner.py --config skills-manifest.yaml --mode diff
```

#### Validate Mode
Validates your manifest file without performing any operations.

```bash
python bmad_provisioner.py --config skills-manifest.yaml --mode validate
```

## 3. Configuration

### 3.1 Skills Manifest Structure

The skills manifest is a YAML file that defines your desired BMAD configuration.

#### Basic Structure
```yaml
project:
  name: Your-Project-Name
  bmad_version: v6.x
  root: /path/to/your/project

  leaders:
    - name: dev-leader
      domain: your-domain
      phase: 4-implementation
      specialists:
        - id: frontend
          name: Frontend Developer
          domain: React, Vue
          skills: [UI, styling]
    
    - name: qa-leader
      domain: testing
      phase: 4-implementation
      specialists:
        - id: unit
          name: Unit Test Specialist
          domain: pytest, jest
          skills: [TDD, mocking]
```

### 3.2 Creating Your First Manifest

#### Step 1: Choose a Template
Start with one of the provided templates:
- `templates/skills-manifest-bmad-provisioner.yaml` - Basic template
- `templates/skills-manifest-healthai.yaml` - Healthcare example

#### Step 2: Customize for Your Project
```bash
# Copy template
cp templates/skills-manifest-bmad-provisioner.yaml my-project-manifest.yaml

# Edit the file
nano my-project-manifest.yaml
```

#### Step 3: Validate Your Manifest
```bash
python bmad_provisioner.py --config my-project-manifest.yaml --mode validate
```

### 3.3 Advanced Configuration

#### Customizations
Add custom configurations for specific leaders:

```yaml
customizations:
  dev-leader:
    memories:
      - "Your project uses React frontend with FastAPI backend"
      - "All data must comply with relevant regulations"
    
    principles:
      - "Always check compliance before implementation"
      - "Prefer standard data models over custom ones"
    
    menu_additions:
      - trigger: custom-workflow
        workflow: '{project-root}/_bmad/custom-skills/dev-leader/workflows/custom.yaml'
        description: "[CUSTOM] Custom development workflow"
```

#### Integration Workflows
Define custom workflows that integrate multiple leaders:

```yaml
integration:
  workflows:
    - phase: 4-implementation
      name: custom-dev-workflow
      sequence:
        - sm              # Story loaded
        - dev-leader      # Routes to specialist
        - specialist      # Implements
        - qa-leader       # Routes to test specialist
        - test-specialist # Tests
```

## 4. Advanced Features

### 4.1 Multi-Project Management

#### Project Isolation
Each project has its own isolated configuration:

```
projects/
├── project-a/
│   ├── skills-manifest.yaml
│   └── _bmad/
├── project-b/
│   ├── skills-manifest.yaml
│   └── _bmad/
└── project-c/
    ├── skills-manifest.yaml
    └── _bmad/
```

#### Cross-Project Sharing
Share skills between projects using the integration section:

```yaml
integration:
  shared_skills:
    - common-leader
    - shared-specialist
```

### 4.2 Backup and Restore

#### Automatic Backups
The provisioner automatically creates backups before making changes:

```bash
# Check available backups
ls -la ~/.bmad-provisioner/backups/

# Restore from backup
python bmad_provisioner.py --config manifest.yaml --mode restore --backup-path /path/to/backup
```

#### Manual Backup
```bash
# Create manual backup
python bmad_provisioner.py --config manifest.yaml --mode backup
```

### 4.3 Custom Skill Generation

#### Using bmad-skill-generator
The provisioner integrates with the bmad-skill-generator for advanced skill creation:

```bash
# Specify custom generator script
python bmad_provisioner.py \
  --config manifest.yaml \
  --generator-script /path/to/custom-generator.py \
  --mode provision
```

#### Custom Templates
Create custom skill templates:

```yaml
templates:
  custom-skill-template:
    name: "Custom Skill"
    description: "Custom skill template"
    files:
      - path: "agents/custom-agent.md"
        template: "custom-agent-template.md"
```

## 5. Best Practices

### 5.1 Configuration Management

#### Version Control
Always keep your skills manifest under version control:

```bash
# Add to git
git add skills-manifest.yaml
git commit -m "Update skills configuration"
git push
```

#### Environment-Specific Configs
Create different manifests for different environments:

```
config/
├── development.yaml
├── staging.yaml
└── production.yaml
```

#### Change Management
```bash
# Always dry-run first
python bmad_provisioner.py --config manifest.yaml --mode provision --dry-run

# Review changes
python bmad_provisioner.py --config manifest.yaml --mode diff

# Apply changes
python bmad_provisioner.py --config manifest.yaml --mode provision
```

### 5.2 Team Collaboration

#### Shared Templates
Create organization-wide skill templates:

```yaml
# organization-templates.yaml
project:
  name: Organization-Template
  bmad_version: v6.x
  root: /shared/templates

  leaders:
    - name: standard-dev-leader
      domain: generic
      specialists:
        - id: frontend
          name: Frontend Developer
          domain: React, Vue, Angular
          skills: [UI, styling, responsive design]
```

#### Documentation
Document your custom skills and workflows:

```markdown
# Custom Skills Documentation

## dev-leader
- Purpose: Standard development workflow
- Specialists: frontend, backend, middleware
- Customizations: HIPAA compliance, FHIR integration

## qa-leader
- Purpose: Quality assurance workflow
- Specialists: unit, integration, e2e, performance
- Customizations: Healthcare data testing, compliance validation
```

### 5.3 Monitoring and Maintenance

#### Regular Analysis
Schedule regular gap analysis:

```bash
# Weekly analysis
python bmad_provisioner.py --config manifest.yaml --mode analyze > weekly-report.txt
```

#### Update Management
Track BMAD framework updates:

```bash
# Check BMAD version
python bmad_provisioner.py --config manifest.yaml --mode analyze | grep "BMAD Version"
```

#### Performance Monitoring
Monitor provisioner performance:

```bash
# Time the operation
time python bmad_provisioner.py --config manifest.yaml --mode provision
```

## 6. Troubleshooting

### 6.1 Common Issues

#### Permission Errors
```bash
# Fix file permissions
chmod +x bmad_provisioner.py

# Fix directory permissions
sudo chown -R $USER:$USER /path/to/project
```

#### Missing Dependencies
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Check Python version
python --version
```

#### BMAD Integration Issues
```bash
# Check BMAD installation
bmad --version

# Verify BMAD project structure
ls -la _bmad/
```

### 6.2 Debug Mode

Enable verbose output for troubleshooting:

```bash
python bmad_provisioner.py --config manifest.yaml --mode analyze --verbose
```

### 6.3 Getting Help

#### Documentation
- Check this user guide
- Review the README.md
- Look at example configurations

#### Community
- Report issues on GitHub
- Ask questions in discussions
- Check existing issues for solutions

## 7. Examples

### 7.1 Basic Project Setup

#### Step 1: Create Manifest
```yaml
# my-project.yaml
project:
  name: My-Project
  bmad_version: v6.x
  root: /home/user/projects/my-project

  leaders:
    - name: dev-leader
      domain: generic
      phase: 4-implementation
      specialists:
        - id: frontend
          name: Frontend Developer
          domain: React, Vue
          skills: [UI, styling]
        
        - id: backend
          name: Backend Developer
          domain: FastAPI, Database
          skills: [REST APIs, database design]
```

#### Step 2: Analyze Current State
```bash
python bmad_provisioner.py --config my-project.yaml --mode analyze
```

#### Step 3: Provision Skills
```bash
# Dry run
python bmad_provisioner.py --config my-project.yaml --mode provision --dry-run

# Apply
python bmad_provisioner.py --config my-project.yaml --mode provision
```

### 7.2 Healthcare Project Example

Based on the HealthAI template:

```yaml
# healthai-project.yaml
project:
  name: HealthAI-Platform
  bmad_version: v6.x
  root: /home/user/projects/HealthAI-Platform

  leaders:
    - name: dev-leader
      domain: healthcare
      specialists:
        - id: frontend
          name: Frontend Developer
          domain: React, Vue, CSS
          skills: [UI development, styling, components, FHIR dashboards]
        
        - id: backend
          name: Backend Developer
          domain: FastAPI, Database
          skills: [REST APIs, HL7/FHIR integration, healthcare data models]
    
    - name: qa-leader
      domain: healthcare
      specialists:
        - id: unit
          name: Unit Test Specialist
          domain: pytest, jest
          skills: [TDD, mocking, code coverage, healthcare data testing]
        
        - id: integration
          name: Integration Test Specialist
          domain: API testing
          skills: [REST testing, FHIR validation, contract tests]
```

### 7.3 Multi-Project Setup

#### Project Structure
```
organization/
├── project-a/
│   ├── skills-manifest.yaml
│   └── _bmad/
├── project-b/
│   ├── skills-manifest.yaml
│   └── _bmad/
└── shared-templates/
    ├── organization-template.yaml
    └── custom-skills/
```

#### Shared Configuration
```yaml
# organization-template.yaml
project:
  name: Organization-Shared
  bmad_version: v6.x
  root: /organization/shared-templates

  leaders:
    - name: standard-dev-leader
      domain: generic
      specialists:
        - id: frontend
          name: Frontend Developer
          domain: React, Vue, Angular
          skills: [UI, styling, responsive design]
```

This user guide provides comprehensive instructions for using the BMAD Provisioner effectively. For additional support, refer to the technical documentation or contact the development team.