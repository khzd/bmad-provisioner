---
name: qa-leader
description: QA leader with specialized agents: Unit Test Specialist, Integration Test Specialist, E2E Test Specialist, Performance Test Specialist. Use when needing domain-specific expertise with coordination. Leader routes to appropriate specialist based on context.
bmad:
  compatible_versions: ['v6.x']
  phases: [2, 3, 4]
  agents: ["leader-qa"] + ["specialist-unit", "specialist-integration", "specialist-e2e", "specialist-performance"]
  pattern: leader-specialists
---

# QA Leader

## Overview

Leader-Specialists pattern for QA domain with 4 specialized agents.

## Architecture

```
QA Leader (Router)
    ↓
    ├─→ Unit Test Specialist
    ├─→ Integration Test Specialist
    ├─→ E2E Test Specialist
    └─→ Performance Test Specialist
```

## Agents

### Leader: QA
**File**: `agents/leader-qa.md`

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
/qa
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
User: "I need unit testing work"
Leader: Analyzes → Routes to Unit Test Specialist
Specialist: Executes domain-specific work
```

### Example 2: Multi-Specialist
```
User: "I need integrated solution"
Leader: Coordinates Unit Test Specialist + Integration Test Specialist
Specialists: Execute in sequence
Leader: Integrates outputs
```

## Integration with BMAD

### Agent Customization
Add to `_bmad/_config/agents/bmm-qa.customize.yaml`:

```yaml
menu:
  - trigger: qa-specialist
    workflow: '{{project-root}}/skills/qa-leader/workflows/route-to-specialist.yaml'
    description: Route to QA specialist
```

### Workflow Phase
Default phase: **3-arch**

Adjust phase in workflow YAML as needed.

## References

- `references/routing-rules.md`: Complete routing logic
- See `bmad-method-structure.md` for BMAD integration patterns

## Resources

### agents/
- `leader-qa.md`: Main coordinator agent
- `specialist-unit.md`: Specialist in pytest, jest
- `specialist-integration.md`: Specialist in API testing
- `specialist-e2e.md`: Specialist in Playwright, Selenium
- `specialist-performance.md`: Specialist in Load testing

### workflows/
- `route-to-specialist.yaml`: Routing workflow

### references/
- `routing-rules.md`: Routing decision matrix
