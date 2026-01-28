# dev-leader - BMAD Leader-Specialists Skill

## Overview

This skill provides a **Leader-Specialists** pattern for dev domain expertise.

## Pattern

```
User Request
    ↓
/dev
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
- **File**: `agents/leader-dev.md`
- **Role**: Coordinate and route requests
- **Triggers**: `/dev`

### Specialist Agents

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

### Step 1: Trigger
User invokes the leader:
```
/dev
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
User: "I need React, Vue, CSS work"
Leader: Analyzes → Routes to Frontend Developer
Specialist: Executes domain-specific work
```

### Example 2: Multi-Specialist
```
User: "I need integrated solution"
Leader: Coordinates Frontend Developer + Backend Developer
Specialists: Execute in sequence
Leader: Integrates outputs
```

## Integration with BMAD

### Agent Customization
Add to `_bmad/_config/agents/bmm-dev.customize.yaml`:

```yaml
menu:
  - trigger: dev-specialist
    workflow: '{{project-root}}/skills/dev-leader/workflows/route-to-specialist.yaml'
    description: Route to dev specialist
```

### Workflow Phase
Default phase: **4-implementation**

Adjust phase in workflow YAML as needed.

## References

- `references/routing-rules.md`: Complete routing logic
- See `bmad-method-structure.md` for BMAD integration patterns

## Resources

### agents/
- `leader-dev.md`: Main coordinator agent

- `specialist-frontend.md`: Specialist in React, Vue, CSS
- `specialist-backend.md`: Specialist in FastAPI, Database
- `specialist-middleware.md`: Specialist in API Gateway, Integration

### workflows/
- `route-to-specialist.yaml`: Routing workflow

### references/
- `routing-rules.md`: Routing decision matrix
