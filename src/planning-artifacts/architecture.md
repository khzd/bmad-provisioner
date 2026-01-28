---
stepsCompleted: [1]
inputDocuments: 
  - 'docs/PRD.md'  # Product Requirements Document
  - 'src/bmad_provisioner.py'  # Main CLI implementation
  - 'src/core/analyzer.py'  # Gap analysis engine
  - 'src/core/generator.py'  # Provisioning engine
  - 'src/models/manifest.py'  # Data models
  - 'src/templates/skills-manifest-bmad-provisioner.yaml'  # Example manifest
  - 'src/bmad-skill-generator/scripts/init_bmad_skill.py'  # Skill generator
workflowType: 'architecture'
project_name: 'bmad-provisioner'
user_name: 'Bibi'
date: '2026-01-28T15:45:18.123Z'
---

# Architecture Decision Document

_This document builds collaboratively through step-by-step discovery. Sections are appended as we work through each architectural decision together._ 

## 1. Context & Scope

### 1.1 Business Context

**BMAD Provisioner** est un outil de productivité conçu pour les équipes de développement utilisant le framework BMAD (Business Model Architecture Design). Il résout la complexité de gestion des compétences BMAD personnalisées en offrant une solution standardisée, automatisée et protégée contre les pertes de configuration lors des mises à jour du framework.

### 1.2 Technical Context

- **Langage Principal**: Python 3.11+
- **Framework Cible**: BMAD v6.x
- **Pattern Architectural**: Leader-Specialists
- **Workflow Supporté**: Quick Flow (Phase 0-1-2-3-4)
- **Environnement Cible**: Multi-projets, CLI-first

### 1.3 Problem Statement

Les équipes BMAD rencontrent des difficultés pour :
- Gérer des compétences personnalisées de manière centralisée
- Protéger leurs configurations lors des mises à jour BMAD
- Standardiser les compétences à travers plusieurs projets
- Maintenir la cohérence entre différentes versions

### 1.4 Success Criteria

- **Performance**: Temps de configuration réduit de 60%
- **Fiabilité**: Taux de succès > 95% pour les provisionnements
- **Adoption**: 80% des équipes BMAD adoptent l'outil dans les 3 premiers mois
- **ROI**: Retour sur investissement > 150% sur 12 mois

## 2. Architectural Patterns

### 2.1 Core Pattern: Declarative Infrastructure as Code

```
Manifeste YAML → Analyse d'écart → Provisionnement → Validation → Déploiement
```

**Rationale**: 
- Permet une gestion versionnée des compétences BMAD
- Survit aux mises à jour du framework BMAD
- Facilite la standardisation entre projets
- Supporte le CI/CD

### 2.2 Integration Pattern: Leader-Specialists

**Leader Agent**: Routeur et coordinateur
- Analyse les demandes entrantes
- Détermine le spécialiste approprié
- Coordonne le travail multi-domaines

**Specialist Agents**: Experts de domaine
- Frontend, Backend, QA, CIS, etc.
- Compétences spécifiques et approfondies
- Respect des meilleures pratiques de leur domaine

**Rationale**:
- Aligné avec l'architecture BMAD existante
- Permet l'évolutivité horizontale
- Facilite la maintenance et les mises à jour

### 2.3 Workflow Pattern: Quick Flow Integration

**Phase 0-1-2-3-4 Support**:
- **Phase 0**: Analyse et découverte
- **Phase 1**: Planification et conception
- **Phase 2**: Prototypage et validation
- **Phase 3**: Architecture et design
- **Phase 4**: Implémentation et déploiement

**Rationale**:
- Intégration transparente avec les workflows BMAD existants
- Support des différents types de leaders (dev-leader, qa-leader, cis-leader)
- Maintient la compatibilité ascendante

## 3. System Architecture

### 3.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    BMAD Provisioner CLI                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │   Main Orchestrator (bmad_provisioner.py)               │ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    Core Components                          │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │   Manifest      │  │   Gap Analyzer  │  │   Generator  │ │
│  │   Parser        │  │   (analyzer.py) │  │   (generator │ │
│  │   (manifest.py) │  │                 │  │   .py)       │ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    BMAD Integration                         │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │   bmad-skill-   │  │   Project       │  │   Backup &   │ │
│  │   generator     │  │   Discovery     │  │   Restore    │ │
│  │                 │  │                 │  │              │ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    Target Projects                          │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │   Project A     │  │   Project B     │  │   Project C  │ │
│  │   (HealthAI)    │  │   (Finance)     │  │   (Retail)   │ │
│  │                 │  │                 │  │              │ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Component Architecture

#### 3.2.1 Core Components

**BMADProvisioner (Orchestrator)**
- Point d'entrée principal
- Gestion des modes (analyze, provision, diff, validate)
- Coordination entre les composants
- Gestion des erreurs et logging

**SkillsManifest (Data Model)**
- Parsing et validation YAML
- Modélisation des compétences BMAD
- Validation de compatibilité
- Gestion des dépendances

**GapAnalyzer (Analysis Engine)**
- Détection des écarts entre manifeste et installation
- Analyse de version BMAD
- Génération de recommandations
- Reporting détaillé

**SkillGenerator (Provisioning Engine)**
- Intégration avec bmad-skill-generator
- Génération de compétences personnalisées
- Gestion des spécialistes
- Validation de conformité

#### 3.2.2 Supporting Components

**SkillBackup (Data Protection)**
- Sauvegarde avant provisionnement
- Restauration en cas d'échec
- Gestion des versions
- Audit trail

**FileStatusChecker (Validation)**
- Vérification de l'intégrité des fichiers
- Détection des modifications
- Comparaison de contenu
- Reporting de conformité

## 4. Data Architecture

### 4.1 Data Models

#### 4.1.1 SkillsManifest

```yaml
project:
  name: string
  bmad_version: string
  root: Path
  leaders: List[Leader]
  customizations: Dict[string, Customization]
  integrations: List[WorkflowIntegration]

Leader:
  name: string
  domain: string
  specialists: List[Specialist]
  phase: string

Specialist:
  id: string
  name: string
  domain: string
  skills: List[string]
  compliance_notes: Optional[string]
```

#### 4.1.2 GapAnalysisReport

```python
class GapAnalysisReport:
    bmad_version: Optional[str]
    leaders: List[LeaderStatus]
    recommendations: List[str]
    
class LeaderStatus:
    name: str
    installed: bool
    files: List[FileStatus]
    needs_update: bool
    
class FileStatus:
    path: Path
    change_type: ChangeType  # MISSING, OUTDATED, UP_TO_DATE, etc.
    details: str
```

### 4.2 Data Flow

```
1. Manifest Input (YAML)
   ↓
2. Validation & Parsing
   ↓
3. Project Discovery
   ↓
4. Gap Analysis
   ↓
5. Recommendations
   ↓
6. Provisioning
   ↓
7. Validation & Reporting
```

### 4.3 Storage Strategy

**Configuration Storage**:
- Manifestes YAML dans chaque projet
- Configuration centralisée dans `_bmad/config.yaml`
- Versioning via Git

**State Storage**:
- Backups temporaires dans `_bmad/.backups/`
- Logs d'audit dans `_bmad/logs/`
- Cache intelligent pour les analyses

**Integration Storage**:
- Compétences générées dans `_bmad/custom-skills/`
- Workflows dans `_bmad/workflows/`
- Templates dans `_bmad/templates/`

## 5. Integration Architecture

### 5.1 BMAD Framework Integration

**Version Compatibility**:
- Support de BMAD v6.x
- Détection automatique de version
- Validation de compatibilité
- Migration assistée

**Workflow Integration**:
- Support des phases Quick Flow
- Intégration avec les patterns Leader-Specialists
- Compatibilité avec tous les types d'agents BMAD
- Extension des workflows existants

**File Structure Integration**:
- Respects BMAD directory conventions
- Intégration transparente avec `_bmad/` structure
- Compatibilité avec les fichiers de configuration existants
- Support des customizations YAML

### 5.2 External Tool Integration

**bmad-skill-generator**:
- Intégration via subprocess
- Génération de compétences personnalisées
- Support des domaines spécialisés (healthcare, qa, cis)
- Validation de conformité BMAD

**Git Integration**:
- Tracking des changements
- Support des branches et tags
- Audit trail des modifications
- Rollback capabilities

**CI/CD Integration**:
- Support des pipelines automatisés
- Validation en pré-production
- Déploiement contrôlé
- Monitoring et alerting

## 6. Security Architecture

### 6.1 Data Protection

**PHI Handling (Healthcare Domain)**:
- Encryption des données sensibles
- Audit trail pour l'accès aux données médicales
- Conformité HIPAA
- Minimisation des données collectées

**Access Control**:
- Authentification basée sur les permissions système
- Isolation des configurations par projet
- Validation des accès aux fichiers
- Logging des opérations sensibles

### 6.2 Compliance

**Healthcare Compliance**:
- Support HIPAA pour les projets médicaux
- Gestion des consentements patients
- Audit trail complet
- Encryption des données à l'arrêt et en transit

**General Compliance**:
- Conformité aux meilleures pratiques de sécurité
- Validation des entrées utilisateur
- Protection contre les injections
- Gestion sécurisée des backups

## 7. Performance Architecture

### 7.1 Scalability

**Horizontal Scaling**:
- Support multi-projets simultanés
- Analyse parallèle des écarts
- Provisionnement asynchrone
- Cache intelligent pour les grosses bases de code

**Vertical Scaling**:
- Optimisation des algorithmes d'analyse
- Lazy loading des composants
- Memory management efficace
- Profiling et monitoring des performances

### 7.2 Performance Targets

**Analysis Performance**:
- Gap analysis < 30 secondes pour 100 compétences
- Validation < 5 secondes pour 50 fichiers
- Discovery < 10 secondes pour 10 projets

**Provisioning Performance**:
- Provisionnement < 2 minutes pour 10 compétences
- Backup < 30 secondes pour 100 fichiers
- Restore < 1 minute pour 100 fichiers

## 8. Deployment Architecture

### 8.1 Development Environment

**Local Development**:
- Python 3.11+ requis
- Dépendances via requirements.txt
- Tests unitaires et d'intégration
- Documentation générée automatiquement

**Testing Strategy**:
- Tests unitaires > 80% coverage
- Tests d'intégration BMAD
- Tests de compatibilité de version
- Tests de performance et de charge

### 8.2 Production Deployment

**Distribution**:
- Package Python distribuable
- Installation via pip
- Dépendances automatiques
- Versioning sémantique

**Monitoring**:
- Logging structuré
- Metrics de performance
- Alerting sur les échecs
- Dashboard de suivi

## 9. Evolution & Maintenance

### 9.1 Version Management

**Backward Compatibility**:
- Support des anciens formats de manifeste
- Migration assistée des configurations
- Documentation des breaking changes
- Tests de régression

**Feature Evolution**:
- Architecture modulaire pour l'extension
- Plugin system pour les domaines spécialisés
- API stable pour les intégrations externes
- Roadmap alignée avec BMAD framework

### 9.2 Maintenance Strategy

**Automated Maintenance**:
- Validation continue des compatibilités
- Tests automatisés sur chaque commit
- Monitoring des performances
- Alerting sur les anomalies

**Manual Maintenance**:
- Documentation à jour
- Support des utilisateurs
- Amélioration continue basée sur feedback
- Sécurité et conformité régulière

## 10. Risk Management

### 10.1 Technical Risks

**BMAD Compatibility**:
- Risque: Incompatibilité avec les futures versions BMAD
- Mitigation: Architecture modulaire, tests de compatibilité continue
- Impact: Moyen à élevé

**Performance**:
- Risque: Ralentissement avec un grand nombre de compétences
- Mitigation: Optimisation progressive, cache intelligent
- Impact: Moyen

### 10.2 Organizational Risks

**Adoption**:
- Risque: Résistance au changement des équipes
- Mitigation: Formation progressive, support continu
- Impact: Moyen

**Dependency**:
- Risque: Trop grande dépendance à l'outil
- Mitigation: Documentation complète, procédures de secours
- Impact: Faible

## 11. Implementation Roadmap

### Phase 1: MVP (Mois 1-2)

**Core Functionality**:
- [ ] Gestion de base des compétences
- [ ] Provisionnement simple
- [ ] Validation de conformité BMAD
- [ ] Interface CLI de base

**Testing & Validation**:
- [ ] Tests unitaires > 80%
- [ ] Tests d'intégration BMAD
- [ ] Validation avec 2 projets pilotes

### Phase 2: Advanced Features (Mois 3-4)

**Gap Analysis**:
- [ ] Détection automatique des écarts
- [ ] Propositions correctives
- [ ] Reporting détaillé

**Multi-Project**:
- [ ] Gestion multi-projets
- [ ] Isolation des configurations
- [ ] Synchronisation contrôlée

### Phase 3: Optimization (Mois 5-6)

**Performance**:
- [ ] Optimisation des temps de provisionnement
- [ ] Cache intelligent
- [ ] Bulk operations

**User Experience**:
- [ ] Interface web simplifiée
- [ ] Notifications intelligentes
- [ ] Documentation interactive

## 12. Conclusion

Cette architecture propose une solution robuste et évolutive pour la gestion des compétences BMAD personnalisées. En combinant une approche déclarative avec des patterns architecturaux éprouvés, BMAD Provisioner offre une alternative fiable aux méthodes manuelles actuelles.

Les choix architecturaux prioritaires la maintenabilité, la performance et la compatibilité avec l'écosystème BMAD existant, tout en préparant le terrain pour des évolutions futures comme l'intégration CI/CD, l'interface web et le support multi-domaines avancé.

L'architecture est conçue pour survivre aux évolutions du framework BMAD tout en offrant une expérience utilisateur fluide et productive aux équipes de développement.