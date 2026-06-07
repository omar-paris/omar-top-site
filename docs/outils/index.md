# Outils OA

Outils opérationnels pour appliquer la doctrine OmarTop sur les VPS clients.

---

## Outils livrés

<div class="grid cards" markdown>

-   :material-stethoscope: **[`oa-doctor`](oa-doctor.md)**

    ---

    Audit d'un VPS contre les 9 phases × 58 standards. Compare l'état réel à `phases-spec.yaml`. Utilisé par `install.omar.paris` (wizard) + cron quotidien (P5 Maintenance).

-   :material-camera-outline: **[`oa-screenshot`](oa-screenshot.md)**

    ---

    Capture d'écran pour preuves attachées aux livrables OA (DOD = owner + test + **preuve**). Intégré Hermes Kanban + Agora posts.

-   :material-clipboard-search-outline: **[`oa-app-intake`](oa-app-intake.md)**

    ---

    Audit automatisé d'une nouvelle app candidate au catalogue. Implémente le workflow [AppIntake](../doctrine/app-intake.md) côté CCMA (étapes 2 + 3).

</div>

---

## Registry

Colonne vertébrale future du système : `/home/omar/registry/INDEX.md`.

Référence les clients, agents, services, secrets. Source unique consommée par `h-omar` + Hub + `oa-doctor`.

---

## Runbooks

Procédures opérationnelles par phase. À générer depuis `phases-spec.yaml` :

- Runbook P1.5 — Audit pré-bootstrap
- Runbook P3.5 — Vault setup
- Runbook P5 — Maintenance (backup + healthchecks)
- Runbook P6 — Export 24h

---

## Hermes

Plateforme de messagerie agents (Kanban + Agora). Skill `hermes-kanban` pour interaction depuis CC.

- Kanban : cartes de travail, statuts, owners
- Agora (Discourse) : forum équipe OA, threads RFC, votes, accepted answers

---

## Voir aussi

- [Phases OmarTop](../phases/index.md)
- [Doctrine OA](../doctrine/index.md)
