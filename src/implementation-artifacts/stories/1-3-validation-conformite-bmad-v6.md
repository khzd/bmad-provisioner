# Story 1.3: Validation de Conformité BMAD v6.x

**Status:** ready-for-dev  
**Epic:** Epic 1 - Consolidation & Stabilisation  
**Priority:** P1 - High  
**Estimated Effort:** 3-5 days  

## User Story

En tant que Lead Développeur BMAD, je veux une validation automatique de conformité avec BMAD v6.x afin de garantir que le provisionnement fonctionne correctement avec la version cible du framework.

## Acceptance Criteria

### AC 1.5: Détection de Version BMAD
- **Given** un projet BMAD installé
- **When** je lance la validation de conformité
- **Then** le système détecte automatiquement la version BMAD installée
- **And** vérifie la compatibilité avec la version cible (v6.x)

### AC 1.6: Validation des Compétences Générées
- **Given** des compétences BMAD générées par le provisioner
- **When** je lance la validation
- **Then** chaque compétence est validée selon les standards BMAD v6.x
- **And** les incompatibilités sont signalées avec des messages détaillés

### AC 1.7: Validation des Workflows
- **Given** les workflows générés
- **When** je lance la validation
- **Then** chaque workflow est vérifié pour la compatibilité v6.x
- **And** les patterns obsolètes sont détectés

## Technical Requirements

### Version Detection
- [ ] Détection automatique de la version BMAD installée
- [ ] Vérification de la compatibilité avec la version cible
- [ ] Messages d'erreur clairs pour les versions incompatibles

### Schema Validation
- [ ] Validation des fichiers YAML selon les schémas BMAD v6.x
- [ ] Vérification des structures de compétences
- [ ] Validation des patterns de workflow

### Compatibility Matrix
- [ ] Matrice de compatibilité version BMAD / fonctionnalités provisioner
- [ ] Avertissements pour les fonctionnalités expérimentales
- [ ] Recommandations de mise à jour

## Dependencies

- **BMAD Framework:** Version v6.x installée
- **Schema Validation:** Outils de validation YAML
- **Version Detection:** Méthodes de détection de version

## Testing

### Validation Tests
- [ ] Test de détection de version BMAD
- [ ] Test de validation de compétences
- [ ] Test de validation de workflows
- [ ] Test de compatibilité multi-version

### Error Scenarios
- [ ] Gestion des versions BMAD incompatibles
- [ ] Validation avec compétences corrompues
- [ ] Workflows obsolètes

## Notes

- Cette story est essentielle pour la compatibilité avec BMAD v6.x
- Doit être implémentée pour garantir la stabilité du provisionnement
- Focus sur la détection proactive des problèmes de compatibilité
- Préparer pour les futures versions de BMAD

## Related Stories

- **Next:** 1.4 - Optimisation des performances
- **Dependencies:** 1.2 (Tests unitaires pour validation)
- **Blocks:** Epic 2 (Extension des compétences)