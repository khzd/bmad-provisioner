#!/usr/bin/env python3
"""
BMAD Provisioner - Infrastructure as Code for BMAD Custom Skills

Manage custom BMAD skills across projects with declarative configuration.
Survives BMAD version updates by re-provisioning from manifest.
"""

import sys
import argparse
from pathlib import Path
from typing import Optional

# Add parent dir to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from models.manifest import SkillsManifest
from core.analyzer import GapAnalyzer
from core.generator import SkillGenerator, SkillBackup


class BMADProvisioner:
    """Main provisioner orchestrator"""
    
    def __init__(self, manifest_path: Path, project_root: Optional[Path] = None):
        self.manifest_path = manifest_path
        self.manifest = SkillsManifest.from_yaml(manifest_path)
        
        # Use project root from manifest or override
        self.project_root = project_root or self.manifest.project.root
        self.analyzer = GapAnalyzer(self.project_root)
    
    def validate_manifest(self) -> bool:
        """Validate manifest configuration"""
        print("🔍 Validating manifest...")
        errors = self.manifest.validate(self.project_root)
        
        if errors:
            print("❌ Manifest validation failed:")
            for error in errors:
                print(f"   - {error}")
            return False
        
        print("✅ Manifest is valid")
        return True
    
    def analyze(self) -> bool:
        """Perform gap analysis"""
        print(f"📊 Analyzing project: {self.manifest.project.name}")
        print(f"   Root: {self.project_root}")
        print()
        
        report = self.analyzer.analyze(self.manifest)
        print(report.summary())
        
        return True
    
    def provision(self, dry_run: bool = False, generator_script: Optional[Path] = None) -> bool:
        """Provision skills to project"""
        if dry_run:
            print("🔍 Dry run mode - no changes will be made")
        
        print("🚀 Provisioning custom skills...")
        
        # First, analyze
        report = self.analyzer.analyze(self.manifest)
        
        # Check if safe to provision
        if not report.bmad_version:
            print("⚠️  Warning: BMAD version not detected")
            if not dry_run:
                response = input("Continue anyway? (y/N): ")
                if response.lower() != 'y':
                    print("❌ Provisioning cancelled")
                    return False
        
        print(f"\n📦 Leaders to provision: {len(self.manifest.project.leaders)}")
        for leader in self.manifest.project.leaders:
            print(f"   - {leader.name} ({leader.domain}): {len(leader.specialists)} specialists")
        
        if dry_run:
            print("\n✅ Dry run complete - no changes made")
            return True
        
        # Find generator script
        if generator_script is None:
            # Auto-detect: look for bmad-skill-generator in common locations
            search_paths = [
                Path.cwd() / "../bmad-skill-generator/scripts/init_bmad_skill.py",
                Path.home() / "bmad-tools/bmad-skill-generator/scripts/init_bmad_skill.py",
                Path.cwd() / "../../bmad-skill-generator/scripts/init_bmad_skill.py",
            ]
            
            for path in search_paths:
                if path.exists():
                    generator_script = path
                    break
            
            if generator_script is None:
                print("❌ Could not find bmad-skill-generator script")
                print("   Use --generator-script to specify path")
                return False
        
        if not generator_script.exists():
            print(f"❌ Generator script not found: {generator_script}")
            return False
        
        print(f"\n🔧 Using generator: {generator_script}")
        
        # Backup existing skills
        backup = SkillBackup(self.project_root)
        backup_path = backup.backup_skills()
        if backup_path:
            print(f"   Backup saved: {backup_path.name}")
        
        # Generate skills
        generator = SkillGenerator(generator_script, self.project_root)
        
        print("\n📦 Generating skills...")
        results = generator.generate_all(self.manifest)
        
        # Summary
        print("\n" + "="*50)
        print("📊 Provisioning Summary")
        print("="*50)
        
        success_count = sum(1 for r in results.values() if r)
        fail_count = len(results) - success_count
        
        for leader_name, success in results.items():
            status = "✅" if success else "❌"
            print(f"{status} {leader_name}")
        
        print(f"\nTotal: {success_count} success, {fail_count} failed")
        
        if fail_count > 0:
            print("\n⚠️  Some skills failed to provision")
            if backup_path:
                response = input("Restore from backup? (y/N): ")
                if response.lower() == 'y':
                    backup.restore_backup(backup_path)
            return False
        
        print("\n✅ All skills provisioned successfully!")
        print(f"\n📁 Custom skills location:")
        print(f"   {self.project_root / '_bmad/custom-skills'}")
        
        return True
    
    def diff(self) -> bool:
        """Show what would change"""
        print("🔍 Computing differences...")
        
        report = self.analyzer.analyze(self.manifest)
        
        # Show what would be created/updated
        print("\nChanges that would be made:")
        
        for leader_status in report.leaders:
            if not leader_status.installed:
                print(f"\n📦 CREATE: {leader_status.name}")
                print(f"   - agents/leader-{leader_status.name}.md")
                print(f"   - workflows/route-to-specialist.yaml")
                for file_status in leader_status.files:
                    print(f"   - {file_status.path.name}")
            elif leader_status.needs_update:
                print(f"\n📝 UPDATE: {leader_status.name}")
                for file_status in leader_status.files:
                    if file_status.change_type.value in ['missing', 'outdated']:
                        print(f"   - {file_status.path.name}: {file_status.details}")
        
        return True


def main():
    parser = argparse.ArgumentParser(
        description='BMAD Provisioner - Infrastructure as Code for BMAD Skills',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze current state
  bmad-provisioner.py --config skills-manifest.yaml --mode analyze
  
  # Show what would change
  bmad-provisioner.py --config skills-manifest.yaml --mode diff
  
  # Provision (dry run)
  bmad-provisioner.py --config skills-manifest.yaml --mode provision --dry-run
  
  # Provision for real
  bmad-provisioner.py --config skills-manifest.yaml --mode provision
  
  # Override project root
  bmad-provisioner.py --config skills-manifest.yaml --project-root ~/my-project --mode analyze
        """
    )
    
    parser.add_argument(
        '--config', '-c',
        type=Path,
        required=True,
        help='Path to skills-manifest.yaml'
    )
    
    parser.add_argument(
        '--generator-script', '-g',
        type=Path,
        help='Path to bmad-skill-generator init_bmad_skill.py (default: auto-detect)'
    )
    
    parser.add_argument(
        '--project-root', '-p',
        type=Path,
        help='Override project root from manifest'
    )
    
    parser.add_argument(
        '--mode', '-m',
        choices=['analyze', 'provision', 'diff', 'validate'],
        default='analyze',
        help='Operation mode (default: analyze)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without applying them'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    # Validate config file exists
    if not args.config.exists():
        print(f"❌ Config file not found: {args.config}")
        sys.exit(1)
    
    try:
        provisioner = BMADProvisioner(args.config, args.project_root)
        
        # Execute requested mode
        if args.mode == 'validate':
            success = provisioner.validate_manifest()
        elif args.mode == 'analyze':
            success = provisioner.validate_manifest() and provisioner.analyze()
        elif args.mode == 'diff':
            success = provisioner.validate_manifest() and provisioner.diff()
        elif args.mode == 'provision':
            success = provisioner.validate_manifest() and provisioner.provision(args.dry_run, args.generator_script)
        else:
            print(f"❌ Unknown mode: {args.mode}")
            sys.exit(1)
        
        sys.exit(0 if success else 1)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
