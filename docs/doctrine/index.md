# Doctrine OA — Renew V3

Doctrine OmarTop / Renew OA V3 — source de vérité pour le modèle VPS OA, les phases, les contrats inter-produits, la souveraineté Vault, et les workflows opérationnels.

---

## Pages doctrinales

<div class="grid cards" markdown>

-   :material-server-network: **[Modèle VPS OA](modele-vps.md)**

    ---

    Définition officielle d'un VPS OA, cycle de vie, objets standards (`vps`, `app`, `capability`, `agent`, `lab_item`) et frontière Hub/Lab/QG.

-   :material-shield-lock-outline: **[Doctrine Multi-Vault (A2)](multi-vault.md)**

    ---

    1 Vault HashiCorp KV v2 par VPS. Hub OA agrège metadata read-only via Tailnet. Souveraineté absolue : les secrets clients ne quittent jamais leur VPS.

-   :material-clipboard-check-outline: **[AppIntake — workflow audit](app-intake.md)**

    ---

    Procédure standardisée pour intégrer une nouvelle app au catalogue OA. 5 étapes (Capture → Audit → Verdict → Décision → Fiche L1), grille 10 critères.

-   :material-wizard-hat: **[InstallWizard (install.omar.paris)](install-wizard.md)**

    ---

    Distinction `install.omar.paris` (onboarding one-time, P0 → P3.5) vs `hub.omar.paris` (daily ops, P4 → P6). Stack Flask + Tailwind + Alpine.

</div>

---

## Documents fondateurs

Les 3 fichiers racines de la doctrine vivent sur le filesystem OA et sont la **source de vérité** :

- **MANIFEST** — `/home/omar/11-Pilotage/Renew OA V3/MANIFEST.md`
- **CONTRACTS** — `/home/omar/11-Pilotage/Renew OA V3/CONTRACTS.md`
- **INDEX-DOCTRINE** — `/home/omar/11-Pilotage/Renew OA V3/INDEX-DOCTRINE.md`

Les pages de ce site **synthétisent** ces documents pour une consultation rapide sur Tailnet — la source canonique reste le filesystem.

---

## Constitution agents (R1 à R13)

Règles non-négociables pour les agents CC :

`/home/omar/3-Agents/agents-cc/_shared/constitution/regles-non-negociables.md`

---

## Pivot stratégique

Le pivot **V3** (juin 2026) réorganise OA autour d'une hiérarchie claire :

- **OmarTop** = doctrine / maturité / standards ; définit le VPS OA.
- **OmarHub** = OS local du VPS courant ; consomme OmarTop.
- **OA Lab** = petite surface OmarTop pour idées, POC, MVP, décisions.
- **QG** = supervision future multi-VPS via résumés sûrs.
- **OmarCatalogue** = méta-catalogue qui range Apps + Skills + MCP + Tools + Bundles + Agents.

Axes :

- **V0** : axe Business (piliers `01-13`) uniquement
- **V2** : axe Personnel (piliers `41-46+`) activé

Voir notes pivot dans `MEMORY.md` CCMA et [Vision OmarTop](../vision/index.md).
