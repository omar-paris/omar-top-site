# Piliers — Axe Business + Axe Personnel

> Source : [MANIFEST §11 + §11.bis — Renew OA V3 v1.2](https://omar.paris/doctrine/manifest)

OA structure ses capacités en **axes** (1 axe = 1 ensemble de besoins cohérents). Chaque axe se décompose en **piliers** (1 pilier = 1 domaine métier transversal). Chaque pilier rassemble ~10 briques L1.

**Convention numérotation par axe** :

- Axe 1 (Business clients) → piliers `01-13`
- Axe 2 (réservé) → piliers `2x`
- Axe 3 (réservé) → piliers `3x`
- Axe 4 (Personnel Alex + recos perso clients) → piliers `4x`

---

## Axe 1 — Business (13 piliers)

Mapping retenu après inspection des 130 briques réelles `omar-catalogue/apps/_stub/` par CCSV (Lot A V0.6, 3 juin 2026).

| # | Nom V3 | Exemple brique L1 | Type capacité dominant |
|---|---|---|---|
| 01 | **Pilotage** | Agenda & calendrier, Kanban, Journal, Cockpit | App / Skill |
| 02 | **Offre** | Catalogue offres, Devis, CRM léger | App / Bundle |
| 03 | **Agents** | Agent personnel, Annuaire agents, Sandbox prompts | Agent / Skill |
| 04 | **Infra-Dev** | Postgres, CI/CD Forgejo, code-server, Containers Docker, Monitoring Beszel | App / Tool |
| 05 | **Réseau** | DNS, Certs TLS, RustDesk, Inventaire parc, Tailscale | App / Tool |
| 06 | **Data** | n8n, Metabase, DuckDB warehouse, Postgres relational | App / Service |
| 07 | **Sécurité** | ClamAV, Audit sec, Charte, CrowdSec, PRA-PCA | App / Tool |
| 08 | **Connaissance** | FAQ, Paperless, Glossaire, Templates, Onboarding | App / Service |
| 09 | **Marketing** | Plausible, Blog, CRM prospects, Listmonk, Parrainage | App / Skill |
| 10 | **Communication** | Accueil / standard, Téléphonie, Messagerie | App / Connexion |
| 11 | **Équipe/RH** | Annuaire collaborateurs, Onboarding RH, Congés | App / Service |
| 12 | **Finance** | Budget & prévisionnel, Compta, Facturation, Banque | App / Connexion |
| 13 | **Legal/Conformité** | Assurances, RGPD, Contrats, Certifications | App / Service |

### Slugs canoniques (filtres UI Hub)

`catalogView` (CCSA `app.js`) propose le filtre `pilier` avec ces 13 valeurs en kebab-case :

```
pilotage, offre, agents, infra-dev, reseau, data, securite,
connaissance, marketing, communication, equipe-rh, finance, legal-conformite
```

### Légende personas

Personas standards utilisés dans `persona_priority` (priorité 1-5) :

- `boulanger` / `avocat` / `consultant` / `fleuriste` / `startuppeur`

---

## Axe 4 — Personnel (6 piliers extensibles)

Activé V0.8 (3 juin 2026 soir) pour permettre catalogue d'apps personnelles (cas ShadowBroker). Format préfixe **2 digits** cohérent avec axe 1.

| # | Nom V3 | Exemple brique L1 |
|---|---|---|
| **41** | **Bien-être** | Strava, MyFitnessPal, méditation, sommeil |
| **42** | **Famille** | Apps kids, partage photos, planning famille |
| **43** | **Social** | Réseaux sociaux pro/perso, communautés |
| **44** | **Passions** | ShadowBroker (OSINT), hobby tracking, sports spectacle |
| **45** | **Éducation** | Apprentissage, veille, podcasts, MOOC |
| **46** | **Jeux** | Gaming, plateformes, communautés |

→ **Extensible** : 47, 48, 49+ pour piliers futurs axe 4 (Alex décide quand besoin).

### Champ obligatoire `axe`

```yaml
axe: business        # business | personnel | mixed
```

Si `axe: personnel`, alors `pilier` doit pointer vers un pilier axe 4 (`41-46+`).

### UI Hub catalogue (CCSA V0.6)

Toggle `axe` dans filtres galerie : **Business** / **Personnel** / **Tous**. Couleurs différenciées (business = bleu, personnel = ambre).

---

## Anti-patterns

- Renommer les piliers sans en informer CCSV (source unique catalogue).
- Créer un 14e pilier axe 1 ou agréger 2 piliers (cohérence 130 briques = 13 × 10 cible).
- Mapper un mot du pilier MANIFEST OA différemment dans MANIFEST OmarCatalogue (alignement strict requis).
- Mélanger axes business + personnel dans la même fiche L1.

---

## Voir aussi

- [Vision OmarTop](index.md)
- [Catalogue L1 baseline (18 apps × 9 piliers)](../catalogue/L1-baseline.md)
- [Doctrine AppIntake — workflow audit](../doctrine/app-intake.md)
