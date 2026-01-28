---
name: cis-leader
description: Cis leader with specialized agents: Innovation Strategist, Research Analyst, Storytelling Expert. Use when needing domain-specific expertise with coordination. Leader routes to appropriate specialist based on context.
bmad:
  compatible_versions: ['v6.x']
  phases: [2, 3, 4]
  agents: ["leader-cis"] + ["specialist-innovation", "specialist-research", "specialist-storytelling"]
  pattern: leader-specialists
---

# Cis Leader

## Overview

Leader-Specialists pattern for cis domain with 3 specialized agents.

## Architecture

```
Cis Leader (Router)
    ↓
    ├─→ Innovation Strategist

    ├─→ Research Analyst
    └─→ {specialists[-1]['name']}
```

## Agents

### Leader: {leader_name}
**File**: `agents/leader-{leader_name}.md`

Coordinates routing to specialists based on domain analysis.

### Specialists


**1. Innovation Strategist**  
**File**: `agents/specialist-innovation.md`  
**Domain**: Design thinking, ideation

**2. Research Analyst**  
**File**: `agents/specialist-research.md`  
**Domain**: Market analysis, user research

**3. Storytelling Expert**  
**File**: `agents/specialist-storytelling.md`  
**Domain**: Narrative design, communication


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

- `specialist-innovation.md`: Specialist in Design thinking, ideation
- `specialist-research.md`: Specialist in Market analysis, user research
- `specialist-storytelling.md`: Specialist in Narrative design, communication

### workflows/
- `route-to-specialist.yaml`: Routing workflow

### references/
- `routing-rules.md`: Routing decision matrix
