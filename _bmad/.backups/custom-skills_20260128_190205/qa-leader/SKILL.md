---
name: qa-leader
description: Qa leader with specialized agents: Unit Test Specialist, Integration Test Specialist, E2E Test Specialist, Performance Test Specialist. Use when needing domain-specific expertise with coordination. Leader routes to appropriate specialist based on context.
bmad:
  compatible_versions: ['v6.x']
  phases: [2, 3, 4]
  agents: ["leader-qa"] + ["specialist-unit", "specialist-integration", "specialist-e2e", "specialist-performance"]
  pattern: leader-specialists
---

# Qa Leader

## Overview

Leader-Specialists pattern for qa domain with 4 specialized agents.

## Architecture

```
Qa Leader (Router)
    ↓
    ├─→ Unit Test Specialist

    ├─→ Integration Test Specialist
    ├─→ E2E Test Specialist
    └─→ {specialists[-1]['name']}
```

## Agents

### Leader: {leader_name}
**File**: `agents/leader-{leader_name}.md`

Coordinates routing to specialists based on domain analysis.

### Specialists


**1. Unit Test Specialist**  
**File**: `agents/specialist-unit.md`  
**Domain**: pytest, jest

**2. Integration Test Specialist**  
**File**: `agents/specialist-integration.md`  
**Domain**: API testing

**3. E2E Test Specialist**  
**File**: `agents/specialist-e2e.md`  
**Domain**: Playwright, Selenium

**4. Performance Test Specialist**  
**File**: `agents/specialist-performance.md`  
**Domain**: Load testing


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

- `specialist-unit.md`: Specialist in pytest, jest
- `specialist-integration.md`: Specialist in API testing
- `specialist-e2e.md`: Specialist in Playwright, Selenium
- `specialist-performance.md`: Specialist in Load testing

### workflows/
- `route-to-specialist.yaml`: Routing workflow

### references/
- `routing-rules.md`: Routing decision matrix
