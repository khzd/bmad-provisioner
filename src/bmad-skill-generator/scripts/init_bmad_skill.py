#!/usr/bin/env python3
"""
BMAD Skill Generator - Leader/Specialists Pattern
Generates BMAD-compliant skills with leader-router and domain specialists
v0.3 - Smart CSV Merging support
"""

import os
import sys
import argparse
from pathlib import Path
import yaml
import csv

# Add parent directory to path for core imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from core.csv_merger import merge_csv_safely
    HAS_MERGER = True
except ImportError:
    HAS_MERGER = False


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


def write_csv_smart(csv_path, headers, rows, verbose=True):
    """
    Write CSV with smart merging if available
    
    Falls back to direct write if merger not available
    """
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    
    if HAS_MERGER:
        # Use smart merger to preserve custom data
        result = merge_csv_safely(
            csv_path=csv_path,
            new_rows=rows,
            headers=headers,
            primary_key_column=0,
            verbose=verbose
        )
        
        if verbose and (result.custom_rows > 0 or result.preserved_rows > 0):
            print(f"      🔄 Preserved {result.custom_rows} custom + {result.preserved_rows} modified rows")
    else:
        # Fallback: direct write (overwrites existing)
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)


def generate_healthcare_csvs(skill_path, domain='healthcare'):
    """Generate healthcare-specific CSV files with smart merging"""
    data_path = skill_path / "data"
    
    # PHI Keywords CSV
    phi_csv = data_path / "phi-keywords.csv"
    phi_rows = [[keyword, 'PHI', 'HIGH'] for keyword in HEALTHCARE_DOMAINS['phi_keywords']]
    write_csv_smart(phi_csv, ['keyword', 'category', 'risk_level'], phi_rows, verbose=True)
    
    # HIPAA Checklist CSV
    hipaa_csv = data_path / "hipaa-checklist.csv"
    hipaa_rows = [[req, desc, 'PENDING'] for req, desc in HEALTHCARE_DOMAINS['hipaa_checklist']]
    write_csv_smart(hipaa_csv, ['requirement', 'description', 'status'], hipaa_rows, verbose=True)
    
    # Medical Terms Routing CSV
    terms_csv = data_path / "routing-keywords.csv"
    terms_rows = [[specialist, keywords] for specialist, keywords in HEALTHCARE_DOMAINS['medical_terms']]
    write_csv_smart(terms_csv, ['specialist', 'keywords'], terms_rows, verbose=True)
    
    return [phi_csv, hipaa_csv, terms_csv]


def generate_qa_csvs(skill_path):
    """Generate QA-specific CSV files with smart merging"""
    data_path = skill_path / "data"
    
    # Test Types CSV
    test_types_csv = data_path / "test-types.csv"
    test_rows = [[test_type, 'HIGH', 'AUTOMATED'] for test_type in QA_DOMAINS['test_types']]
    write_csv_smart(test_types_csv, ['test_type', 'priority', 'automation_level'], test_rows, verbose=True)
    
    # QA Checklist CSV
    qa_checklist_csv = data_path / "qa-checklist.csv"
    qa_rows = [[req, desc, 'PENDING'] for req, desc in QA_DOMAINS['qa_checklist']]
    write_csv_smart(qa_checklist_csv, ['requirement', 'description', 'status'], qa_rows, verbose=True)
    
    # Routing Keywords CSV
    routing_csv = data_path / "routing-keywords.csv"
    routing_rows = [[specialist, keywords] for specialist, keywords in QA_DOMAINS['routing_keywords']]
    write_csv_smart(routing_csv, ['specialist', 'keywords'], routing_rows, verbose=True)
    
    return [test_types_csv, qa_checklist_csv, routing_csv]


def generate_cis_csvs(skill_path):
    """Generate CIS-specific CSV files with smart merging"""
    data_path = skill_path / "data"
    
    # Creative Methods CSV
    methods_csv = data_path / "creative-methods.csv"
    methods_rows = [[method, 'Ideation and problem-solving', 'innovation'] for method in CIS_DOMAINS['creative_methods']]
    write_csv_smart(methods_csv, ['method', 'use_case', 'specialist'], methods_rows, verbose=True)

    # CIS Checklist CSV
    cis_checklist_csv = data_path / "cis-checklist.csv"
    cis_rows = [[stage, desc, 'PENDING'] for stage, desc in CIS_DOMAINS['cis_checklist']]
    write_csv_smart(cis_checklist_csv, ['stage', 'description', 'status'], cis_rows, verbose=True)
    
    # Routing Keywords CSV
    routing_csv = data_path / "routing-keywords.csv"
    routing_rows = [[specialist, keywords] for specialist, keywords in CIS_DOMAINS['routing_keywords']]
    write_csv_smart(routing_csv, ['specialist', 'keywords'], routing_rows, verbose=True)
    
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
- Route to appropriate specialist based on request content
- Coordinate multi-specialist workflows when needed
- Ensure consistent communication between specialists
- Aggregate and synthesize specialist outputs

## Available Specialists
{specialist_list}

## Routing Strategy
{specialist_routing}
{domain_section}

## Communication Style
- **Tone**: Professional, helpful, collaborative
- **Approach**: Analyze first, route smartly, coordinate effectively
- **Language**: Clear technical communication

## Principles
- Route to the most appropriate specialist
- Provide specialists with complete context
- Coordinate complex tasks across multiple specialists
- Maintain consistency across specialist interactions
- Always validate specialist outputs before final response
"""
    
    leader_path = skill_path / "agents" / f"leader-{leader_name}.md"
    leader_path.write_text(content)
    return leader_path


def generate_specialist_agent(skill_path, specialist, domain=None):
    """Generate specialist agent"""
    specialist_id = specialist['id']
    specialist_name = specialist['name']
    specialist_domain = specialist['domain']
    specialist_description = specialist['description']
    specialist_skills = specialist['skills']
    leader_name = specialist['leader_name']
    
    skills_list = "\n".join([f"- {skill}" for skill in specialist_skills])
    
    # Domain-specific sections
    domain_section = ""
    if domain == 'healthcare':
        domain_section = """

## Healthcare-Specific Guidelines
- **HIPAA Compliance**: All implementations must respect PHI handling rules
- **Audit Logging**: Log all access to sensitive healthcare data
- **Data Encryption**: Ensure PHI is encrypted at rest and in transit
- **Patient Safety**: Prioritize patient safety in all technical decisions

## Reference Data
- Check `data/phi-keywords.csv` for PHI identification
- Consult `data/hipaa-checklist.csv` for compliance validation
"""
    
    content = f"""# {specialist_name} - Specialist Agent

## Role
{specialist_description}

## Domain Expertise
{specialist_domain}

## Core Skills
{skills_list}

## Responsibilities
- Execute domain-specific work assigned by {leader_name}
- Apply best practices for {specialist_domain}
- Provide detailed technical guidance
- Validate work against domain standards
- Collaborate with other specialists when needed
{domain_section}

## Communication Style
- **Tone**: {specialist.get('communication_style', 'Professional, detail-oriented')}
- **Approach**: Deep technical expertise in {specialist_domain}
- **Language**: Domain-specific terminology with clear explanations

## Principles
"""
    
    for principle in specialist.get('principles', ['Maintain domain best practices', 'Ensure quality and consistency']):
        content += f"\n- {principle}"
    
    content += f"""

## Collaboration
- Report to: **{leader_name}**
- Works with: Other specialists as coordinated by {leader_name}
- Escalate: Complex cross-domain issues to {leader_name}
"""
    
    spec_path = skill_path / "agents" / f"specialist-{specialist_id}.md"
    spec_path.write_text(content)
    return spec_path


def generate_routing_workflow(skill_path, leader_name, specialists):
    """Generate routing workflow YAML"""
    specialist_ids = [s['id'] for s in specialists]
    
    workflow = {
        'name': 'route-to-specialist',
        'description': f'Route requests to appropriate specialist under {leader_name}',
        'trigger': f'/{leader_name}',
        'steps': [
            {
                'name': 'analyze-request',
                'agent': f'leader-{leader_name}',
                'action': 'Analyze request and determine appropriate specialist',
                'output': 'routing_decision'
            },
            {
                'name': 'route-to-specialist',
                'agent': 'specialist-{{routing_decision.specialist_id}}',
                'action': 'Execute specialist work',
                'input': '{{request}}',
                'output': 'specialist_result'
            },
            {
                'name': 'synthesize-response',
                'agent': f'leader-{leader_name}',
                'action': 'Review and synthesize specialist output',
                'input': '{{specialist_result}}',
                'output': 'final_response'
            }
        ]
    }
    
    workflow_path = skill_path / "workflows" / "route-to-specialist.yaml"
    with open(workflow_path, 'w') as f:
        yaml.dump(workflow, f, default_flow_style=False, sort_keys=False)
    
    return workflow_path


def generate_routing_rules(skill_path, specialists):
    """Generate routing rules documentation"""
    
    content = """# Routing Rules

## Specialist Routing Matrix

| Trigger Conditions | Specialist | Domain |
|--------------------|------------|--------|
"""
    
    for s in specialists:
        content += f"| {s['trigger_conditions']} | {s['name']} | {s['domain']} |\n"
    
    content += """

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
"""
    
    rules_path = skill_path / "references" / "routing-rules.md"
    rules_path.write_text(content)
    return rules_path


def generate_skill_md(skill_path, skill_name, leader_name, specialists, bmad_config):
    """Generate SKILL.md documentation"""
    
    content = f"""# {skill_name} - BMAD Leader-Specialists Skill

## Overview

This skill provides a **Leader-Specialists** pattern for {leader_name} domain expertise.

## Pattern

```
User Request
    ↓
/{leader_name}
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
- **File**: `agents/leader-{leader_name}.md`
- **Role**: Coordinate and route requests
- **Triggers**: `/{leader_name}`

### Specialist Agents
"""
    
    for i, s in enumerate(specialists):
        content += f"\n**{i+1}. {s['name']}**  \n**File**: `agents/specialist-{s['id']}.md`  \n**Domain**: {s['domain']}\n"
    
    content += f"""

## Workflow

### Step 1: Trigger
User invokes the leader:
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
    workflow: '{{{{project-root}}}}/skills/{skill_name}/workflows/route-to-specialist.yaml'
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
    if HAS_MERGER:
        print(f"   ✅ Smart CSV Merging enabled")
    else:
        print(f"   ⚠️  Smart CSV Merging not available (will overwrite CSV files)")
    
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