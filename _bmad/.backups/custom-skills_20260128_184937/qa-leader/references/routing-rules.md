# Routing Rules

## Decision Tree

```
Request Received
    ↓
Analyze Domain/Context
    ↓
Match to Specialist
    ↓
Route & Execute
```

## Specialist Routing Matrix

| Trigger Condition | Specialist | Domain |
|-------------------|------------|--------|

| Request involves pytest, jest | Unit Test Specialist | pytest, jest |
| Request involves API testing | Integration Test Specialist | API testing |
| Request involves Playwright, Selenium | E2E Test Specialist | Playwright, Selenium |
| Request involves Load testing | Performance Test Specialist | Load testing |

## Multi-Specialist Scenarios

When request requires multiple specialists:
1. Leader coordinates sequence
2. Specialists execute in dependency order
3. Leader integrates outputs
4. Final validation by leader

## Escalation Rules

- Unknown domain → Route to leader for analysis
- Conflicting requirements → Leader mediates
- Cross-domain dependencies → Leader coordinates

## Context Preservation

Each specialist receives:
- Original request context
- Leader's analysis
- Previous specialist outputs (if any)
- Routing decision rationale

## Best Practices

- Always route through leader first
- Specialists should not route to each other directly
- Leader maintains decision log
- Document routing rationale in outputs
