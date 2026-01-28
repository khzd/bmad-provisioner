---
name: architect-leader
description: Architect leader with specialized agents: System Architect, Integration Architect, Risk Architect. Use when needing domain-specific expertise with coordination. Leader routes to appropriate specialist based on context.
bmad:
  compatible_versions: ['v6.x']
  phases: [2, 3, 4]
  agents: ["leader-architect"] + ["specialist-system-arch", "specialist-integration-arch", "specialist-risk-arch"]
  pattern: leader-specialists
---

# Architect Leader

## Overview

Leader-Specialists pattern for architect domain with 3 specialized agents.

## Architecture

```
Architect Leader (Router)
    ↓
    ├─→ System Architect

    ├─→ Integration Architect
    └─→ {specialists[-1]['name']}
```

## Agents

### Leader: {leader_name}
**File**: `agents/leader-{leader_name}.md`

Coordinates routing to specialists based on domain analysis.

### Specialists


**1. System Architect**  
**File**: `agents/specialist-system-arch.md`  
**Domain**: System Architecture, Scalability

**2. Integration Architect**  
**File**: `agents/specialist-integration-arch.md`  
**Domain**: Integration Architecture, API Design

**3. Risk Architect**  
**File**: `agents/specialist-risk-arch.md`  
**Domain**: Security & Compliance


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

- `specialist-system-arch.md`: Specialist in System Architecture, Scalability
- `specialist-integration-arch.md`: Specialist in Integration Architecture, API Design
- `specialist-risk-arch.md`: Specialist in Security & Compliance

### workflows/
- `route-to-specialist.yaml`: Routing workflow

### references/
- `routing-rules.md`: Routing decision matrix
