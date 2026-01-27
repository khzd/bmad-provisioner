# BMAD-Compliant Skill Creation Patterns

## Overview

Creating skills that integrate seamlessly with BMAD Method requires following specific patterns that respect BMAD's agent-based architecture, workflow system, and document flow.

## Core Integration Patterns

### Pattern 1: Agent Extension Skill

**Use Case**: Add specialized domain expertise to existing agents

**Structure**:
```
skill-name/
├── SKILL.md
├── references/
│   ├── domain-knowledge.md
│   └── terminology.md
└── scripts/
    └── validate-domain-rules.py
```

**Integration Point**: Agent's `memories` section in customize.yaml
```yaml
memories:
  - "Domain expert in {skill-domain}"
  - "Always consult {skill-name} references for {specific-topic}"
```

**Example**: Healthcare compliance skill adds HIPAA knowledge to Architect agent

---

### Pattern 2: Workflow Skill

**Use Case**: Add new workflow to BMAD phases

**Structure**:
```
skill-name/
├── SKILL.md
├── workflows/
│   └── custom-workflow.yaml
└── references/
    └── workflow-guide.md
```

**Integration Point**: Agent's `menu` section
```yaml
menu:
  - trigger: custom-action
    workflow: '{project-root}/skills/{skill-name}/workflows/custom-workflow.yaml'
    description: Description of custom workflow
```

**Example**: Security audit workflow added to QA agent

---

### Pattern 3: Module Skill

**Use Case**: Create complete domain-specific module

**Structure**:
```
skill-name/
├── SKILL.md
├── agents/
│   ├── custom-agent-1.md
│   └── custom-agent-2.md
├── workflows/
│   ├── phase-1-workflow.yaml
│   └── phase-2-workflow.yaml
├── config/
│   └── module.yaml
└── references/
    └── domain-guide.md
```

**Integration Point**: BMad module system via `npx bmad-method install`

**Example**: Legal compliance module with Compliance Officer agent

---

### Pattern 4: Document Template Skill

**Use Case**: Standardize document generation

**Structure**:
```
skill-name/
├── SKILL.md
├── assets/
│   ├── template-prd.md
│   ├── template-architecture.md
│   └── template-story.md
└── references/
    └── template-guide.md
```

**Integration Point**: Workflow dependencies
```yaml
- agent: pm
  action: create-prd
  dependencies:
    - file: skills/{skill-name}/assets/template-prd.md
```

**Example**: Medical device PRD template with FDA requirements

---

### Pattern 5: Validation Skill

**Use Case**: Add quality checks to workflows

**Structure**:
```
skill-name/
├── SKILL.md
├── scripts/
│   ├── validate-compliance.py
│   └── check-requirements.py
└── references/
    └── validation-rules.md
```

**Integration Point**: Workflow steps
```yaml
- agent: qa
  action: validate-output
  dependencies:
    - file: .docs/prd.md
  validation:
    script: skills/{skill-name}/scripts/validate-compliance.py
```

**Example**: RGPD compliance validator for architecture docs

---

## BMAD-Specific Requirements

### 1. Respect Phase Structure

Skills must align with BMAD phases:
- **Phase 0**: Initialization
- **Phase 1**: Discovery/Brainstorming
- **Phase 2**: Planning (PRD creation)
- **Phase 3**: Architecture
- **Phase 4**: Development

### 2. Document Dependencies

Always declare required documents:
```yaml
dependencies:
  - file: .docs/project-brief.md
    required: true
  - file: .docs/architecture.md
    required: false
```

### 3. Agent Handoffs

Clear transition points:
```yaml
- agent: architect
  action: complete-design
  outputs:
    - .docs/architecture.md
  handoff:
    to: sm
    trigger: sprint-planning
```

### 4. Context Management

- **Fresh Chats**: Document when fresh chat needed
- **Memory**: Use agent memories for persistent context
- **Sharding**: Support document sharding for large outputs

### 5. Workflow YAML Compliance

Required fields:
```yaml
name: workflow-name
description: Clear description
phase: 1-discovery | 2-plan | 3-arch | 4-dev
sequence:
  - agent: agent-name
    action: action-description
    dependencies: []
    outputs: []
```

## Anti-Patterns to Avoid

### ❌ Don't: Bypass Agent System
```yaml
# BAD: Direct script execution without agent
- action: run-script
  script: custom-script.py
```

### ✅ Do: Use Agent Wrapper
```yaml
# GOOD: Agent executes script
- agent: custom-agent
  action: process-data
  tool: scripts/custom-script.py
```

### ❌ Don't: Hardcode Paths
```yaml
# BAD
dependencies:
  - file: /home/user/project/.docs/prd.md
```

### ✅ Do: Use Variables
```yaml
# GOOD
dependencies:
  - file: '{project-root}/.docs/prd.md'
```

### ❌ Don't: Ignore Dependencies
```yaml
# BAD: No dependency check
- agent: dev
  action: implement-feature
```

### ✅ Do: Declare Dependencies
```yaml
# GOOD
- agent: dev
  action: implement-feature
  dependencies:
    - file: .docs/architecture.md
    - file: .docs/stories/story-1.md
```

## Skill Metadata for BMAD

### SKILL.md Frontmatter Extensions

```yaml
---
name: skill-name
description: Standard description
bmad:
  compatible_versions: ["v6.x", "v7.x"]
  phases: [2, 3, 4]
  agents: ["architect", "dev", "qa"]
  requires_modules: ["bmm"]
  optional_modules: ["bmb", "bmgd"]
---
```

## Testing BMAD Integration

### Checklist

- [ ] Skill follows BMAD directory conventions
- [ ] Agent customizations use `.customize.yaml`
- [ ] Workflows declare all dependencies
- [ ] Workflow YAML validates against BMAD schema
- [ ] Fresh chat requirements documented
- [ ] Context limits considered
- [ ] Handoffs clearly defined
- [ ] Compatible with Quick Flow / BMad Method / Enterprise tracks
- [ ] Module installation tested
- [ ] Works with Claude Code, Cursor, Windsurf

## Example: Complete Healthcare Skill

```
healthcare-compliance/
├── SKILL.md
│   └── bmad: {phases: [2,3], agents: ["architect", "qa"]}
├── agents/
│   └── compliance-officer.md
├── workflows/
│   ├── hipaa-review.yaml
│   └── risk-assessment.yaml
├── references/
│   ├── hipaa-requirements.md
│   ├── rgpd-checklist.md
│   └── fda-guidelines.md
├── scripts/
│   ├── validate-phi-handling.py
│   └── audit-trail-generator.py
└── assets/
    └── compliance-report-template.md
```

**Integration**:
```yaml
# _bmad/_config/agents/bmm-architect.customize.yaml
persona:
  principles:
    - "Healthcare data requires HIPAA compliance"

memories:
  - "Project is healthcare-related, consult healthcare-compliance skill"

menu:
  - trigger: hipaa-review
    workflow: '{project-root}/skills/healthcare-compliance/workflows/hipaa-review.yaml'
    description: Review architecture for HIPAA compliance
```

## References

- BMAD Method Structure: See `bmad-method-structure.md`
- Official Workflow Schema: https://github.com/bmad-code-org/BMAD-METHOD/tree/main/src/workflows
- Agent Customization: https://docs.bmad-method.org/how-to/customization/
