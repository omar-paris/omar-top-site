# Sites publics OA — Hub / Install / Top

> Source : [MANIFEST §13 — Renew OA V3 v1.2](https://omar.paris/doctrine/manifest)

OA expose **3 sites publics distincts** dédiés à 3 audiences différentes. Les 3 sites lisent la même source de vérité doctrinale (`phases-spec.yaml` + MANIFEST + CONTRACTS) mais l'exposent dans des formats différents.

---

## Table comparative

| Site | URL | Audience | Phase OmarTop | Statut |
|---|---|---|---|---|
| **Hub** | `hub.{client}.com` | User client établi (daily ops) | P4 → P6 | V0.5.0 LIVE |
| **Install** | `install.{client}.com` | User client vierge (one-time onboarding) | P0 → P3.5 | V1 cette semaine |
| **Top** | `top.omar.paris` | Agents IA + developers OA + auditeurs externes | doctrine OmarTop | V0.4 POC MkDocs |

---

## Métaphores

- **Hub** = backoffice quotidien client → *tableau de bord voiture*
- **Install** = wizard onboarding → *concessionnaire qui livre clé en main*
- **Top** = wiki / documentation OmarTop → *manuel constructeur + références techniques*

---

## Détail des 3 sites

### Hub (`hub.{client}.com`)

- **Cas d'usage** : daily ops — voir apps, vault, paramètres
- **Public** : user établi (familier de son VPS)
- **Agent intégré** : `h-{client}` (ex : Édilia DAF pour JAB)
- **Pattern UX** : vue d'ensemble + édition
- **Durée session** : quelques minutes
- **Phases couvertes** : P4 → P5 → P6
- **Stack V0** : statique HTML/JS + Caddy `file_server` + JSONs préconstruits

### Install (`install.{client}.com`)

- **Cas d'usage** : one-time — *"je viens de recevoir mon VPS"*
- **Public** : user vierge (premier contact)
- **Agent intégré** : `h-onboarding` (expert config pédagogue)
- **Pattern UX** : wizard pas-à-pas + validation à chaque étape
- **Durée session** : 30-60 min one-time
- **Phases couvertes** : P0 → P1 → P2 → P3 → P3.5 → P4 (handoff Hub)
- **Stack recommandée** : Flask + Tailwind + Alpine.js + Vault HashiCorp API
- **Auth** : magic link (URL signée 24h)
- **Persistance** : `/var/www/install-omar/state/<client-id>.yaml`

### Top (`top.omar.paris`)

- **Cas d'usage** : référence doctrinale OmarTop — phases, standards, principes
- **Public** : agents IA OA (CCMA, CCSV, CCSA, CCCU, `h-omar`) + developers + auditeurs externes
- **Pattern UX** : navigation arborescente + recherche
- **Source données** : MkDocs Material + `phases-spec.yaml` régénéré
- **Phases couvertes** : doctrine intégrale OmarTop (P0 → P8)

---

## Phases OmarTop par site

| Phase | Site hébergeur | URL pattern |
|---|---|---|
| P0 Commerce | `install.omar.paris` | `install.omar.paris/buy` (V2) |
| P1 Provisioning | `install.omar.paris` | `install.omar.paris/<id>/p1-provisioning` (V2) |
| P1.5 Audit pré-bootstrap | `install.omar.paris` | `install.omar.paris/<id>/p1-5-audit` |
| P2 L0 stack | `install.omar.paris` | `install.omar.paris/<id>/p2-l0-stack` |
| P3 L1 baseline | `install.omar.paris` | `install.omar.paris/<id>/p3-l1-baseline` |
| **P3.5 Vault setup** | `install.omar.paris` | `install.omar.paris/<id>/p3-5-vault-setup` |
| P4 Activation | `install.omar.paris` → handoff Hub | `install.omar.paris/<id>/p4-activation` |
| P5 Maintenance | `hub.{client}.com` | `hub.{client}.com/parametres/maintenance` |
| P6 Export | `hub.{client}.com` | `hub.{client}.com/parametres/export` |

---

## Distinction critique

- **OmarTop** = doctrine (concept + `phases-spec.yaml` + `oa-doctor` + skill `omar-top-bootstrap`)
- **install.omar.paris** = implémentation concrète UI de OmarTop pour onboarding
- **hub.omar.paris** = implémentation concrète UI pour daily ops

OmarTop reste le **squelette commun** lu par les 2 sites Install et Hub.

---

## Roadmap install.omar.paris

| Version | Quoi |
|---|---|
| **V0.4** (cette semaine) | Phase P3.5 gravée doctrinalement |
| **V1** (semaine prochaine) | MVP wizard P2 → P3 → P3.5 → P4 (Maryse onboarding) |
| **V2** (post-cabinet validé) | Full e-commerce P0 + provisioning auto Hetzner P1 + handoff Hub automatique |
| **V3** | Standard onboarding tous clients OA |

---

## Voir aussi

- [Vision OmarTop](index.md)
- [Phases OmarTop — vue d'ensemble](../phases/index.md)
- [InstallWizard — spec install.omar.paris](../doctrine/install-wizard.md)
