# InstallWizard — install.omar.paris vs hub.omar.paris

> Source : [CONTRACTS §InstallWizard — Renew OA V3 V0.5.3](https://omar.paris/doctrine/contracts)

OA expose **2 sites publics distincts** dédiés à 2 cas d'usage radicalement différents : daily ops (Hub) versus onboarding one-time (Install).

---

## Principe (proposition CCCU validée CTO)

| Aspect | `hub.{client}.com` (Hub) | `install.{client}.com` (Wizard) |
|---|---|---|
| **Phase OmarTop couverte** | P4 → P5 → P6 | P0 → P1 → P2 → P3 → P3.5 |
| **Cas d'usage** | Daily : voir apps, vault, paramètres | One-time : *« je viens de recevoir mon VPS »* |
| **Public** | User établi (familier) | User vierge (premier contact) |
| **Agent intégré** | `h-{client}` (Édilia DAF pour JAB) | `h-onboarding` (expert config pédagogue) |
| **Pattern UX** | Vue d'ensemble + édition | Wizard pas-à-pas + validation à chaque étape |
| **Durée session** | Quelques min | 30-60 min one-time |
| **Métaphore** | Tableau de bord voiture | Concessionnaire qui livre clé en main |

---

## Phases OmarTop par site

| Phase | Site hébergeur | URL pattern |
|---|---|---|
| P0 Commerce | `install.omar.paris` | `install.omar.paris/buy` (V2) |
| P1 Provisioning | `install.omar.paris` | `install.omar.paris/<client-id>/p1-provisioning` (V2) |
| P1.5 Audit pré-bootstrap | `install.omar.paris` | `install.omar.paris/<client-id>/p1-5-audit` |
| P2 L0 stack | `install.omar.paris` | `install.omar.paris/<client-id>/p2-l0-stack` |
| P3 L1 baseline | `install.omar.paris` | `install.omar.paris/<client-id>/p3-l1-baseline` |
| **P3.5 Vault setup** | `install.omar.paris` | `install.omar.paris/<client-id>/p3-5-vault-setup` |
| P4 Activation | `install.omar.paris` → handoff Hub | `install.omar.paris/<client-id>/p4-activation` puis redirect Hub |
| P5 Maintenance | `hub.{client}.com` | `hub.{client}.com/parametres/maintenance` |
| P6 Export | `hub.{client}.com` | `hub.{client}.com/parametres/export` |

---

## Stack technique recommandée (proposition CCMA)

- **Backend** : Flask (cohérence stack OA Hub V1a) + Vault HashiCorp API
- **Frontend** : même stack que Hub (Tailwind + Alpine.js) pour cohérence visuelle
- **Agent intégré** : `h-onboarding` (Hermes profile dédié) qui guide pas-à-pas
- **Auth** : magic link (pas d'auth user, juste URL signée 24h)
- **Persistance** : `/var/www/install-omar/state/<client-id>.yaml` (état wizard, reprise possible)

---

## Roadmap install.omar.paris

| Version | Quoi |
|---|---|
| **V0.4** (cette semaine) | Phase P3.5 gravée doctrinalement (`phases-spec.yaml` + skill `omar-top-bootstrap` mis à jour) |
| **V1** (semaine prochaine) | MVP wizard P2 → P3 → P3.5 → P4 (sans P0/P1 e-commerce). Utilisable pour Maryse onboarding. |
| **V2** (post-cabinet validé) | Full e-commerce P0 + provisioning auto Hetzner P1 + handoff Hub automatique |
| **V3** | Standard onboarding tous clients OA |

---

## Différence avec OmarTop « concept doctrinaire »

- **OmarTop** = doctrine (concept + `phases-spec.yaml` + `oa-doctor` + skill `omar-top-bootstrap`)
- **install.omar.paris** = implémentation concrète UI de OmarTop pour onboarding
- **hub.omar.paris** = implémentation concrète UI pour daily ops

OmarTop reste le **squelette commun** lu par les 2 sites.

---

## Pattern UX wizard

Pour chaque phase (P1.5 → P4), l'install wizard suit le même pattern :

1. **Intro** : explication pédagogique de ce qui va se passer (`h-onboarding`)
2. **Pré-check** : `oa-doctor --check-phase Px` retourne l'état actuel
3. **Action** : bouton « Lancer » qui déclenche `bootstrap-vX.sh --phase Px`
4. **Stream logs** : sortie temps réel dans une zone scrollable
5. **Validation** : `oa-doctor --check-phase Px --strict` doit retourner exit 0
6. **Suivant** : bouton « Phase suivante » apparaît seulement si validation OK

L'état est persisté à chaque étape dans `state/<client-id>.yaml` pour permettre la reprise après déconnexion.

---

## Voir aussi

- [Sites publics OA (Hub / Install / Top)](../vision/sites-oa.md)
- [Phases OmarTop — vue d'ensemble](../phases/index.md)
- [Phase P3.5 — Vault setup](../phases/P3.5.md)
- [Doctrine Multi-Vault](multi-vault.md)
