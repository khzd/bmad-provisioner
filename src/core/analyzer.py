"""
Gap Analyzer - Compare manifest vs installed BMAD configuration
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Optional
import yaml
import csv
from enum import Enum


class ChangeType(Enum):
    """Type of change detected"""
    MISSING = "missing"
    OUTDATED = "outdated"
    UP_TO_DATE = "up_to_date"
    CONFLICTING = "conflicting"
    EXTRA = "extra"


@dataclass
class FileStatus:
    """Status of a single file"""
    path: Path
    change_type: ChangeType
    details: str
    
    def __repr__(self):
        emoji = {
            ChangeType.MISSING: "❌",
            ChangeType.OUTDATED: "⚠️",
            ChangeType.UP_TO_DATE: "✅",
            ChangeType.CONFLICTING: "🔥",
            ChangeType.EXTRA: "📦"
        }
        return f"{emoji[self.change_type]} {self.path}: {self.details}"


@dataclass
class LeaderStatus:
    """Status of a leader skill"""
    name: str
    installed: bool
    files: List[FileStatus]
    
    @property
    def is_up_to_date(self) -> bool:
        return all(f.change_type == ChangeType.UP_TO_DATE for f in self.files)
    
    @property
    def needs_update(self) -> bool:
        return any(f.change_type in [ChangeType.MISSING, ChangeType.OUTDATED] 
                   for f in self.files)


@dataclass
class GapAnalysisReport:
    """Complete gap analysis report"""
    bmad_version: Optional[str]
    leaders: List[LeaderStatus]
    recommendations: List[str]
    
    def summary(self) -> str:
        """Generate human-readable summary"""
        lines = ["📊 Gap Analysis Report", "=" * 50, ""]
        
        # BMAD version
        if self.bmad_version:
            lines.append(f"BMAD Version: {self.bmad_version}")
        else:
            lines.append("⚠️  BMAD version not detected")
        lines.append("")
        
        # Leaders status
        for leader in self.leaders:
            if leader.is_up_to_date:
                lines.append(f"✅ {leader.name}: Up to date")
            elif not leader.installed:
                lines.append(f"❌ {leader.name}: Not installed")
            elif leader.needs_update:
                lines.append(f"⚠️  {leader.name}: Needs update")
                for file_status in leader.files:
                    if file_status.change_type != ChangeType.UP_TO_DATE:
                        lines.append(f"   {file_status}")
        
        lines.append("")
        
        # Recommendations
        if self.recommendations:
            lines.append("💡 Recommendations:")
            for rec in self.recommendations:
                lines.append(f"   - {rec}")
        
        return "\n".join(lines)


class GapAnalyzer:
    """Analyze gaps between manifest and installed BMAD"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.bmad_root = project_root / "_bmad"
        self.custom_skills_root = self.bmad_root / "custom-skills"
    
    def detect_bmad_version(self) -> Optional[str]:
        """Detect installed BMAD version"""
        package_json = self.project_root / "package.json"
        if package_json.exists():
            try:
                import json
                with open(package_json) as f:
                    data = json.load(f)
                    deps = data.get('dependencies', {})
                    if 'bmad-method' in deps:
                        return deps['bmad-method']
            except:
                pass
        
        # Try to read from BMAD core
        core_version = self.bmad_root / "core" / "VERSION"
        if core_version.exists():
            return core_version.read_text().strip()
        
        return None
    
    def check_leader_installed(self, leader_name: str) -> bool:
        """Check if a leader is installed"""
        leader_path = self.custom_skills_root / leader_name
        return leader_path.exists()
    
    def check_file_status(self, file_path: Path, expected_content: Optional[str] = None) -> FileStatus:
        """Check status of a single file"""
        if not file_path.exists():
            return FileStatus(
                path=file_path,
                change_type=ChangeType.MISSING,
                details="File does not exist"
            )
        
        # If no expected content, just check existence
        if expected_content is None:
            return FileStatus(
                path=file_path,
                change_type=ChangeType.UP_TO_DATE,
                details="File exists"
            )
        
        # Compare content (simplified - could use hash)
        actual_content = file_path.read_text()
        if actual_content == expected_content:
            return FileStatus(
                path=file_path,
                change_type=ChangeType.UP_TO_DATE,
                details="Content matches"
            )
        else:
            return FileStatus(
                path=file_path,
                change_type=ChangeType.OUTDATED,
                details="Content differs"
            )
    
    def check_csv_status(self, csv_path: Path, expected_rows: List[List[str]]) -> FileStatus:
        """Check CSV file status with smart comparison"""
        if not csv_path.exists():
            return FileStatus(
                path=csv_path,
                change_type=ChangeType.MISSING,
                details=f"CSV missing ({len(expected_rows)} rows expected)"
            )
        
        # Read existing CSV
        with open(csv_path, 'r') as f:
            reader = csv.reader(f)
            existing_rows = list(reader)
        
        # Compare
        missing_rows = []
        for expected_row in expected_rows:
            if expected_row not in existing_rows:
                missing_rows.append(expected_row)
        
        if not missing_rows:
            return FileStatus(
                path=csv_path,
                change_type=ChangeType.UP_TO_DATE,
                details=f"All {len(expected_rows)} rows present"
            )
        else:
            return FileStatus(
                path=csv_path,
                change_type=ChangeType.OUTDATED,
                details=f"{len(missing_rows)} rows missing"
            )
    
    def analyze_leader(self, leader, manifest_leader) -> LeaderStatus:
        """Analyze a single leader"""
        leader_name = manifest_leader.name
        leader_path = self.custom_skills_root / leader_name
        
        # Extract short leader name (remove -leader suffix if present)
        short_leader_name = leader_name.replace('-leader', '')
        
        files = []
        
        # Check leader installed
        if not self.check_leader_installed(leader_name):
            return LeaderStatus(
                name=leader_name,
                installed=False,
                files=[FileStatus(
                    path=leader_path,
                    change_type=ChangeType.MISSING,
                    details="Leader not installed"
                )]
            )
        
        # Check key files
        key_files = [
            leader_path / "agents" / f"leader-{short_leader_name}.md",
            leader_path / "workflows" / "route-to-specialist.yaml",
            leader_path / "references" / "routing-rules.md",
        ]
        
        for file_path in key_files:
            files.append(self.check_file_status(file_path))
        
        # Check specialist files
        for spec in manifest_leader.specialists:
            spec_file = leader_path / "agents" / f"specialist-{spec.id}.md"
            files.append(self.check_file_status(spec_file))
        
        # Check CSV files if domain specific
        if manifest_leader.domain != 'generic':
            data_path = leader_path / "data"
            if data_path.exists():
                for csv_file in data_path.glob("*.csv"):
                    files.append(FileStatus(
                        path=csv_file,
                        change_type=ChangeType.UP_TO_DATE,
                        details="CSV exists (content check skipped)"
                    ))
        
        return LeaderStatus(
            name=leader_name,
            installed=True,
            files=files
        )
    
    def analyze(self, manifest) -> GapAnalysisReport:
        """Perform complete gap analysis"""
        bmad_version = self.detect_bmad_version()
        
        # Analyze each leader
        leaders = []
        for manifest_leader in manifest.project.leaders:
            leader_status = self.analyze_leader(manifest_leader, manifest_leader)
            leaders.append(leader_status)
        
        # Generate recommendations
        recommendations = []
        
        # Check if BMAD installed
        if not self.bmad_root.exists():
            recommendations.append("BMAD not installed - run: npx bmad-method@alpha install")
        
        # Check leaders
        missing_leaders = [l for l in leaders if not l.installed]
        if missing_leaders:
            recommendations.append(
                f"Install {len(missing_leaders)} missing leaders: "
                f"{', '.join(l.name for l in missing_leaders)}"
            )
        
        outdated_leaders = [l for l in leaders if l.installed and l.needs_update]
        if outdated_leaders:
            recommendations.append(
                f"Update {len(outdated_leaders)} outdated leaders: "
                f"{', '.join(l.name for l in outdated_leaders)}"
            )
        
        if not missing_leaders and not outdated_leaders:
            recommendations.append("All leaders up to date - safe to provision")
        
        return GapAnalysisReport(
            bmad_version=bmad_version,
            leaders=leaders,
            recommendations=recommendations
        )