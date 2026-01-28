# Routing Rules

## Specialist Routing Matrix

| Trigger Conditions | Specialist | Domain |
|--------------------|------------|--------|
| Request involves Healthcare Domain, Medical Workflows | Healthcare Business Analyst | Healthcare Domain, Medical Workflows |
| Request involves Financial Domain, Banking | Finance Business Analyst | Financial Domain, Banking |
| Request involves Marketing Domain, Analytics | Marketing Business Analyst | Marketing Domain, Analytics |


## Routing Decision Process

1. **Analyze Request**: Leader examines request content and context
2. **Match Keywords**: Compare against specialist domains and trigger conditions
3. **Select Specialist**: Choose most appropriate specialist
4. **Route Request**: Load specialist agent and provide context
5. **Monitor Execution**: Track specialist work
6. **Synthesize Output**: Review and format final response

## Multi-Specialist Coordination

When a request requires multiple specialists:

1. Leader identifies all required specialists
2. Determines execution order
3. Routes to first specialist
4. Passes outputs between specialists
5. Synthesizes final integrated response

## Escalation Rules

- **Unknown Domain**: Leader handles directly or requests clarification
- **Cross-Domain Complexity**: Leader coordinates multiple specialists
- **Specialist Unavailable**: Leader provides general guidance or suggests alternative
