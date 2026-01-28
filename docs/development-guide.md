# BMAD Provisioner - Development Guide

## Overview

This guide provides comprehensive instructions for developers working on the BMAD Provisioner project. It covers setup, development practices, testing, and contribution guidelines.

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Setup Instructions](#2-setup-instructions)
3. [Development Workflow](#3-development-workflow)
4. [Code Style Guidelines](#4-code-style-guidelines)
5. [Testing Strategy](#5-testing-strategy)
6. [Debugging](#6-debugging)
7. [Contributing](#7-contributing)
8. [Troubleshooting](#8-troubleshooting)

## 1. Prerequisites

### System Requirements
- **Python:** 3.11 or higher
- **Git:** For version control
- **Virtual Environment:** Recommended for isolation

### Dependencies
```bash
# Core dependencies
pyyaml>=6.0

# Development dependencies (optional)
pytest>=7.0          # Testing framework
pytest-cov>=4.0      # Coverage reporting
black>=22.0          # Code formatting
flake8>=5.0          # Linting
mypy>=0.991          # Type checking
```

## 2. Setup Instructions

### 2.1 Clone the Repository
```bash
git clone <repository-url>
cd bmad-provisioner
```

### 2.2 Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 2.3 Install Dependencies
```bash
# Install core dependencies
pip install -r requirements.txt

# Install development dependencies (optional)
pip install pytest pytest-cov black flake8 mypy
```

### 2.4 Verify Installation
```bash
# Test basic functionality
python bmad_provisioner.py --help

# Run basic tests (if available)
python -m pytest tests/ -v
```

## 3. Development Workflow

### 3.1 Project Structure
```
bmad-provisioner/
├── bmad_provisioner.py       # Main CLI entry point
├── models/                   # Data models and validation
│   └── manifest.py
├── core/                     # Core business logic
│   ├── analyzer.py          # Gap analysis engine
│   └── generator.py         # Provisioning logic
├── templates/               # Configuration templates
├── tests/                   # Test files
├── docs/                    # Documentation
└── src/                     # Source code (legacy structure)
```

### 3.2 Development Process

#### 3.2.1 Feature Development
1. **Create Branch:** `git checkout -b feature/your-feature-name`
2. **Write Tests:** Create tests for new functionality
3. **Implement Feature:** Write the actual code
4. **Run Tests:** Ensure all tests pass
5. **Code Review:** Submit pull request for review

#### 3.2.2 Bug Fixes
1. **Create Branch:** `git checkout -b fix/issue-description`
2. **Write Test:** Create test that reproduces the bug
3. **Fix Bug:** Implement the fix
4. **Verify:** Ensure test passes and no regressions

### 3.3 Configuration Development

#### 3.3.1 Creating New Templates
1. **Template Location:** Add to `templates/` directory
2. **Naming Convention:** Use descriptive names with `.yaml` extension
3. **Validation:** Test template with validation tools
4. **Documentation:** Add comments explaining configuration options

#### 3.3.2 Adding New Configuration Options
1. **Model Update:** Update data models in `models/manifest.py`
2. **Validation:** Add validation rules
3. **Documentation:** Update documentation
4. **Tests:** Add tests for new options

## 4. Code Style Guidelines

### 4.1 Python Standards
- **PEP 8:** Follow Python style guide
- **Type Hints:** Use type annotations for all public functions
- **Docstrings:** Comprehensive docstrings for all public APIs

### 4.2 Code Formatting
```bash
# Format code using black
black .

# Check formatting
black --check .

# Lint code
flake8 .

# Type checking
mypy .
```

### 4.3 Naming Conventions
- **Classes:** PascalCase (`SkillsManifest`, `GapAnalyzer`)
- **Functions:** snake_case (`validate_manifest`, `analyze_project`)
- **Variables:** snake_case (`project_root`, `manifest_path`)
- **Constants:** UPPER_SNAKE_CASE (`DEFAULT_TIMEOUT`, `MAX_RETRIES`)

### 4.4 Import Organization
```python
# Standard library imports
import sys
import argparse
from pathlib import Path

# Third-party imports
import yaml

# Local imports
from models.manifest import SkillsManifest
from core.analyzer import GapAnalyzer
```

## 5. Testing Strategy

### 5.1 Test Structure
```
tests/
├── __init__.py
├── test_manifest.py          # Manifest parsing tests
├── test_analyzer.py          # Analysis engine tests
├── test_generator.py         # Provisioning tests
├── test_cli.py              # CLI interface tests
└── fixtures/                # Test data and fixtures
    ├── valid_manifest.yaml
    ├── invalid_manifest.yaml
    └── expected_outputs/
```

### 5.2 Writing Tests

#### 5.2.1 Unit Tests
```python
import pytest
from models.manifest import SkillsManifest

def test_valid_manifest_parsing():
    """Test parsing of valid manifest file."""
    manifest_data = {
        'project': {
            'name': 'test-project',
            'bmad_version': 'v6.x',
            'root': '/tmp/test'
        }
    }
    
    manifest = SkillsManifest.from_dict(manifest_data)
    assert manifest.project.name == 'test-project'
    assert manifest.project.bmad_version == 'v6.x'

def test_invalid_manifest_validation():
    """Test validation of invalid manifest."""
    manifest_data = {
        'project': {
            'name': '',  # Invalid: empty name
            'bmad_version': 'invalid-version'
        }
    }
    
    manifest = SkillsManifest.from_dict(manifest_data)
    errors = manifest.validate(Path('/tmp'))
    assert len(errors) > 0
```

#### 5.2.2 Integration Tests
```python
def test_end_to_end_provisioning(tmp_path):
    """Test complete provisioning workflow."""
    # Setup test project structure
    project_root = tmp_path / "test_project"
    project_root.mkdir()
    
    # Create BMAD structure
    bmad_dir = project_root / "_bmad"
    bmad_dir.mkdir()
    
    # Test provisioning
    provisioner = BMADProvisioner(
        manifest_path=Path("templates/skills-manifest-bmad-provisioner.yaml"),
        project_root=project_root
    )
    
    result = provisioner.provision(dry_run=True)
    assert result is True
```

### 5.3 Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=models --cov=core --cov-report=html

# Run specific test file
pytest tests/test_manifest.py

# Run specific test
pytest tests/test_manifest.py::test_valid_manifest_parsing

# Run tests with verbose output
pytest -v
```

### 5.4 Test Coverage
- **Target:** >80% code coverage
- **Coverage Report:** Generate HTML report for review
- **CI Integration:** Fail builds if coverage drops below threshold

## 6. Debugging

### 6.1 Common Issues

#### 6.1.1 YAML Parsing Errors
```python
# Enable verbose YAML parsing
import yaml
try:
    data = yaml.safe_load(file_content)
except yaml.YAMLError as e:
    print(f"YAML Error: {e}")
    print(f"Line: {e.problem_mark.line}")
```

#### 6.1.2 Path Resolution Issues
```python
# Debug path resolution
from pathlib import Path
project_root = Path("/path/to/project")
print(f"Project root exists: {project_root.exists()}")
print(f"Absolute path: {project_root.absolute()}")
```

#### 6.1.3 BMAD Integration Issues
```python
# Debug BMAD detection
analyzer = GapAnalyzer(project_root)
version = analyzer.detect_bmad_version()
print(f"Detected BMAD version: {version}")
```

### 6.2 Debugging Tools

#### 6.2.1 Logging
```python
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Use in code
logger.debug("Debug message")
logger.info("Information message")
logger.warning("Warning message")
logger.error("Error message")
```

#### 6.2.2 Interactive Debugging
```python
# Add breakpoint for interactive debugging
import pdb; pdb.set_trace()

# Or use Python's built-in breakpoint (Python 3.7+)
breakpoint()
```

### 6.3 Performance Debugging

#### 6.3.1 Profiling
```python
import cProfile
import pstats

# Profile function
def profile_function():
    # Your code here
    pass

cProfile.run('profile_function()', 'profile_stats')
stats = pstats.Stats('profile_stats')
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 functions
```

## 7. Contributing

### 7.1 Contribution Guidelines

#### 7.1.1 Before Contributing
1. **Fork the Repository:** Create your own fork
2. **Check Issues:** Look for existing issues or feature requests
3. **Discuss:** Create issue for major changes

#### 7.1.2 Pull Request Process
1. **Branch:** Create feature branch from `main`
2. **Commit:** Make atomic commits with clear messages
3. **Test:** Ensure all tests pass
4. **Documentation:** Update documentation for new features
5. **Review:** Address review feedback

#### 7.1.3 Commit Message Format
```
<type>: <description>

<optional body>

<optional footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Example:**
```
feat: Add support for multi-project configurations

- Add ProjectConfig model for handling multiple projects
- Update GapAnalyzer to support project isolation
- Add validation for project-specific configurations

Closes #123
```

### 7.2 Code Review Process

#### 7.2.1 Review Criteria
- **Functionality:** Does the code work as intended?
- **Tests:** Are appropriate tests included?
- **Documentation:** Is the code well-documented?
- **Style:** Does it follow coding standards?
- **Performance:** Are there any performance concerns?

#### 7.2.2 Review Process
1. **Automated Checks:** CI/CD pipeline validation
2. **Peer Review:** At least one maintainer review
3. **Testing:** Manual testing of new features
4. **Merge:** Squash and merge to main branch

## 8. Troubleshooting

### 8.1 Common Problems

#### 8.1.1 Permission Errors
```bash
# Fix file permissions
chmod +x bmad_provisioner.py

# Fix directory permissions
sudo chown -R $USER:$USER /path/to/project
```

#### 8.1.2 Python Path Issues
```bash
# Check Python path
python -c "import sys; print(sys.path)"

# Add to Python path
export PYTHONPATH="/path/to/project:$PYTHONPATH"
```

#### 8.1.3 Dependency Issues
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Check installed packages
pip list

# Check package versions
python -c "import yaml; print(yaml.__version__)"
```

### 8.2 Getting Help

#### 8.2.1 Documentation
- **README.md:** Basic usage and setup
- **docs/:** Comprehensive documentation
- **API Docs:** Generated from docstrings

#### 8.2.2 Community
- **Issues:** Report bugs and request features
- **Discussions:** Ask questions and share ideas
- **Contributing:** Guidelines for contributors

#### 8.2.3 Debug Mode
```bash
# Enable verbose output
python bmad_provisioner.py --verbose --config manifest.yaml --mode analyze

# Use debug flag if available
python bmad_provisioner.py --debug --config manifest.yaml
```

### 8.3 Known Limitations

#### 8.3.1 Current Limitations
- **Single-threaded:** No parallel processing support
- **Limited Error Recovery:** Some errors require manual intervention
- **Platform Dependencies:** Some features may vary by platform

#### 8.3.2 Workarounds
- **Large Projects:** Use dry-run mode first
- **Error Recovery:** Manual backup and restore
- **Platform Issues:** Check platform-specific documentation

## 9. Development Tools

### 9.1 IDE Configuration

#### 9.1.1 VS Code
```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true
}
```

#### 9.1.2 PyCharm
- Enable pytest integration
- Configure black formatter
- Set up flake8 inspection
- Enable type checking

### 9.2 Development Scripts

#### 9.2.1 Setup Script
```bash
#!/bin/bash
# setup-dev.sh

echo "Setting up development environment..."

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run initial tests
python -m pytest tests/ -v

echo "Development environment ready!"
```

#### 9.2.2 Quality Check Script
```bash
#!/bin/bash
# quality-check.sh

echo "Running quality checks..."

# Format code
black .

# Check formatting
black --check .

# Lint code
flake8 .

# Type checking
mypy .

# Run tests with coverage
pytest --cov=models --cov=core --cov-report=term-missing

echo "Quality checks complete!"
```

This development guide provides comprehensive instructions for contributing to the BMAD Provisioner project. Always refer to the latest version of this document and follow the established conventions for the best development experience.