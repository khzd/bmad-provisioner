# Story 1.5: Stratégie d'Agents - Generalistes vs Spécialistes

**Status:** ready-for-dev  
**Epic:** Epic 1 - Consolidation & Stabilisation  
**Priority:** P2 - Medium  
**Estimated Effort:** 2-3 jours  

## Contexte

Le PRD ne couvre pas la stratégie d'évolution des compétences BMAD. Lors de la conception du qa-leader, une réflexion stratégique s'est imposée face à l'explosion des 97K agents créés en 1 mois par la communauté IA.

## Problématique

**Dilemme :** Créer des spécialistes par domaine (healthcare, marketing, finance) ou des généralistes intelligents ?

### Option A : Spécialistes par Domaine
```yaml
qa-leader:
  specialists:
    - functional-healthcare    # Test fonctionnel healthcare
    - functional-marketing     # Test fonctionnel marketing  
    - functional-finance       # Test fonctionnel finance
    # ... explosion combinatoire
```

**Inconvénients :**
- ❌ **Explosion combinatoire** (97K agents !)
- ❌ **Maintenance lourde**
- ❌ **Complexité exponentielle**

### Option B : Généralistes Intelligents
```yaml
qa-leader:
  specialists:
    - functional-general       # Test fonctionnel général
    - business-general         # Test métier général
    - user-journey-general     # Parcours utilisateurs général
```

**Avantages :**
- ✅ **Scalabilité exponentielle**
- ✅ **Maintenance simplifiée**
- ✅ **Adaptabilité maximale**

## Décision Stratégique

**Choix :** **Approche "Dev Senior"** - 3 généralistes intelligents

### Rationale

#### 1. Analogie Dev Senior
Dans les entreprises, un Dev Senior est recruté pour son expertise technique, pas son expertise métier. Il reçoit une formation de 2-3 semaines sur les concepts métier, puis implémente avec expertise.

#### 2. Scalabilité Face à l'Explosion des Agents
Avec 97K agents créés en 1 mois, une approche spécialiste par domaine devient ingérable. Les généralistes intelligents offrent une meilleure scalabilité.

#### 3. Maintenance Simplifiée
3 agents à maintenir vs 9+ spécialistes par domaine. Moins de complexité, plus de stabilité.

#### 4. Adaptabilité Maximale
Les généralistes peuvent s'adapter à de nouveaux domaines sans création d'agent supplémentaire.

## Architecture Proposée

### Nouvelle Structure du qa-leader
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

### Workflow Type "Dev Senior"
1. **Leader** reçoit la demande
2. **Détecte le domaine** (healthcare/marketing/finance)
3. **Charge le spécialiste général**
4. **Spécialiste général** :
   - Pose les bonnes questions pour comprendre le domaine
   - Apprend rapidement les concepts clés
   - Implémente avec expertise technique
   - Documente pour la prochaine fois

## Acceptance Criteria

### AC 1.11: Architecture Généraliste
- **Given** un besoin de test fonctionnel dans un nouveau domaine
- **When** je configure le qa-leader
- **Then** 3 généralistes intelligents suffisent à couvrir tous les domaines
- **And** pas besoin de créer de nouveaux spécialistes

### AC 1.12: Adaptabilité Rapide
- **Given** un spécialiste général chargé
- **When** il reçoit une demande dans un domaine inconnu
- **Then** il pose les bonnes questions pour comprendre le domaine
- **And** il s'adapte rapidement avec une courbe d'apprentissage courte

### AC 1.13: Scalabilité
- **Given** l'explosion des 97K agents
- **When** de nouveaux domaines émergent
- **Then** les généralistes s'adaptent sans création d'agent supplémentaire
- **And** la maintenance reste simplifiée

## Technical Requirements

### Compétences des Généralistes
- **functional-general** : pytest, TDD, scénarios d'usage, validation fonctionnelle
- **business-general** : règles métier, workflows, validation processus
- **user-journey-general** : user stories, parcours clients, UX validation

### Système de Détection de Domaine
- Analyse des mots-clés dans la demande
- Détection automatique healthcare/marketing/finance
- Routing intelligent vers le bon généraliste

### Documentation d'Apprentissage
- Stockage des concepts appris par domaine
- Amélioration continue des connaissances
- Partage entre spécialistes

## Dependencies

- **PRD Complété** : Section "Stratégie d'Évolution des Compétences"
- **Architecture MD** : Section "Philosophie de Conception - Approche Dev Senior"
- **Skills Manifest** : Configuration des 3 généralistes

## Testing

### Tests de Scalabilité
- [ ] Test avec 10+ domaines différents
- [ ] Validation de l'adaptabilité rapide
- [ ] Mesure de la courbe d'apprentissage

### Tests de Maintenance
- [ ] Ajout d'un nouveau domaine sans création d'agent
- [ ] Mise à jour des connaissances partagées
- [ ] Validation de la documentation d'apprentissage

### Tests de Performance
- [ ] Temps de réponse avec généralistes vs spécialistes
- [ ] Charge mémoire avec 3 agents vs 9+ agents
- [ ] Maintenance simplifiée

## Notes

- Cette décision complète le PRD sur un aspect crucial non couvert
- L'approche "Dev Senior" s'inspire des meilleures pratiques du recrutement
- La scalabilité est prioritaire face à l'explosion des agents IA
- La maintenance simplifiée garantit la pérennité du projet

## Related Stories

- **Next:** Epic 2 - Extension des compétences (avec l'approche généraliste)
- **Dependencies:** 1.1, 1.2, 1.3, 1.4 (stabilité de base requise)
- **Blocks:** None

## Documentation Impact

- **PRD.md** : Ajout section "Stratégie d'Évolution des Compétences"
- **architecture.md** : Ajout section "Philosophie de Conception - Approche Dev Senior"
- **sprint-status.yaml** : Ajout story 1.5 en ready-for-dev