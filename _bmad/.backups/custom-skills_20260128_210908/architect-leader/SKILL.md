# architect-leader - BMAD Leader-Specialists Skill

## Overview

This skill provides a **Leader-Specialists** pattern for architect domain expertise.

## Pattern

```
User Request
    ↓
/architect
    ↓
Leader Agent (Coordinator)
    ↓
Routes to Specialist
    ↓
Specialist Executes
    ↓
Leader Synthesizes
    ↓
Response to User
```

## Components

### Leader Agent
- **File**: `agents/leader-architect.md`
- **Role**: Coordinate and route requests
- **Triggers**: `/architect`

### Specialist Agents

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

### Step 1: Trigger
User invokes the leader:
```
/architect
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
User: "I need System Architecture, Scalability work"
Leader: Analyzes → Routes to System Architect
Specialist: Executes domain-specific work
```

### Example 2: Multi-Specialist
```
User: "I need integrated solution"
Leader: Coordinates System Architect + Integration Architect
Specialists: Execute in sequence
Leader: Integrates outputs
```

## Integration with BMAD

### Agent Customization
Add to `_bmad/_config/agents/bmm-architect.customize.yaml`:

```yaml
menu:
  - trigger: architect-specialist
    workflow: '{{project-root}}/skills/architect-leader/workflows/route-to-specialist.yaml'
    description: Route to architect specialist
```

### Workflow Phase
Default phase: **3-arch**

Adjust phase in workflow YAML as needed.

## References

- `references/routing-rules.md`: Complete routing logic
- See `bmad-method-structure.md` for BMAD integration patterns

## Resources

### agents/
- `leader-architect.md`: Main coordinator agent

- `specialist-system-arch.md`: Specialist in System Architecture, Scalability
- `specialist-integration-arch.md`: Specialist in Integration Architecture, API Design
- `specialist-risk-arch.md`: Specialist in Security & Compliance

### workflows/
- `route-to-specialist.yaml`: Routing workflow

### references/
- `routing-rules.md`: Routing decision matrix
