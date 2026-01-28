# Story 1.1: Gestion de base des compétences

**Status:** ready-for-dev  
**Epic:** Epic 1 - MVP Core  
**Priority:** P1 - High  
**Estimated Effort:** 3-5 days  

## User Story

En tant que Lead Développeur BMAD, je veux pouvoir gérer les compétences personnalisées de base afin de standardiser les configurations à travers mes projets.

## Acceptance Criteria

### AC 1.1: Création de compétences simples
- **Given** un template YAML de compétence BMAD
- **When** je crée une nouvelle compétence
- **Then** la compétence est validée selon les standards BMAD v6.x
- **And** la compétence est enregistrée dans le système

### AC 1.2: Liste des compétences existantes
- **Given** plusieurs compétences BMAD personnalisées
- **When** je demande la liste des compétences
- **Then** toutes les compétences sont affichées avec leur statut
- **And** les informations de version et de compatibilité sont visibles

### AC 1.3: Suppression sécurisée
- **Given** une compétence BMAD personnalisée
- **When** je la supprime
- **Then** un backup est automatiquement créé
- **And** les dépendances sont vérifiées avant suppression
- **And** une confirmation est demandée

## Technical Requirements

### Backend
- [ ] Validation YAML selon schéma BMAD v6.x
- [ ] Stockage des compétences dans un format structuré
- [ ] Gestion des versions et historique des modifications
- [ ] Vérification des dépendances avant suppression

### CLI Interface
- [ ] Commande `bmad-provisioner skill create`
- [ ] Commande `bmad-provisioner skill list`
- [ ] Commande `bmad-provisioner skill delete`
- [ ] Sortie formatée et compréhensible

### Integration
- [ ] Compatible avec BMAD v6.x workflow
- [ ] Support des patterns Leader-Specialists
- [ ] Intégration avec le système de provisionnement

## Dependencies

- **Framework:** BMAD v6.x
- **Language:** Python 3.11+
- **Configuration:** YAML validation
- **Storage:** Local file system

## Testing

### Unit Tests
- [ ] Validation YAML schema
- [ ] Gestion des erreurs
- [ ] Backup system

### Integration Tests
- [ ] BMAD framework compatibility
- [ ] CLI command execution
- [ ] Multi-project isolation

## Notes

- Cette story est la première étape du MVP Core
- Doit être complétée avant de passer aux stories suivantes
- Focus sur la simplicité et la fiabilité
- Préparer la base pour les fonctionnalités avancées

## Related Stories

- **Next:** 1.2 - Provisionnement simple
- **Dependencies:** None
- **Blocks:** None