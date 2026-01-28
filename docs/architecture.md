# BMAD Provisioner - Architecture Documentation

## Overview

This document provides a comprehensive technical architecture overview of the BMAD Provisioner, detailing the system design, component interactions, and technical decisions that support its role as an infrastructure-as-code tool for BMAD skill management.

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    BMAD Provisioner CLI                     │
│                    (bmad_provisioner.py)                    │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    BMAD Provisioner                         │
│                    (Core Engine)                            │
├─────────────────────┬───────────────────────────────────────┤
│  Configuration      │  Analysis & Provisioning              │
│  Management         │  Engine                               │
│  (models/)          │  (core/)                               │
│                     │                                       │
│  ┌─────────────────┐ │  ┌─────────────────┐                 │
│  │   Manifest      │ │  │   Analyzer      │                 │
│  │   Parser        │ │  │   (Gap Analysis)│                 │
│  │   (manifest.py) │ │  └─────────────────┘                 │
│  └─────────────────┘ │  ┌─────────────────┐                 │
│                     │  │   Generator     │                 │
│  ┌─────────────────┐ │  │   (Provisioning)│                 │
│  │   Validation    │ │  │   (generator.py)│                 │
│  │   Engine        │ │  └─────────────────┘                 │
│  │                 │ │  ┌─────────────────┐                 │
│  │                 │ │  │   Backup/Restore│                 │
│  │                 │ │  │   (backup.py)   │                 │
│  │                 │ │  └─────────────────┘                 │
│  └─────────────────┘ │                                       │
└─────────────────────┴───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    External Systems                         │
├─────────────────────┬───────────────────────────────────────┤
│  BMAD Framework     │  File System                          │
│  (v6.x)             │  (Project Structure)                  │
│                     │                                       │
│  ┌─────────────────┐ │  ┌─────────────────┐                 │
│  │   BMAD CLI      │ │  │   Project       │                 │
│  │   Integration   │ │  │   Root          │                 │
│  │                 │ │  │   (_bmad/)      │                 │
│  │                 │ │  │                 │                 │
│  │                 │ │  │   Skills        │                 │
│  │                 │ │  │   (custom/)     │                 │
│  │                 │ │  │                 │                 │
│  │                 │ │  │   Configs       │                 │
│  │                 │ │  │   (agents/)     │                 │
│  └─────────────────┘ │  └─────────────────┘                 │
└─────────────────────┴───────────────────────────────────────┘
```

## Component Architecture

### 1. Main CLI Component (`bmad_provisioner.py`)

#### Purpose
Primary entry point and orchestrator for all BMAD Provisioner operations.

#### Responsibilities
- Command-line argument parsing and validation
- Operation mode routing (analyze, provision, diff, validate)
- Error handling and user feedback
- Workflow coordination between components

#### Key Classes
```python
class BMADProvisioner:
    """Main provisioner orchestrator"""
    
    def __init__(self, manifest_path: Path, project_root: Optional[Path] = None)
    def validate_manifest(self) -> bool
    def analyze(self) -> bool
    def provision(self, dry_run: bool = False, generator_script: Optional[Path] = None) -> bool
    def diff(self) -> bool
```

#### Dependencies
- `models.manifest.SkillsManifest` - Configuration parsing
- `core.analyzer.GapAnalyzer` - Analysis engine
- `core.generator.SkillGenerator` - Provisioning engine

### 2. Configuration Management (`models/`)

#### Purpose
Data models and validation logic for YAML manifest files.

#### Components

##### 2.1 Manifest Parser (`models/manifest.py`)
```python
class SkillsManifest:
    """Represents a complete skills manifest configuration"""
    
    @classmethod
    def from_yaml(cls, path: Path) -> 'SkillsManifest'
    def validate(self, project_root: Path) -> List[str]
    def to_dict(self) -> Dict[str, Any]
```

##### 2.2 Data Models
```python
class ProjectConfig:
    """Project-level configuration"""
    name: str
    bmad_version: str
    root: Path

class LeaderConfig:
    """Leader configuration with specialists"""
    name: str
    domain: str
    phase: str
    specialists: List[SpecialistConfig]

class SpecialistConfig:
    """Specialist configuration"""
    id: str
    name: str
    domain: str
    skills: List[str]
```

#### Validation Rules
- YAML schema validation
- Path existence verification
- BMAD version compatibility
- Configuration completeness

### 3. Analysis Engine (`core/analyzer.py`)

#### Purpose
Performs gap analysis between desired and actual BMAD configurations.

#### Key Components

##### 3.1 Gap Analyzer
```python
class GapAnalyzer:
    """Analyzes gaps between desired and actual BMAD state"""
    
    def __init__(self, project_root: Path)
    def analyze(self, manifest: SkillsManifest) -> AnalysisReport
    def detect_bmad_version(self) -> Optional[str]
    def check_leader_status(self, leader: LeaderConfig) -> LeaderStatus
    def compare_files(self, leader_path: Path, template_files: List[Path]) -> List[FileStatus]
```

##### 3.2 Analysis Report
```python
class AnalysisReport:
    """Comprehensive analysis results"""
    bmad_version: Optional[str]
    leaders: List[LeaderStatus]
    recommendations: List[str]
    
    def summary(self) -> str
    def detailed_report(self) -> str
```

#### Analysis Process
1. **BMAD Detection:** Locate and validate BMAD installation
2. **Leader Analysis:** Check each leader's installation status
3. **File Comparison:** Compare actual vs expected file states
4. **Gap Identification:** Identify missing, outdated, or incorrect configurations
5. **Recommendations:** Generate actionable improvement suggestions

### 4. Provisioning Engine (`core/generator.py`)

#### Purpose
Automated generation and deployment of BMAD skills and configurations.

#### Key Components

##### 4.1 Skill Generator
```python
class SkillGenerator:
    """Generates BMAD skills from manifest configuration"""
    
    def __init__(self, generator_script: Path, project_root: Path)
    def generate_all(self, manifest: SkillsManifest) -> Dict[str, bool]
    def generate_leader(self, leader: LeaderConfig) -> bool
    def generate_specialist(self, leader_name: str, specialist: SpecialistConfig) -> bool
    def generate_customizations(self, leader_name: str, customizations: Dict) -> bool
```

##### 4.2 Backup System
```python
class SkillBackup:
    """Manages backup and restore of BMAD configurations"""
    
    def __init__(self, project_root: Path)
    def backup_skills(self) -> Optional[Path]
    def restore_backup(self, backup_path: Path) -> bool
    def list_backups(self) -> List[Path]
```

#### Provisioning Process
1. **Backup Creation:** Create snapshot of current configuration
2. **Leader Generation:** Generate leader-specific files and configurations
3. **Specialist Generation:** Create specialist definitions and workflows
4. **Customization Application:** Apply leader-specific customizations
5. **Integration Setup:** Configure workflow integrations
6. **Validation:** Verify successful deployment

## Data Flow Architecture

### Configuration Flow
```
YAML Manifest → Parser → Validation → Data Models → Analysis/Provisioning
```

### Analysis Flow
```
Current State → Gap Analysis → Recommendations → User Decision → Provisioning
```

### Provisioning Flow
```
Manifest → Generator → File Creation → Integration → Validation → Backup
```

## Integration Architecture

### BMAD Framework Integration

#### Compatibility Layer
- **Version Detection:** Automatic BMAD version identification
- **API Compatibility:** Support for BMAD v6.x features
- **Workflow Integration:** Seamless integration with BMAD workflows

#### File System Integration
- **Project Structure:** Understanding of BMAD project layout
- **File Operations:** Safe file creation, modification, and backup
- **Path Resolution:** Intelligent path handling across platforms

### External Tool Integration

#### bmad-skill-generator
- **Script Integration:** Direct integration with skill generation scripts
- **Parameter Passing:** Automatic parameter mapping
- **Error Handling:** Graceful handling of generation failures

#### Development Tools
- **Git Integration:** Version control awareness
- **IDE Support:** Compatible with common development environments
- **CI/CD Ready:** Designed for automated deployment pipelines

## Security Architecture

### Configuration Security
- **Path Validation:** Prevent directory traversal attacks
- **File Permissions:** Proper file permission management
- **Backup Security:** Secure backup storage and access

### Data Protection
- **PHI Handling:** Special considerations for healthcare data (in HealthAI template)
- **Encryption:** Support for encrypted configuration storage
- **Audit Trail:** Comprehensive logging of all operations

## Performance Architecture

### Optimization Strategies
- **Caching:** Intelligent caching of analysis results
- **Parallel Processing:** Concurrent analysis where possible
- **Lazy Loading:** Load only required components
- **Memory Management:** Efficient memory usage patterns

### Scalability Considerations
- **Large Projects:** Support for projects with many skills
- **Multi-Project:** Efficient handling of multiple project configurations
- **Performance Monitoring:** Built-in performance metrics

## Error Handling Architecture

### Error Categories
1. **Configuration Errors:** Invalid manifest files
2. **System Errors:** File system or permission issues
3. **Integration Errors:** BMAD framework issues
4. **User Errors:** Invalid command-line usage

### Recovery Strategies
- **Graceful Degradation:** Continue operation with reduced functionality
- **Rollback Mechanisms:** Automatic rollback on failure
- **User Guidance:** Clear error messages with suggested solutions

## Testing Architecture

### Test Categories
1. **Unit Tests:** Component-level testing
2. **Integration Tests:** End-to-end workflow testing
3. **Validation Tests:** Configuration and schema testing
4. **Performance Tests:** Load and stress testing

### Test Framework
- **pytest:** Primary testing framework
- **Mocking:** Comprehensive mocking for external dependencies
- **Coverage:** Target >80% code coverage

## Deployment Architecture

### Development Environment
- **Local Execution:** Direct Python execution
- **Virtual Environment:** Isolated Python environment
- **Development Tools:** Integrated development setup

### Production Deployment
- **Package Distribution:** Python package format
- **Dependencies:** Minimal external dependencies
- **Platform Support:** Cross-platform compatibility

### CI/CD Integration
- **Automated Testing:** Continuous integration testing
- **Deployment Pipelines:** Automated deployment workflows
- **Quality Gates:** Automated quality checks

## 3.3.2 Gestion des Compétences

- **Compétences personnalisées** : Installation et configuration
- **Dépendances** : Gestion automatique des dépendances entre compétences
- **Versioning** : Contrôle des versions des compétences installées
- **Backup/Restore** : Sauvegarde et restauration des configurations

## 3.4 Philosophie de Conception - Approche Dev Senior

### 3.4.1 Stratégie d'Agents Généralistes

**Principe Fondamental :** Adopter une approche similaire au recrutement Dev Senior dans les entreprises.

**Rationale :**
- **Scalabilité** : Face à l'explosion des 97K agents IA, une approche spécialiste par domaine devient ingérable
- **Maintenance Simplifiée** : 3 agents à maintenir vs 9+ spécialistes par domaine
- **Adaptabilité Maximale** : Les généralistes s'adaptent à de nouveaux domaines sans création d'agent supplémentaire

### 3.4.2 Architecture Généraliste pour qa-leader

```yaml
qa-leader:
  domain: healthcare, marketing, finance
  specialists:
    # Généralistes (Base)
    - functional-general       # Test fonctionnel général
    - business-general         # Test métier général  
    - user-journey-general     # Parcours utilisateurs général
    
    # Spécialistes (Optionnels)
    - functional-healthcare    # Si besoin de spécialisation healthcare
    - functional-marketing     # Si besoin de spécialisation marketing
    - functional-finance       # Si besoin de spécialisation finance
```

### 3.4.3 Workflow Type "Dev Senior"

#### Étapes du Processus
1. **Leader** reçoit la demande et détecte automatiquement le domaine (healthcare/marketing/finance)
2. **Charge le spécialiste général** approprié basé sur la nature de la demande
3. **Spécialiste général** :
   - Pose les bonnes questions pour comprendre le domaine spécifique
   - Apprend rapidement les concepts clés du domaine
   - Implémente avec expertise technique
   - Documente les apprentissages pour la prochaine fois

#### Avantages de l'Approche
- ✅ **Expertise Technique** : Les généralistes maîtrisent les fondamentaux
- ✅ **Adaptabilité Rapide** : Courbe d'apprentissage courte (2-3 semaines)
- ✅ **Maintenance Simplifiée** : Moins d'agents à maintenir et documenter
- ✅ **Scalabilité Exponentielle** : Supporte l'explosion des agents IA

### 3.4.4 Compétences des Généralistes

#### functional-general
- **Compétences de base :** pytest, TDD, scénarios d'usage, validation fonctionnelle
- **Adaptabilité :** Capacité à comprendre rapidement les spécificités fonctionnelles de tout domaine

#### business-general  
- **Compétences de base :** règles métier, workflows, validation processus
- **Adaptabilité :** Capacité à modéliser rapidement les processus métiers de tout secteur

#### user-journey-general
- **Compétences de base :** user stories, parcours clients, UX validation
- **Adaptabilité :** Capacité à comprendre rapidement les parcours utilisateurs de tout contexte

### 3.4.5 Système de Détection de Domaine

#### Analyse Contextuelle
- **Mots-clés** : Détection automatique basée sur le vocabulaire utilisé
- **Patterns** : Reconnaissance de patterns spécifiques à chaque domaine
- **Routing Intelligent** : Aiguillage vers le bon généraliste

#### Apprentissage Continu
- **Stockage des Concepts** : Mémorisation des concepts appris par domaine
- **Amélioration Continue** : Enrichissement des connaissances partagées
- **Partage entre Spécialistes** : Mutualisation des apprentissages

### 3.4.6 Impact sur l'Architecture Globale

#### Cohérence avec BMAD
- **Pattern Supporté :** Compatible avec le pattern Leader-Specialists de BMAD
- **Workflow Intégré :** S'inscrit naturellement dans le workflow Quick Flow
- **Extension Facile** : Peut être étendu à d'autres leaders (dev-leader, cis-leader)

#### Pérennité du Système
- **Évolutivité** : Supporte l'évolution continue du framework BMAD
- **Maintenabilité** : Réduction de la complexité de maintenance
- **Standardisation** : Approche uniforme applicable à tous les types de compétences

### 3.4.7 Best Practices Inspirées du Développement Logiciel

#### Recrutement Dev Senior
- **Expertise Technique** : Priorité à l'expertise plutôt qu'à la spécialisation métier
- **Capacité d'Apprentissage** : Importance de la capacité à apprendre rapidement
- **Adaptabilité** : Capacité à s'adapter à différents contextes métiers

#### Application à l'IA
- **Agents Polyvalents** : Préférer des agents avec une base solide et adaptable
- **Formation Continue** : Mettre en place des mécanismes d'apprentissage continu
- **Documentation Partagée** : Créer des bases de connaissances mutualisées

## Future Architecture Considerations

### Extensibility
- **Plugin Architecture:** Support for custom extensions
- **API Design:** RESTful API for programmatic access
- **Web Interface:** Future GUI development considerations

### Advanced Features
- **Real-time Monitoring:** Live configuration monitoring
- **Advanced Analytics:** Usage and performance analytics
- **Machine Learning:** Intelligent configuration suggestions

This architecture provides a solid foundation for the BMAD Provisioner's current functionality while maintaining flexibility for future enhancements and scaling requirements.