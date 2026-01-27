#!/usr/bin/env python3
"""
BMAD Skill Generator - Leader/Specialists Pattern
Generates BMAD-compliant skills with leader-router and domain specialists
"""

import os
import sys
import argparse
from pathlib import Path
import yaml
import csv


# Domain-specific templates
HEALTHCARE_DOMAINS = {
    'phi_keywords': ['patient', 'medical record', 'diagnosis', 'prescription', 'SSN', 'insurance', 'PHI'],
    'hipaa_checklist': [
        ('Encryption at rest', 'Data encrypted in database'),
        ('Encryption in transit', 'TLS/SSL for all communications'),
        ('Access controls', 'Role-based access implemented'),
        ('Audit logging', 'All PHI access logged'),
        ('Data minimization', 'Only necessary PHI collected'),
        ('Patient consent', 'Consent management in place'),
        ('Breach notification', 'Incident response plan ready'),
    ],
    'medical_terms': [
        ('clinical', 'diagnosis, treatment, symptoms, medical history'),
        ('patient', 'demographics, contact, insurance, consent'),
        ('compliance', 'HIPAA, PHI, audit, security, encryption'),
    ]
}

QA_DOMAINS = {
    'test_types': ['unit', 'integration', 'e2e', 'performance', 'security', 'accessibility'],
    'qa_checklist': [
        ('Code coverage', 'Minimum 80% coverage achieved'),
        ('Test automation', 'Critical paths automated'),
        ('Performance baseline', 'Response times within SLA'),
        ('Security scan', 'No critical vulnerabilities'),
        ('Accessibility audit', 'WCAG 2.1 AA compliance'),
        ('Cross-browser testing', 'All major browsers tested'),
        ('Mobile testing', 'iOS and Android tested'),
    ],
    'routing_keywords': [
        ('unit', 'component, function, class, mock, isolated'),
        ('integration', 'API, service, contract, integration'),
        ('e2e', 'user flow, scenario, end-to-end, browser'),
        ('performance', 'load, stress, benchmark, profiling, latency'),
    ]
}

CIS_DOMAINS = {
    'creative_methods': ['brainstorming', 'mind mapping', 'design thinking', 'SCAMPER', '6 thinking hats'],
    'cis_checklist': [
        ('Problem definition', 'Problem clearly articulated'),
        ('User research', 'Target audience identified'),
        ('Ideation session', 'Multiple solutions generated'),
        ('Prototype', 'Concept visualization created'),
        ('Validation', 'Feedback collected from stakeholders'),
        ('Story arc', 'Narrative structure defined'),
        ('Visual design', 'Supporting visuals prepared'),
    ],
    'routing_keywords': [
        ('innovation', 'ideation, brainstorming, creativity, design thinking'),
        ('research', 'analysis, data, competitive, user study, market'),
        ('storytelling', 'narrative, presentation, communication, content'),
    ]
}


def generate_healthcare_csvs(skill_path, domain='healthcare'):
    """Generate healthcare-specific CSV files"""
    data_path = skill_path / "data"
    
    # PHI Keywords CSV
    phi_csv = data_path / "phi-keywords.csv"
    with open(phi_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['keyword', 'category', 'risk_level'])
        for keyword in HEALTHCARE_DOMAINS['phi_keywords']:
            writer.writerow([keyword, 'PHI', 'HIGH'])
    
    # HIPAA Checklist CSV
    hipaa_csv = data_path / "hipaa-checklist.csv"
    with open(hipaa_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['requirement', 'description', 'status'])
        for req, desc in HEALTHCARE_DOMAINS['hipaa_checklist']:
            writer.writerow([req, desc, 'PENDING'])
    
    # Medical Terms Routing CSV
    terms_csv = data_path / "routing-keywords.csv"
    with open(terms_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['specialist', 'keywords'])
        for specialist, keywords in HEALTHCARE_DOMAINS['medical_terms']:
            writer.writerow([specialist, keywords])
    
    return [phi_csv, hipaa_csv, terms_csv]


def generate_qa_csvs(skill_path):
    """Generate QA-specific CSV files"""
    data_path = skill_path / "data"
    
    # Test Types CSV
    test_types_csv = data_path / "test-types.csv"
    with open(test_types_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['test_type', 'priority', 'automation_level'])
        for test_type in QA_DOMAINS['test_types']:
            writer.writerow([test_type, 'HIGH', 'AUTOMATED'])
    
    # QA Checklist CSV
    qa_checklist_csv = data_path / "qa-checklist.csv"
    with open(qa_checklist_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['requirement', 'description', 'status'])
        for req, desc in QA_DOMAINS['qa_checklist']:
            writer.writerow([req, desc, 'PENDING'])
    
    # Routing Keywords CSV
    routing_csv = data_path / "routing-keywords.csv"
    with open(routing_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['specialist', 'keywords'])
        for specialist, keywords in QA_DOMAINS['routing_keywords']:
            writer.writerow([specialist, keywords])
    
    return [test_types_csv, qa_checklist_csv, routing_csv]


def generate_cis_csvs(skill_path):
    """Generate CIS-specific CSV files"""
    data_path = skill_path / "data"
    
    # Creative Methods CSV
    methods_csv = data_path / "creative-methods.csv"
    with open(methods_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['method', 'use_case', 'specialist'])
        for method in CIS_DOMAINS['creative_methods']:
            writer.writerow([method, 'Ideation and problem-solving', 'innovation'])
    
    # CIS Checklist CSV
    cis_checklist_csv = data_path / "cis-checklist.csv"
    with open(cis_checklist_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['stage', 'description', 'status'])
        for stage, desc in CIS_DOMAINS['cis_checklist']:
            writer.writerow([stage, desc, 'PENDING'])
    
    # Routing Keywords CSV
    routing_csv = data_path / "routing-keywords.csv"
    with open(routing_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['specialist', 'keywords'])
        for specialist, keywords in CIS_DOMAINS['routing_keywords']:
            writer.writerow([specialist, keywords])
    
    return [methods_csv, cis_checklist_csv, routing_csv]


def create_directory_structure(base_path, skill_name, include_data=False):
    """Create the base directory structure for the skill"""
    directories = [
        f"{skill_name}",
        f"{skill_name}/agents",
        f"{skill_name}/workflows",
        f"{skill_name}/references",
    ]
    
    if include_data:
        directories.append(f"{skill_name}/data")
    
    for directory in directories:
        path = Path(base_path) / directory
        path.mkdir(parents=True, exist_ok=True)
    
    return Path(base_path) / skill_name


def generate_leader_agent(skill_path, leader_name, specialists, domain=None):
    """Generate leader/router agent"""
    specialist_list = "\n".join([f"- **{s['name']}**: {s['description']}" for s in specialists])
    specialist_routing = "\n".join([
        f"  - {s['name']}: {s['trigger_conditions']}" 
        for s in specialists
    ])
    
    # Domain-specific sections
    domain_section = ""
    if domain == 'healthcare':
        domain_section = """

## Healthcare-Specific Responsibilities
- **HIPAA Compliance**: Ensure all routing respects PHI handling rules
- **Audit Trail**: Log all specialist routing decisions
- **Patient Safety**: Prioritize clinical specialists for medical queries
- **Data Minimization**: Route only necessary context to specialists

## PHI Handling
- Check for PHI in requests before routing
- Apply encryption for sensitive data
- Log access for audit compliance
- Consult `data/phi-keywords.csv` for PHI detection

## Compliance Integration
- Use `data/hipaa-checklist.csv` for validation
- Reference `data/routing-keywords.csv` for medical term routing
"""
    
    content = f"""# {leader_name.title()} - Leader Agent

## Role
Coordinate and route requests to specialized agents based on domain expertise.

## Responsibilities
- Analyze incoming requests
- Determine appropriate specialist
- Route to correct domain expert
- Coordinate cross-domain work
{domain_section}

## Available Specialists
{specialist_list}

## Routing Logic

### When to Route
{specialist_routing}

### Routing Process
1. Analyze request context
2. Identify primary domain
3. Check specialist availability
4. Route to most appropriate specialist
5. Monitor and coordinate if multiple specialists needed

## Menu

Load specialists:
"""
    
    # Build specialists menu
    for s in specialists:
        content += f"\n- `/{s['id']}` - Load {s['name']}"
    
    content += """

## Workflow Integration

This leader agent uses the routing workflow:
```
workflows/route-to-specialist.yaml
```

## Communication Style
- Clear and directive
- Domain-aware
- Efficient handoffs
- Maintains context across specialists

## Principles
- Route to most specialized agent available
- Prefer specialist over generalist
- Coordinate multi-domain work
- Maintain traceability of decisions
"""
    
    agent_path = skill_path / "agents" / f"leader-{leader_name}.md"
    agent_path.write_text(content)
    return agent_path


def generate_specialist_agent(skill_path, specialist, domain=None):
    """Generate specialist agent"""
    
    # Domain-specific compliance sections
    compliance_section = ""
    if domain == 'healthcare':
        compliance_section = f"""

## Healthcare Compliance

### HIPAA Requirements
- Handle PHI according to HIPAA standards
- Maintain audit logs for all PHI access
- Apply encryption for data at rest and in transit
- Implement access controls and authentication

### Specialist-Specific Compliance
{specialist.get('compliance_notes', '- Follow domain-specific healthcare regulations')}

### PHI Handling
- Identify PHI using `data/phi-keywords.csv`
- Minimize PHI exposure
- Obtain patient consent when required
- Report any PHI incidents to leader

### Audit Trail
Log all actions involving:
- Patient data access
- Clinical decisions
- Prescription information
- Medical records handling
"""
    
    content = f"""# {specialist['name']} - Specialist Agent

## Role
{specialist['description']}

## Domain Expertise
{specialist['domain']}

## Specialized Skills
"""
    
    # Build skills list
    for skill in specialist['skills']:
        content += f"\n- {skill}"
    
    content += """

## When to Use This Specialist
{specialist['trigger_conditions']}
{compliance_section}

## Communication Style
{specialist.get('communication_style', 'Professional, domain-focused, detail-oriented')}

## Principles
"""
    
    # Build principles list
    for principle in specialist.get('principles', ['Maintain domain best practices', 'Ensure quality and consistency']):
        content += f"\n- {principle}"
    
    content += """

## Workflow Integration
Works with leader agent: `leader-{specialist['leader_name']}`

## Handoff Protocol
- Receive context from leader
- Execute specialized work
- Report back to leader with results
- Flag cross-domain dependencies
- Flag cross-domain dependencies
"""
    
    agent_path = skill_path / "agents" / f"specialist-{specialist['id']}.md"
    agent_path.write_text(content)
    return agent_path


def generate_routing_workflow(skill_path, leader_name, specialists):
    """Generate YAML workflow for routing"""
    specialist_steps = []
    for spec in specialists:
        specialist_steps.append({
            'agent': f"specialist-{spec['id']}",
            'action': f"execute-{spec['id']}-work",
            'condition': spec['trigger_conditions'],
            'dependencies': [{'file': '{project-root}/.docs/requirements.md'}],
            'outputs': [f".docs/{spec['id']}-output.md"]
        })
    
    workflow = {
        'name': f'route-to-specialist-{leader_name}',
        'description': f'Route requests to appropriate {leader_name} specialist',
        'phase': '3-arch',  # Default, adjust as needed
        'sequence': [
            {
                'agent': f'leader-{leader_name}',
                'action': 'analyze-request',
                'dependencies': [{'file': '{project-root}/.docs/requirements.md'}],
                'outputs': ['.docs/routing-decision.md']
            },
            {
                'agent': f'leader-{leader_name}',
                'action': 'route-to-specialist',
                'dependencies': [{'file': '.docs/routing-decision.md'}],
                'handoff': {
                    'to': 'specialist',
                    'routing': [
                        {'condition': spec['trigger_conditions'], 'agent': f"specialist-{spec['id']}"} 
                        for spec in specialists
                    ]
                }
            }
        ] + specialist_steps
    }
    
    workflow_path = skill_path / "workflows" / f"route-to-specialist.yaml"
    with open(workflow_path, 'w') as f:
        yaml.dump(workflow, f, default_flow_style=False, sort_keys=False)
    
    return workflow_path


def generate_routing_rules(skill_path, specialists):
    """Generate routing rules documentation"""
    content = f"""# Routing Rules

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
"""
    
    # Build routing table rows
    for s in specialists:
        content += f"\n| {s['trigger_conditions']} | {s['name']} | {s['domain']} |"
    
    content += """

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
"""
    
    rules_path = skill_path / "references" / "routing-rules.md"
    rules_path.write_text(content)
    return rules_path


def generate_skill_md(skill_path, skill_name, leader_name, specialists, bmad_config):
    """Generate main SKILL.md"""
    specialist_list = ", ".join([s['name'] for s in specialists])
    
    content = f"""---
name: {skill_name}
description: {leader_name.title()} leader with specialized agents: {specialist_list}. Use when needing domain-specific expertise with coordination. Leader routes to appropriate specialist based on context.
bmad:
  compatible_versions: {bmad_config.get('compatible_versions', ['v6.x'])}
  phases: {bmad_config.get('phases', [2, 3, 4])}
  agents: ["leader-{leader_name}"] + [{', '.join([f'"specialist-{s["id"]}"' for s in specialists])}]
  pattern: leader-specialists
---

# {skill_name.replace('-', ' ').title()}

## Overview

Leader-Specialists pattern for {leader_name} domain with {len(specialists)} specialized agents.

## Architecture

```
{leader_name.title()} Leader (Router)
    ↓
    ├─→ {specialists[0]['name']}
"""
    
    # Build tree structure for middle specialists
    for s in specialists[1:-1]:
        content += f"\n    ├─→ {s['name']}"
    
    content += """
    └─→ {specialists[-1]['name']}
```

## Agents

### Leader: {leader_name}
**File**: `agents/leader-{leader_name}.md`

Coordinates routing to specialists based on domain analysis.

### Specialists

"""
    
    # Build specialists list with details
    for i, s in enumerate(specialists):
        content += f"\n**{i+1}. {s['name']}**  \n**File**: `agents/specialist-{s['id']}.md`  \n**Domain**: {s['domain']}\n"
    
    content += """

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
"""
    
    # Add specialist resources (can't use join in f-string with backslash)
    for s in specialists:
        content += f"\n- `specialist-{s['id']}.md`: {s['description']}"
    
    content += """

### workflows/
- `route-to-specialist.yaml`: Routing workflow

### references/
- `routing-rules.md`: Routing decision matrix
"""
    
    skill_md_path = skill_path / "SKILL.md"
    skill_md_path.write_text(content)
    return skill_md_path


def main():
    parser = argparse.ArgumentParser(
        description='Generate BMAD Leader-Specialists skill structure',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create Dev Leader with 3 specialists
  python init_bmad_skill.py dev-leader --output ./skills \\
    --specialists frontend:"Front-end development":"React, Vue, styling" \\
                  middleware:"Middleware/API":"REST, GraphQL, integration" \\
                  backend:"Back-end development":"Database, services, logic"
  
  # Create Architect Leader for LoB
  python init_bmad_skill.py architect-leader --output ./skills \\
    --specialists healthcare:"Healthcare architecture":"HIPAA, PHI, medical" \\
                  finance:"Financial architecture":"PCI-DSS, banking, compliance" \\
                  retail:"Retail architecture":"E-commerce, inventory, POS"
        """
    )
    
    parser.add_argument('skill_name', help='Name of the skill (e.g., dev-leader, architect-leader)')
    parser.add_argument('--output', '-o', default='.', help='Output directory (default: current directory)')
    parser.add_argument('--leader', '-l', help='Leader name (default: extracted from skill_name)')
    parser.add_argument(
        '--specialists', '-s', 
        nargs='+', 
        required=True,
        help='Specialists in format: id:name:domain:skills (skills comma-separated)'
    )
    parser.add_argument('--phase', default='3-arch', help='Default BMAD phase (default: 3-arch)')
    parser.add_argument('--bmad-versions', default='v6.x', help='Compatible BMAD versions (default: v6.x)')
    parser.add_argument(
        '--domain', '-d',
        choices=['generic', 'healthcare', 'qa', 'cis'],
        default='generic',
        help='Domain specialization (adds domain-specific templates and CSV files)'
    )
    
    args = parser.parse_args()
    
    # Parse leader name
    leader_name = args.leader if args.leader else args.skill_name.replace('-leader', '')
    
    # Parse specialists
    specialists = []
    for i, spec_str in enumerate(args.specialists):
        parts = spec_str.split(':')
        if len(parts) < 3:
            print(f"Error: Specialist format should be 'id:name:domain:skills'")
            print(f"Got: {spec_str}")
            sys.exit(1)
        
        spec_id = parts[0]
        spec_name = parts[1]
        spec_domain = parts[2]
        spec_skills = parts[3].split(',') if len(parts) > 3 else [spec_domain]
        
        specialists.append({
            'id': spec_id,
            'name': spec_name,
            'domain': spec_domain,
            'description': f"Specialist in {spec_domain}",
            'skills': spec_skills,
            'trigger_conditions': f"Request involves {spec_domain}",
            'leader_name': leader_name,
            'communication_style': 'Professional, domain-focused',
            'principles': [
                f'Follow {spec_domain} best practices',
                'Ensure domain-specific quality',
                'Maintain consistency with leader direction'
            ]
        })
    
    # BMAD configuration
    bmad_config = {
        'compatible_versions': [args.bmad_versions],
        'phases': [2, 3, 4],
        'default_phase': args.phase
    }
    
    # Create structure
    print(f"🚀 Generating BMAD skill: {args.skill_name}")
    print(f"   Leader: {leader_name}")
    print(f"   Specialists: {len(specialists)}")
    print(f"   Domain: {args.domain}")
    
    include_data = args.domain != 'generic'
    skill_path = create_directory_structure(args.output, args.skill_name, include_data=include_data)
    print(f"✅ Created directory structure at {skill_path}")
    
    # Generate domain-specific CSV files
    if args.domain == 'healthcare':
        csv_files = generate_healthcare_csvs(skill_path, args.domain)
        print(f"✅ Generated {len(csv_files)} healthcare CSV files")
        for csv_file in csv_files:
            print(f"   - {csv_file.name}")
    elif args.domain == 'qa':
        csv_files = generate_qa_csvs(skill_path)
        print(f"✅ Generated {len(csv_files)} QA CSV files")
        for csv_file in csv_files:
            print(f"   - {csv_file.name}")
    elif args.domain == 'cis':
        csv_files = generate_cis_csvs(skill_path)
        print(f"✅ Generated {len(csv_files)} CIS CSV files")
        for csv_file in csv_files:
            print(f"   - {csv_file.name}")
    
    # Generate files
    leader_path = generate_leader_agent(skill_path, leader_name, specialists, domain=args.domain)
    print(f"✅ Generated leader agent: {leader_path.name}")
    
    for spec in specialists:
        spec_path = generate_specialist_agent(skill_path, spec, domain=args.domain)
        print(f"✅ Generated specialist: {spec_path.name}")
    
    workflow_path = generate_routing_workflow(skill_path, leader_name, specialists)
    print(f"✅ Generated routing workflow: {workflow_path.name}")
    
    rules_path = generate_routing_rules(skill_path, specialists)
    print(f"✅ Generated routing rules: {rules_path.name}")
    
    skill_md_path = generate_skill_md(skill_path, args.skill_name, leader_name, specialists, bmad_config)
    print(f"✅ Generated SKILL.md: {skill_md_path.name}")
    
    print(f"\n✅ Skill '{args.skill_name}' generated successfully at {skill_path}")
    print(f"\nNext steps:")
    print(f"1. Review and customize agents in {skill_path}/agents/")
    print(f"2. Adjust routing workflow in {skill_path}/workflows/")
    if include_data:
        print(f"3. Review CSV files in {skill_path}/data/")
        print(f"4. Test with: /{leader_name}")
    else:
        print(f"3. Test with: /{leader_name}")
    print(f"4. Package with: scripts/package_skill.py {skill_path}")


if __name__ == '__main__':
    main()