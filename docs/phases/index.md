<!--
  AUTO-GENERATED — DO NOT EDIT MANUALLY
  Source : phases-spec.yaml
  Generator : scripts/build-from-yaml.py
  Re-run : /home/omar/.local/venv-mkdocs/bin/python scripts/build-from-yaml.py
-->


# Phases OmarTop

La methode OmarTop est structuree en **9 phases** couvrant **58 standards** au total (`42` obligatoires, `16` cibles).

> Source de verite : `/home/omar/23-Offre/actifs/omar-top/phases-spec.yaml` — version `0.1` (2026-06-02)

## Matrice

| Phase | Theme | Standards | Required | Target |
|-------|-------|-----------|----------|--------|
| 💼 **[P0](P0.md)** | Commerce | 4 | 2 | 2 |
| 🖥️ **[P1](P1.md)** | Provisioning | 5 | 4 | 1 |
| 🔍 **[P1.5](P1.5.md)** | Audit pre-bootstrap | 6 | 4 | 2 |
| 🧱 **[P2](P2.md)** | L0 stack | 9 | 6 | 3 |
| 📚 **[P3](P3.md)** | L1 baseline | 7 | 6 | 1 |
| 🔐 **[P3.5](P3.5.md)** | Vault setup | 10 | 8 | 2 |
| 🪽 **[P4](P4.md)** | Activation | 4 | 4 | 0 |
| 🩺 **[P5](P5.md)** | Maintenance | 7 | 3 | 4 |
| 📦 **[P6](P6.md)** | Export | 6 | 5 | 1 |
| | **Total** | **58** | **42** | **16** |

## Roadmap (phases envisagees V1+)

| Phase | Nom | Quand | Rationale |
|-------|-----|-------|-----------|
| `P7` | Audit conformite | `V1` | Audit RGPD + ISO 27001-like + AI Act. Devient critique des qu'on a >5 clients. |
| `P8` | Federation | `V2` | Permettre a une autre equipe d'operer son propre Hub OA (marque blanche). |

## Audit global

```bash
oa-doctor --check-all
```

L'outil [`oa-doctor`](../outils/index.md) audite chaque phase et calcule le pourcentage de configuration du VPS.

---

*Page auto-generee depuis `phases-spec.yaml`. Editer le YAML, pas ce fichier.*
