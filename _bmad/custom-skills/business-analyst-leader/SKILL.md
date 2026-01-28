---
name: business-analyst-leader
description: Business-Analyst leader with specialized agents: Healthcare Business Analyst, Finance Business Analyst, Marketing Business Analyst. Use when needing domain-specific expertise with coordination. Leader routes to appropriate specialist based on context.
bmad:
  compatible_versions: ['v6.x']
  phases: [2, 3, 4]
  agents: ["leader-business-analyst"] + ["specialist-healthcare-ba", "specialist-finance-ba", "specialist-marketing-ba"]
  pattern: leader-specialists
---

# Business Analyst Leader

## Overview

Leader-Specialists pattern for business-analyst domain with 3 specialized agents.

## Architecture

```
Business-Analyst Leader (Router)
    ↓
    ├─→ Healthcare Business Analyst

    ├─→ Finance Business Analyst
    └─→ {specialists[-1]['name']}
```

## Agents

### Leader: {leader_name}
**File**: `agents/leader-{leader_name}.md`

Coordinates routing to specialists based on domain analysis.

### Specialists


**1. Healthcare Business Analyst**  
**File**: `agents/specialist-healthcare-ba.md`  
**Domain**: Healthcare Domain, Medical Workflows

**2. Finance Business Analyst**  
**File**: `agents/specialist-finance-ba.md`  
**Domain**: Financial Domain, Banking

**3. Marketing Business Analyst**  
**File**: `agents/specialist-marketing-ba.md`  
**Domain**: Marketing Domain, Analytics


## Workflow

### Step 1: Load Leader
```
/{leader_name}
```

### Step 2: Leader Analyzes Request
Determines appropriate specialist based on:
- Domain keywords
- Context requirements
- Complexity level
- Cross-domain needs

### Step 3: Route to Specialist
Leader loads appropriate specialist agent

### Step 4: Specialist Executes
Domain expert handles specific work

### Step 5: Coordinate (if needed)
Leader coordinates multi-specialist work

## Usage Examples

### Example 1: Single Specialist
```
User: "I need {specialists[0]['domain']} work"
Leader: Analyzes → Routes to {specialists[0]['name']}
Specialist: Executes domain-specific work
```

### Example 2: Multi-Specialist
```
User: "I need integrated solution"
Leader: Coordinates {specialists[0]['name']} + {specialists[1]['name']}
Specialists: Execute in sequence
Leader: Integrates outputs
```

## Integration with BMAD

### Agent Customization
Add to `_bmad/_config/agents/bmm-{leader_name}.customize.yaml`:

```yaml
menu:
  - trigger: {leader_name}-specialist
    workflow: '{{project-root}}/skills/{skill_name}/workflows/route-to-specialist.yaml'
    description: Route to {leader_name} specialist
```

### Workflow Phase
Default phase: **{bmad_config.get('default_phase', '3-arch')}**

Adjust phase in workflow YAML as needed.

## References

- `references/routing-rules.md`: Complete routing logic
- See `bmad-method-structure.md` for BMAD integration patterns

## Resources

### agents/
- `leader-{leader_name}.md`: Main coordinator agent

- `specialist-healthcare-ba.md`: Specialist in Healthcare Domain, Medical Workflows
- `specialist-finance-ba.md`: Specialist in Financial Domain, Banking
- `specialist-marketing-ba.md`: Specialist in Marketing Domain, Analytics

### workflows/
- `route-to-specialist.yaml`: Routing workflow

### references/
- `routing-rules.md`: Routing decision matrix
