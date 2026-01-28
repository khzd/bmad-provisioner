# cis-leader - BMAD Leader-Specialists Skill

## Overview

This skill provides a **Leader-Specialists** pattern for cis domain expertise.

## Pattern

```
User Request
    ↓
/cis
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
- **File**: `agents/leader-cis.md`
- **Role**: Coordinate and route requests
- **Triggers**: `/cis`

### Specialist Agents

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

### Step 1: Trigger
User invokes the leader:
```
/cis
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
User: "I need Design thinking, ideation work"
Leader: Analyzes → Routes to Innovation Strategist
Specialist: Executes domain-specific work
```

### Example 2: Multi-Specialist
```
User: "I need integrated solution"
Leader: Coordinates Innovation Strategist + Research Analyst
Specialists: Execute in sequence
Leader: Integrates outputs
```

## Integration with BMAD

### Agent Customization
Add to `_bmad/_config/agents/bmm-cis.customize.yaml`:

```yaml
menu:
  - trigger: cis-specialist
    workflow: '{{project-root}}/skills/cis-leader/workflows/route-to-specialist.yaml'
    description: Route to cis specialist
```

### Workflow Phase
Default phase: **1-discovery**

Adjust phase in workflow YAML as needed.

## References

- `references/routing-rules.md`: Complete routing logic
- See `bmad-method-structure.md` for BMAD integration patterns

## Resources

### agents/
- `leader-cis.md`: Main coordinator agent

- `specialist-innovation.md`: Specialist in Design thinking, ideation
- `specialist-research.md`: Specialist in Market analysis, user research
- `specialist-storytelling.md`: Specialist in Narrative design, communication

### workflows/
- `route-to-specialist.yaml`: Routing workflow

### references/
- `routing-rules.md`: Routing decision matrix
