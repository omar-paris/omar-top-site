# `oa-doctor`

Audit d'un VPS client contre les **9 phases × 58 standards** OmarTop. Compare l'état réel aux exigences de `phases-spec.yaml`.

---

## Synopsis

```bash
oa-doctor --client <id> --phases <all|Px|Px,Py>
oa-doctor --check-phase Px [--strict]
oa-doctor --report markdown > rapport.md
```

---

## Cas d'usage

### Audit complet d'un client

```bash
oa-doctor --client jab --phases all
```

Parcourt les 9 phases (P0 → P6 + P1.5 + P3.5) et valide les 58 standards. Sortie console colorée + code retour binaire :

- `0` → tous les standards `required` passent
- `1` → au moins un standard `required` échoue
- `2` → un standard `target` (non bloquant) échoue (warning seulement)

### Check d'une phase précise (mode wizard)

```bash
oa-doctor --check-phase P3.5 --strict
```

Utilisé par `install.omar.paris` à chaque étape du wizard. En mode `--strict`, tous les standards `target` sont remontés comme erreurs.

### Génération d'un rapport audit

```bash
oa-doctor --client jab --phases all --report markdown > audits/jab-2026-06-03.md
```

Produit un rapport markdown listant pour chaque standard : statut PASS/FAIL/WARN + preuve attachée + remédiation proposée.

---

## Architecture

### Source de vérité

`phases-spec.yaml` (versionné dans `omar-top/`) liste les 9 phases et leurs 58 standards. Chaque standard contient :

- `id` (ex : `P2-CADDY-INSTALLED`)
- `phase` (P0, P1, ..., P6)
- `required` / `target` (bloquant ou recommandé)
- `check` (commande bash qui doit retourner exit 0)
- `why` (rationale doctrinal, optionnel)
- `fix` (remédiation suggérée, optionnel)

### Mécanisme de check

Pour chaque standard, `oa-doctor` exécute le `check` défini en YAML dans un sous-shell isolé :

```bash
bash -c "$check_command" >/dev/null 2>&1
```

Le code retour détermine le statut PASS / FAIL. La preuve attachée est le `stdout` capturé en mode verbose.

---

## Intégration

### Sites publics OA

- **install.omar.paris** : check à chaque étape du wizard (P1.5 → P3.5 → P4)
- **hub.omar.paris** : page `/parametres/maintenance` affiche le dernier rapport audit
- **top.omar.paris** : chaque page phase liste les standards et un bloc `oa-doctor --check-phase Px`

### Cron quotidien

```bash
# crontab user
0 3 * * * oa-doctor --client <auto> --phases all --report markdown > ~/audits/$(date +%Y-%m-%d).md
```

Le rapport quotidien alimente le healthcheck du VPS (`P5 Maintenance`).

### Hermes Kanban

`h-omar` lit le rapport quotidien et crée des cartes Kanban automatiques pour chaque standard FAIL.

---

## Voir aussi

- [Phases OmarTop — vue d'ensemble](../phases/index.md)
- [Phase P5 — Maintenance](../phases/P5.md)
- [Outil `oa-screenshot`](oa-screenshot.md)
- [Outil `oa-app-intake`](oa-app-intake.md)
