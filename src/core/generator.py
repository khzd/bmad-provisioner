"""
Generator - Integrate with bmad-skill-generator to actually provision skills
"""

import subprocess
from pathlib import Path
from typing import List, Dict, Optional
import shutil
from .csv_merger import merge_csv_safely

class SkillGenerator:
    """Generate skills using bmad-skill-generator"""
    
    def __init__(self, generator_script: Path, project_root: Path):
        self.generator_script = generator_script
        self.project_root = project_root
        self.output_dir = project_root / "_bmad" / "custom-skills"
    
    def ensure_output_dir(self):
        """Ensure custom-skills directory exists"""
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_leader(self, leader_config, domain: str = 'generic') -> bool:
        """Generate a single leader skill"""
        print(f"🔨 Generating {leader_config.name}...")
        
        # Build specialists arguments
        specialists_args = []
        for spec in leader_config.specialists:
            # Format: id:name:domain:skills
            skills_str = ",".join(spec.skills)
            spec_arg = f"{spec.id}:{spec.name}:{spec.domain}:{skills_str}"
            specialists_args.append(spec_arg)
        
        # Build command
        cmd = [
            'python3',
            str(self.generator_script),
            leader_config.name,
            '--output', str(self.output_dir),
            '--domain', domain,
            '--phase', leader_config.phase,
            '--specialists'
        ] + specialists_args
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            print(f"✅ Generated {leader_config.name}")
            if result.stdout:
                # Show key output lines
                for line in result.stdout.split('\n'):
                    if '✅' in line or '📦' in line:
                        print(f"   {line}")
            
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to generate {leader_config.name}")
            print(f"   Error: {e.stderr}")
            return False
    
    def generate_customize_file(self, leader_name: str, customization) -> bool:
        """Generate _config/agents/*.customize.yaml file"""
        print(f"🔧 Creating customize file for {leader_name}...")
        
        config_dir = self.project_root / "_bmad" / "_config" / "agents"
        config_dir.mkdir(parents=True, exist_ok=True)
        
        customize_file = config_dir / f"custom-{leader_name}.customize.yaml"
        
        # Build YAML content
        content = []
        
        if customization.memories:
            content.append("memories:")
            for memory in customization.memories:
                content.append(f'  - "{memory}"')
            content.append("")
        
        if customization.principles:
            content.append("principles:")
            for principle in customization.principles:
                content.append(f'  - "{principle}"')
            content.append("")
        
        if customization.menu_additions:
            content.append("menu:")
            for menu_item in customization.menu_additions:
                content.append(f"  - trigger: {menu_item['trigger']}")
                content.append(f"    workflow: '{menu_item['workflow']}'")
                content.append(f"    description: \"{menu_item['description']}\"")
            content.append("")
        
        if content:
            customize_file.write_text('\n'.join(content))
            print(f"✅ Created {customize_file.name}")
            return True
        
        return False
    #####
    def generate_csv_with_merge(
        self,
        csv_path: Path,
        headers: List[str],
        rows: List[List[str]],
        verbose: bool = True
    ) -> bool:
        """
        Generate CSV with smart merging to preserve custom data
        
        Args:
            csv_path: Path to CSV file
            headers: CSV headers
            rows: CSV rows
            verbose: Print merge statistics
        
        Returns:
            True if successful
        """
        try:
            from .csv_merger import merge_csv_safely
            
            result = merge_csv_safely(
                csv_path=csv_path,
                new_rows=rows,
                headers=headers,
                primary_key_column=0,
                verbose=verbose
            )
            
            if verbose and (result.custom_rows > 0 or result.preserved_rows > 0):
                print(f"   🔄 Smart merge preserved {result.custom_rows} custom rows + {result.preserved_rows} user modifications")
            
            return True
        except Exception as e:
            print(f"   ⚠️  CSV merge failed: {e}")
            # Fallback: write directly
            csv_path.parent.mkdir(parents=True, exist_ok=True)
            import csv
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(rows)
            return True    
    ######""
    def generate_all(self, manifest) -> Dict[str, bool]:
        """Generate all leaders from manifest"""
        self.ensure_output_dir()
        
        results = {}
        
        for leader in manifest.project.leaders:
            # Generate leader skill
            success = self.generate_leader(leader, leader.domain)
            results[leader.name] = success
            
            if not success:
                continue
            
            # Generate customize file if customizations exist
            if leader.name in manifest.project.customizations:
                customization = manifest.project.customizations[leader.name]
                self.generate_customize_file(leader.name, customization)
        
        return results


class SkillBackup:
    """Backup existing skills before provisioning"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.backup_dir = project_root / "_bmad" / ".backups"
    
    def backup_skills(self) -> Optional[Path]:
        """Backup existing custom-skills directory"""
        custom_skills = self.project_root / "_bmad" / "custom-skills"
        
        if not custom_skills.exists():
            return None
        
        # Create backup with timestamp
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self.backup_dir / f"custom-skills_{timestamp}"
        
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"💾 Backing up existing skills to {backup_path.name}...")
        shutil.copytree(custom_skills, backup_path)
        print(f"✅ Backup created")
        
        return backup_path
    
    def restore_backup(self, backup_path: Path) -> bool:
        """Restore from backup"""
        if not backup_path.exists():
            print(f"❌ Backup not found: {backup_path}")
            return False
        
        custom_skills = self.project_root / "_bmad" / "custom-skills"
        
        # Remove current
        if custom_skills.exists():
            shutil.rmtree(custom_skills)
        
        # Restore backup
        shutil.copytree(backup_path, custom_skills)
        print(f"✅ Restored from {backup_path.name}")
        
        return True
