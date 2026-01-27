"""
Models for BMAD Provisioner - Skills Manifest parsing
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from pathlib import Path
import yaml


@dataclass
class Specialist:
    """Specialist configuration"""
    id: str
    name: str
    domain: str
    skills: List[str]
    compliance_notes: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Specialist':
        return cls(
            id=data['id'],
            name=data['name'],
            domain=data['domain'],
            skills=data['skills'],
            compliance_notes=data.get('compliance_notes')
        )


@dataclass
class Leader:
    """Leader skill configuration"""
    name: str
    domain: str
    specialists: List[Specialist]
    phase: str = '3-arch'
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Leader':
        specialists = [Specialist.from_dict(s) for s in data['specialists']]
        return cls(
            name=data['name'],
            domain=data['domain'],
            specialists=specialists,
            phase=data.get('phase', '3-arch')
        )


@dataclass
class Customization:
    """Agent customization configuration"""
    memories: List[str] = field(default_factory=list)
    menu_additions: List[Dict] = field(default_factory=list)
    principles: List[str] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Customization':
        return cls(
            memories=data.get('memories', []),
            menu_additions=data.get('menu_additions', []),
            principles=data.get('principles', [])
        )


@dataclass
class WorkflowIntegration:
    """Workflow integration configuration"""
    phase: str
    name: str
    sequence: List[str]
    
    @classmethod
    def from_dict(cls, data: dict) -> 'WorkflowIntegration':
        return cls(
            phase=data['phase'],
            name=data['name'],
            sequence=data['sequence']
        )


@dataclass
class Project:
    """Project configuration"""
    name: str
    bmad_version: str
    root: Path
    leaders: List[Leader]
    customizations: Dict[str, Customization]
    integrations: List[WorkflowIntegration]
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Project':
        leaders = [Leader.from_dict(l) for l in data['leaders']]
        customizations = {
            name: Customization.from_dict(custom)
            for name, custom in data.get('customizations', {}).items()
        }
        integrations = [
            WorkflowIntegration.from_dict(i) 
            for i in data.get('integration', {}).get('workflows', [])
        ]
        
        return cls(
            name=data['name'],
            bmad_version=data['bmad_version'],
            root=Path(data['root']).expanduser(),
            leaders=leaders,
            customizations=customizations,
            integrations=integrations
        )


@dataclass
class SkillsManifest:
    """Complete skills manifest"""
    project: Project
    
    @classmethod
    def from_yaml(cls, yaml_path: Path) -> 'SkillsManifest':
        """Load manifest from YAML file"""
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)
        
        project = Project.from_dict(data['project'])
        return cls(project=project)
    
    def validate(self, project_root: Optional[Path] = None) -> List[str]:
        """Validate manifest configuration"""
        errors = []
        
        # Use override or manifest root
        root_to_check = project_root or self.project.root
        
        # Check project root exists
        if not root_to_check.exists():
            errors.append(f"Project root does not exist: {root_to_check}")
        
        # Check BMAD installation
        bmad_path = root_to_check / "_bmad"
        if not bmad_path.exists():
            errors.append(f"BMAD not installed at {root_to_check}")
        
        # Check leader names are unique
        leader_names = [l.name for l in self.project.leaders]
        if len(leader_names) != len(set(leader_names)):
            errors.append("Duplicate leader names found")
        
        # Check specialist IDs are unique within each leader
        for leader in self.project.leaders:
            spec_ids = [s.id for s in leader.specialists]
            if len(spec_ids) != len(set(spec_ids)):
                errors.append(f"Duplicate specialist IDs in {leader.name}")
        
        return errors
