# Vision OmarTop

> Source : [MANIFEST §1-7 — Renew OA V3 v1.2](https://omar.paris/doctrine/manifest)

OmarTop est la **doctrine procédurale et le référentiel de maturité** qui transforme un VPS vide en **VPS OA** : souverain, agentable, maintenable et réversible. Cette page résume la vision et les principes intangibles qui guident la méthode.

!!! note "Frontière Lab"
    `lab.omar.paris` est une surface fille d'OmarTop pour idées, POC, MVP et décisions. Le Lab ne définit pas la maturité globale : il applique OmarTop aux objets non stabilisés.

---

## 1. Vision en 1 phrase

> **`hub.omar.paris` est le backoffice unique d'`omar.paris` qui permet à un client OA d'acheter, configurer, utiliser, surveiller et quitter un agent IA souverain — chacun voit le VPS associé à son compte, sans support technique requis après le bootstrap.**

---

## 2. Promesse client (manifeste public)

> *« L'assistant IA qui prend en charge la paperasse et le marketing que les artisans n'ont pas le temps de gérer — chez vous, vos données restent vôtres, et vous pouvez partir avec elles en 24h si vous voulez. »*

Trois composants contractualisables :

- **L'assistant fait le travail** (capacités réelles, pas du chatbot)
- **Souveraineté** (données chez le client, OA n'y accède pas)
- **Réversibilité** (export 24h, format ouvert)

---

## 3. Les 7 principes fondateurs (intangibles)

1. **Self-Registration over Central Lists** — chaque capacité se déclare dans le registry du VPS, pas dans une liste centrale OA. `h-omar` scanne, ne dicte pas.
2. **Souveraineté client absolue** — secrets dans Vault age/sops, pas de données client en cache chez OA. JAMAIS d'export hors VPS sans demande écrite explicite du client.
3. **1 capacité = 3 documents** (`README` + `CONFIG` + `LOG`) — sauf Tools attachés à une App (`README` + `LOG`, `CONFIG` hérite du parent).
4. **8 statuts cycle de vie** : Backlog / Disponible / En qualification / Rodage / Active / Dégradé / Suspendu / Retiré.
5. **Code-first** — les docs sortent en parallèle du code, jamais avant. Pas de POC sur papier.
6. **DOD owner + test + preuve** — chaque livrable a un propriétaire nommé, un test passé, une preuve attachée.
7. **Travailler AVEC l'existant** — zéro fork conceptuel. On améliore le catalogue `oa-index` existant, on n'en crée pas un nouveau.

---

## 4. Les 3 audiences du Hub

| Audience | Quoi voir | Quoi faire | URL pattern |
|---|---|---|---|
| **Alex (admin)** | Tous les VPS sous gestion OA | Configurer, monitorer, exporter, facturer | `hub.omar.paris/admin/...` (V1) |
| **Client (ex : JAB, Maryse)** | Son VPS uniquement | Visualiser apps, statuts, logs ; demander ajout/retrait capacités ; exporter ses données | `hub.{client}.com/` |
| **Agent (API)** | Endpoints JSON de chaque VPS | Lire registry, écrire logs, déclencher actions (V1+) | `hub.{client}.com/api/...` |

---

## 5. Architecture des 3 produits OA

| Produit | Nature | Rôle |
|---|---|---|
| **OmarHub** | **App / OS local** | Cockpit du VPS courant : apps, capacités, santé, maintenance. Consomme OmarTop. |
| **OmarTop** | **Doctrine / maturité / standards** | Définit le VPS OA, les phases, les standards, les schémas et l'audit. |
| **OA Lab** | **Surface OmarTop** | Idées, POC, MVP, décisions et cycles projet. N'est pas la doctrine. |
| **QG** | **Supervision future** | Agrégation multi-VPS via résumés sûrs produits par les Hubs. |
| **OmarCatalogue** | **Méta-catalogue** | Range Apps + Skills + MCP + Tools + Bundles + Agents disponibles. |

Hiérarchie retenue : **OmarTop définit**, **Hub/Lab/QG consomment**, **Catalogue range**.

---

## 6. Les 7 phases bootstrap

| Phase | Nom | Sortie |
|---|---|---|
| **P0** | Commerce | Contrat signé + paiement |
| **P1** | Provisioning | VPS chez Hetzner/Pantheos provisionné |
| **P1.5** | Audit pré-bootstrap | Détection legacy + snapshot + GO/migration/STOP |
| **P2** | L0 stack | Caddy + Tailscale + Vault + Hermes Agent installés |
| **P3** | L1 baseline | 18 Apps L1 baseline installées |
| **P4** | Activation | Soul.md agent + 1 service client démo OK |
| **P5** | Maintenance | Backup quotidien + `oa-doctor` + healthchecks |
| **P6** | Export | rclone export 24h vers user |

Détail complet : voir [Phases OmarTop](../phases/index.md).

---

## 7. 6 critères de succès T+24h

Mesure binaire PASS/FAIL le dimanche matin. **4/6 minimum = sprint réussi. 6/6 = bonus V0.5.**

1. OmarHub accessible (`hub.omar.paris/`)
2. Page Apps fonctionnelle (130 entries, filtres, vues)
3. Page détail App (10 fiches L1 complètes)
4. OmarTop dry-run (`bootstrap-v0.sh --dry-run` retourne 0)
5. OmarCatalogue migré (5→8 statuts)
6. Zéro régression (Hermes, dashboard, Kanban, Agora, sops, Tailscale)

---

## Voir aussi

- [Piliers business + axe Personnel](piliers.md)
- [Sites publics OA (Hub / Install / Top)](sites-oa.md)
- [Doctrine Multi-Vault](../doctrine/multi-vault.md)
- [AppIntake — workflow audit](../doctrine/app-intake.md)
