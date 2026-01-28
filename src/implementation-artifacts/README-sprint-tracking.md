# Sprint Status Tracking - Guide d'utilisation

## Vue d'ensemble

Ce système de tracking de sprint permet de suivre l'avancement du développement du **BMAD Provisioner** en mode **retro-planning**. 

**Important :** Ce système reflète l'état réel du projet (version 0.2 déjà existante) et non une roadmap théorique. Nous adaptons le tracking à la réalité du développement.

## Contexte du Projet

**BMAD Provisioner** est un outil CLI Python déjà fonctionnel en version 0.2 avec :
- ✅ CLI complète avec commandes analyze/provision/diff/validate
- ✅ Système de gap analysis opérationnel
- ✅ Génération de compétences BMAD intégrée
- ✅ Compétences BMAD installées (dev-leader, qa-leader, cis-leader)
- ✅ Manifestes et templates de configuration
- ✅ Documentation de développement

**Objectif :** Passer de la version 0.2 à une version 1.0 stable et complète.

## Structure du Système

```
src/implementation-artifacts/
├── sprint-status.yaml          # Fichier de suivi principal (ADAPTÉ À L'ÉTAT RÉEL)
├── stories/                    # Dossiers des stories individuelles
│   ├── 1-1-documentation-systeme-existant.md     # EN COURS - Ce que nous faisons
│   ├── 1-2-tests-unitaires-integration.md        # À développer
│   ├── 1-3-validation-conformite-bmad-v6.md      # À développer
│   ├── 1-4-optimisation-performances.md          # À développer
│   └── ...
└── README-sprint-tracking.md   # Ce guide (ADAPTÉ AU RETRO-PLANNING)
```

## Épics et Stories Actuels

### Epic 1: Consolidation & Stabilisation (EN COURS)
**Objectif :** Passer de la version 0.2 à une version 1.0 stable

- **1.1: Documentation du Système Existant** (in-progress) - Ce que nous faisons actuellement
- **1.2: Tests Unitaires et d'Intégration** (backlog) - Garantir la fiabilité
- **1.3: Validation de Conformité BMAD v6.x** (backlog) - Compatibilité framework
- **1.4: Optimisation des Performances** (backlog) - Améliorer l'expérience utilisateur

### Epic 2: Extension des Compétences (BACKLOG)
**Objectif :** Étendre les fonctionnalités au-delà de la version 0.2

- **2.1: Nouveaux Spécialistes selon Besoins Utilisateurs**
- **2.2: Intégration avec d'Autres Frameworks BMAD**
- **2.3: Amélioration de l'Expérience Utilisateur CLI**
- **2.4: Monitoring et Reporting Avancé**

### Epic 3: Production & Scaling (BACKLOG)
**Objectif :** Préparer pour un usage en production à grande échelle

- **3.1: Déploiement en Production**
- **3.2: Support Multi-projets Avancé**
- **3.3: Intégration CI/CD**
- **3.4: Documentation Utilisateur Finale**

## Comprendre le Fichier de Suivi

### Format YAML

Le fichier `sprint-status.yaml` contient :

- **Métadonnées du projet** : informations générales
- **Status definitions** : explication des différents statuts
- **development_status** : état actuel de chaque epic, story et retrospective

### Statuts des Épics

- `backlog` : Epic pas encore commencé
- `in-progress` : Epic en cours de développement
- `done` : Toutes les stories de l'épic sont terminées

### Statuts des Stories

- `backlog` : Story seulement définie dans les fichiers épic
- `ready-for-dev` : Fichier de story créé, prêt pour le développement
- `in-progress` : En cours de développement
- `review` : Développement terminé, en revue
- `done` : Story complètement terminée

### Statuts des Rétrospectives

- `optional` : Peut être complétée mais pas obligatoire
- `done` : Rétrospective terminée

## Workflow de Développement

### 1. Création d'une Story

1. **Créer le fichier de story** dans `stories/` avec le format : `{epic}-{story}-{titre}.md`
2. **Mettre à jour le statut** dans `sprint-status.yaml` :
   - Epic : `in-progress` (si c'est la première story)
   - Story : `ready-for-dev`

### 2. Développement

1. **Passer la story en** `in-progress` lors du démarrage du développement
2. **Développer** selon les critères d'acceptation définis
3. **Passer en** `review` quand le développement est terminé

### 3. Revue et Validation

1. **Reviewer** examine le code et les tests
2. **Passer en** `done` si tout est validé
3. **Documenter** les apprentissages pour la prochaine story

### 4. Rétrospective (Optionnel)

1. **Compléter** la retrospective si souhaité
2. **Passer le statut** en `done`

## Exemple de Workflow

```bash
# 1. Créer une nouvelle story
touch stories/1-2-provisionnement-simple.md

# 2. Mettre à jour le statut
# Dans sprint-status.yaml :
# epic-1: in-progress (déjà fait)
# 1-2-provisionnement-simple: ready-for-dev

# 3. Commencer le développement
# Modifier dans sprint-status.yaml :
# 1-2-provisionnement-simple: in-progress

# 4. Terminer le développement
# Modifier dans sprint-status.yaml :
# 1-2-provisionnement-simple: review

# 5. Après revue positive
# Modifier dans sprint-status.yaml :
# 1-2-provisionnement-simple: done
```

## Bonnes Pratiques

### Pour les Stories

- **Nommer clairement** : utiliser le format kebab-case
- **Définir des critères d'acceptation** précis et testables
- **Estimer l'effort** de manière réaliste
- **Documenter les dépendances**

### Pour le Tracking

- **Mettre à jour les statuts** en temps réel
- **Ne pas sauter d'étapes** dans le workflow
- **Documenter les blocages** dans les fichiers de story
- **Utiliser les rétrospectives** pour améliorer le processus

### Pour les Épics

- **Compléter les stories dans l'ordre** (sauf cas particuliers)
- **Ne pas démarrer un nouvel épic** tant que le précédent n'est pas terminé
- **Faire des points d'étape** réguliers

## Intégration avec BMAD

Ce système est conçu pour fonctionner avec le workflow BMAD :

1. **Phase 0-1** : Analyse et conception (définition des épics)
2. **Phase 2** : Solutioning (découpage en stories)
3. **Phase 3-4** : Implementation (développement selon ce tracking)

## Commandes Utiles

```bash
# Voir l'état actuel
cat src/implementation-artifacts/sprint-status.yaml

# Compter les stories par statut
grep -c "ready-for-dev" src/implementation-artifacts/sprint-status.yaml
grep -c "in-progress" src/implementation-artifacts/sprint-status.yaml
grep -c "done" src/implementation-artifacts/sprint-status.yaml

# Lister les stories existantes
ls src/implementation-artifacts/stories/
```

## Personas et Rôles

### Scrum Master (SM)
- **Responsable** : Création et suivi des stories
- **Fréquence** : Quotidienne
- **Objectif** : S'assurer que chaque story est bien définie avant développement

### Développeur (Dev)
- **Responsable** : Mise à jour des statuts pendant le développement
- **Fréquence** : En temps réel
- **Objectif** : Maintenir le tracking à jour

### Product Owner (PO)
- **Responsable** : Validation des critères d'acceptation
- **Fréquence** : À chaque passage en review/done
- **Objectif** : S'assurer de la qualité et de la conformité

## Points de Contrôle

### Daily Standup
- [ ] Quelles stories sont en cours ?
- [ ] Y a-t-il des blocages ?
- [ ] Quelles stories seront prêtes pour demain ?

### Review de Sprint
- [ ] Toutes les stories de l'épic sont-elles terminées ?
- [ ] Les critères d'acceptation sont-ils respectés ?
- [ ] Quels apprentissages pour le prochain épic ?

### Rétrospective
- [ ] Le workflow a-t-il fonctionné ?
- [ ] Qu'est-ce qui peut être amélioré ?
- [ ] Quels sont les points de friction ?

## Support et Maintenance

Pour toute question sur ce système de tracking :

1. **Consulter** ce guide
2. **Vérifier** les exemples dans le répertoire
3. **Contacter** l'équipe BMAD Provisioner

---

**Dernière mise à jour :** 28/01/2026  
**Version :** 1.0  
**Projet :** BMAD Provisioner