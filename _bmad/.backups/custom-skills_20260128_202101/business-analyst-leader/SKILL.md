# business-analyst-leader - BMAD Leader-Specialists Skill

## Overview

This skill provides a **Leader-Specialists** pattern for business-analyst domain expertise.

## Pattern

```
User Request
    ↓
/business-analyst
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
- **File**: `agents/leader-business-analyst.md`
- **Role**: Coordinate and route requests
- **Triggers**: `/business-analyst`

### Specialist Agents

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

### Step 1: Trigger
User invokes the leader:
```
/business-analyst
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
User: "I need Healthcare Domain, Medical Workflows work"
Leader: Analyzes → Routes to Healthcare Business Analyst
Specialist: Executes domain-specific work
```

### Example 2: Multi-Specialist
```
User: "I need integrated solution"
Leader: Coordinates Healthcare Business Analyst + Finance Business Analyst
Specialists: Execute in sequence
Leader: Integrates outputs
```

## Integration with BMAD

### Agent Customization
Add to `_bmad/_config/agents/bmm-business-analyst.customize.yaml`:

```yaml
menu:
  - trigger: business-analyst-specialist
    workflow: '{{project-root}}/skills/business-analyst-leader/workflows/route-to-specialist.yaml'
    description: Route to business-analyst specialist
```

### Workflow Phase
Default phase: **1-analysis**

Adjust phase in workflow YAML as needed.

## References

- `references/routing-rules.md`: Complete routing logic
- See `bmad-method-structure.md` for BMAD integration patterns

## Resources

### agents/
- `leader-business-analyst.md`: Main coordinator agent

- `specialist-healthcare-ba.md`: Specialist in Healthcare Domain, Medical Workflows
- `specialist-finance-ba.md`: Specialist in Financial Domain, Banking
- `specialist-marketing-ba.md`: Specialist in Marketing Domain, Analytics

### workflows/
- `route-to-specialist.yaml`: Routing workflow

### references/
- `routing-rules.md`: Routing decision matrix
