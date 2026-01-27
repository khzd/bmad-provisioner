# BMAD Method Structure Reference

## Directory Structure

```
project-root/
├── _bmad/                          # BMad installation directory
│   ├── _config/
│   │   ├── agents/                 # Agent customization files
│   │   │   ├── bmm-dev.customize.yaml
│   │   │   ├── bmm-pm.customize.yaml
│   │   │   └── ...
│   │   └── modules/                # Module configurations
│   ├── agents/                     # Compiled agent prompts
│   │   ├── bmm-analyst.md
│   │   ├── bmm-architect.md
│   │   ├── bmm-dev.md
│   │   ├── bmm-pm.md
│   │   ├── bmm-sm.md              # Scrum Master
│   │   ├── bmm-ux.md              # UX Designer
│   │   ├── bmm-qa.md
│   │   └── ...
│   ├── workflows/                  # YAML workflow definitions
│   │   ├── 0-init-workflows/
│   │   ├── 1-discovery-workflows/
│   │   ├── 2-plan-workflows/
│   │   ├── 3-arch-workflows/
│   │   └── 4-dev-workflows/
│   └── modules/                    # Installed modules
│       ├── bmm/                    # BMad Method Module
│       ├── bmb/                    # BMad Builder Module
│       └── bmgd/                   # Game Dev Studio (optional)
├── .docs/                          # Generated documentation
│   ├── project-brief.md
│   ├── prd.md                      # Product Requirements Document
│   ├── architecture.md
│   ├── tech-spec.md
│   ├── epics/                      # Sharded epic files
│   │   ├── epic-1-auth.md
│   │   ├── epic-2-ui.md
│   │   └── ...
│   └── stories/                    # Individual story files
│       ├── story-1-login.md
│       ├── story-2-dashboard.md
│       └── ...
├── bmm-workflow-status.yaml        # Workflow tracking
└── sprint-status.yaml              # Sprint tracking
```

## Core Concepts

### 1. Agents

Specialized AI personas with domain expertise:

- **Analyst**: Project brainstorming, market research, problem definition
- **PM** (Product Manager): PRD creation, epic/story breakdown
- **Architect**: System design, tech stack, architecture decisions
- **SM** (Scrum Master): Sprint planning, story management, retrospectives
- **Dev**: Implementation, code generation, testing
- **QA**: Code review, quality assurance
- **UX Designer**: User experience design, wireframes
- **PO** (Product Owner): Document validation, alignment checks

### 2. Workflows

YAML-based structured processes:
- **Phases**: 0-Init, 1-Discovery, 2-Plan, 3-Architecture, 4-Development
- **Sequence**: Ordered steps with agent assignments
- **Dependencies**: Required documents from previous steps
- **Handoffs**: Clear transition points between agents

### 3. Planning Tracks

Scale-adaptive intelligence:

| Track | Complexity | Planning Depth | Time to Code |
|-------|-----------|----------------|--------------|
| Quick Flow | Level 0-1 | Minimal | 10-30 min |
| BMad Method | Level 2-3 | Full | 30 min - 2h |
| Enterprise | Level 4 | Comprehensive | 1-3 hours |

### 4. Document Flow

```
project-brief.md → prd.md → architecture.md → tech-spec.md → stories/*.md
```

Each document feeds the next, ensuring consistency and traceability.

## Agent Customization

### Structure: `_bmad/_config/agents/{agent-name}.customize.yaml`

```yaml
persona:
  role: 'Senior Full-Stack Engineer'
  identity: 'Your custom identity'
  communication_style: 'Professional'
  principles:
    - 'Principle 1'
    - 'Principle 2'

memories:
  - 'Persistent context item 1'
  - 'Persistent context item 2'

menu:
  - trigger: custom-workflow
    workflow: '{project-root}/custom/workflow.yaml'
    description: Custom workflow description
```

## Workflow Structure

### YAML Workflow Definition

```yaml
name: workflow-name
description: Workflow purpose
phase: 2-plan
sequence:
  - agent: analyst
    action: create-brief
    dependencies:
      - file: .docs/project-brief.md
    outputs:
      - .docs/project-brief.md
  
  - agent: pm
    action: create-prd
    dependencies:
      - file: .docs/project-brief.md
    outputs:
      - .docs/prd.md
```

## Key Commands

- `/bmad-help` - Context-aware help system
- `/{agent-name}` - Load specific agent
- `/workflow-init` - Initialize project tracking
- `/workflow-status` - Check progress
- `/quick-spec` - Fast tech-spec for simple features
- `/sprint-planning` - Create sprint with stories
- `/retrospective` - Complete epic review

## Module System

### Official Modules

1. **BMM** (BMad Method): Core agile workflow (21 agents, 50+ workflows)
2. **BMB** (BMad Builder): Create custom agents/workflows/modules
3. **BMGD** (Game Dev Studio): Game development workflows
4. **CIS** (Creative Intelligence Suite): Innovation & design thinking

### Module Structure

```
module-name/
├── agents/
│   ├── module-agent-1.md
│   └── module-agent-2.md
├── workflows/
│   ├── workflow-1.yaml
│   └── workflow-2.yaml
├── config/
│   └── module.yaml
└── package.json
```

## Best Practices

1. **Fresh Chats**: Start new chat for each workflow (avoids context limits)
2. **Sequential Execution**: Follow phase order (0→1→2→3→4)
3. **Document Dependencies**: Always check required inputs exist
4. **Validation**: Run PO master-checklist between phases
5. **Sharding**: Use PO to shard large docs into focused files
6. **Customization**: Override agents via customize.yaml, not core files

## Integration Points

- **IDE**: Claude Code, Cursor, Windsurf, VS Code
- **Version Control**: Works with Git workflows
- **CI/CD**: Generates deployment-ready structures
- **Documentation**: Auto-generates comprehensive docs

## References

- Official Repo: https://github.com/bmad-code-org/BMAD-METHOD
- Documentation: https://docs.bmad-method.org
- Discord: https://discord.gg/gk8jAdXWmj
