---
name: dev-leader
description: Dev leader with specialized agents: Frontend Developer, Backend Developer, Middleware Developer. Use when needing domain-specific expertise with coordination. Leader routes to appropriate specialist based on context.
bmad:
  compatible_versions: ['v6.x']
  phases: [2, 3, 4]
  agents: ["leader-dev"] + ["specialist-frontend", "specialist-backend", "specialist-middleware"]
  pattern: leader-specialists
---

# Dev Leader

## Overview

Leader-Specialists pattern for dev domain with 3 specialized agents.

## Architecture

```
Dev Leader (Router)
    ↓
    ├─→ Frontend Developer

    ├─→ Backend Developer
    └─→ {specialists[-1]['name']}
```

## Agents

### Leader: {leader_name}
**File**: `agents/leader-{leader_name}.md`

Coordinates routing to specialists based on domain analysis.

### Specialists


**1. Frontend Developer**  
**File**: `agents/specialist-frontend.md`  
**Domain**: React, Vue, CSS

**2. Backend Developer**  
**File**: `agents/specialist-backend.md`  
**Domain**: FastAPI, Database

**3. Middleware Developer**  
**File**: `agents/specialist-middleware.md`  
**Domain**: API Gateway, Integration


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

- `specialist-frontend.md`: Specialist in React, Vue, CSS
- `specialist-backend.md`: Specialist in FastAPI, Database
- `specialist-middleware.md`: Specialist in API Gateway, Integration

### workflows/
- `route-to-specialist.yaml`: Routing workflow

### references/
- `routing-rules.md`: Routing decision matrix
