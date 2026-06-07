#!/usr/bin/env python3
"""
build-from-yaml.py — Generateur de pages MkDocs depuis sources YAML OmarTop.

Sources :
- /home/omar/23-Offre/actifs/omar-top/phases-spec.yaml (9 phases, 58 standards)
- /home/omar/23-Offre/actifs/omar-top/templates/L1-baseline.yaml (18 apps L1)

Sorties :
- docs/phases/P0.md, P1.md, P1.5.md, P2.md, P3.md, P3.5.md, P4.md, P5.md, P6.md
- docs/catalogue/L1-baseline.md

Usage :
    /home/omar/.local/venv-mkdocs/bin/python scripts/build-from-yaml.py

Idempotent : peut etre lance autant de fois que voulu. Ecrase les pages generees.
Source de verite : YAML uniquement. NE PAS editer manuellement les .md generes.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

# Paths absolus
SITE_ROOT = Path("/home/omar/23-Offre/actifs/omar-top-site")
DOCS_DIR = SITE_ROOT / "docs"
PHASES_DIR = DOCS_DIR / "phases"
CATALOGUE_DIR = DOCS_DIR / "catalogue"

PHASES_YAML = Path("/home/omar/23-Offre/actifs/omar-top/phases-spec.yaml")
L1_YAML = Path("/home/omar/23-Offre/actifs/omar-top/templates/L1-baseline.yaml")

# Marker auto-genere (en commentaire HTML pour ne pas s'afficher)
AUTOGEN_HEADER = (
    "<!--\n"
    "  AUTO-GENERATED — DO NOT EDIT MANUALLY\n"
    "  Source : {source}\n"
    "  Generator : scripts/build-from-yaml.py\n"
    "  Re-run : /home/omar/.local/venv-mkdocs/bin/python scripts/build-from-yaml.py\n"
    "-->\n\n"
)


def slug_for_phase(phase_id: str) -> str:
    """P1.5 -> P1.5 (garde le point, MkDocs accepte les noms avec point)."""
    return phase_id


def render_level_badge(level: str) -> str:
    """Rend un badge Material pour le level d'un standard."""
    if level == "minimum_required":
        # Rouge = obligatoire
        return '<span style="background:#d32f2f;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">REQUIRED</span>'
    elif level == "target":
        # Bleu = cible (recommande)
        return '<span style="background:#1976d2;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">TARGET</span>'
    else:
        return f"`{level}`"


def render_status_badge(status: str) -> str:
    """Rend un badge pour le status_target d'une app L1."""
    if status == "Active":
        return '<span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>'
    elif status == "Disponible":
        return '<span style="background:#757575;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">DISPONIBLE</span>'
    else:
        return f"`{status}`"


def render_phase_page(phase: dict) -> str:
    """Genere le markdown d'une phase."""
    phase_id = phase["id"]
    name = phase["name"]
    icon = phase.get("icon", "")
    summary = phase.get("summary", "").strip()
    standards = phase.get("standards", [])

    n_required = sum(1 for s in standards if s.get("level") == "minimum_required")
    n_target = sum(1 for s in standards if s.get("level") == "target")

    lines = []
    lines.append(AUTOGEN_HEADER.format(source="phases-spec.yaml"))
    lines.append(f"# {icon} {phase_id} — {name}")
    lines.append("")
    lines.append(f"> {summary}")
    lines.append("")

    # Compteurs
    lines.append("## Vue d'ensemble")
    lines.append("")
    lines.append("| Metrique | Valeur |")
    lines.append("|----------|--------|")
    lines.append(f"| Identifiant phase | `{phase_id}` |")
    lines.append(f"| Nom | {name} |")
    lines.append(f"| Standards totaux | **{len(standards)}** |")
    lines.append(f"| Obligatoires (`minimum_required`) | **{n_required}** |")
    lines.append(f"| Cibles (`target`) | **{n_target}** |")
    lines.append("")

    # Tableau standards
    lines.append("## Standards")
    lines.append("")
    lines.append("| Cle | Label | Niveau | Version | Ajoute en |")
    lines.append("|-----|-------|--------|---------|-----------|")
    for std in standards:
        key = std.get("key", "")
        label = std.get("label", "").replace("|", "\\|")
        level = std.get("level", "")
        version = std.get("version", "")
        added_in = std.get("added_in", "—")
        lines.append(
            f"| `{key}` | {label} | {render_level_badge(level)} | `{version}` | `{added_in}` |"
        )
    lines.append("")

    # Detail des standards avec why
    standards_with_why = [s for s in standards if s.get("why")]
    if standards_with_why:
        lines.append("## Detail (rationale)")
        lines.append("")
        for std in standards_with_why:
            lines.append(f'??? info "`{std["key"]}` — {std.get("label", "")}"')
            lines.append(f'    **Pourquoi** : {std["why"]}')
            lines.append("")

    # Commande d'audit oa-doctor
    lines.append("## Audit")
    lines.append("")
    lines.append(
        f"Pour auditer cette phase sur un VPS client, executer :"
    )
    lines.append("")
    lines.append("```bash")
    lines.append(f"oa-doctor --check-phase {phase_id}")
    lines.append("```")
    lines.append("")
    lines.append(
        "L'outil parcourt chaque standard, execute son `check_present` "
        "et affiche le statut (OK / FAIL / MISSING)."
    )
    lines.append("")

    # Navigation
    lines.append("---")
    lines.append("")
    lines.append(f"*Source : `phases-spec.yaml` — version `{phase.get('version', '0.1')}` — voir [matrice complete](index.md).*")
    lines.append("")

    return "\n".join(lines)


def render_phases_index(spec: dict) -> str:
    """Genere docs/phases/index.md a partir de la matrice complete."""
    phases = spec.get("phases", [])
    total_standards = sum(len(p.get("standards", [])) for p in phases)
    total_required = sum(
        sum(1 for s in p.get("standards", []) if s.get("level") == "minimum_required")
        for p in phases
    )
    total_target = sum(
        sum(1 for s in p.get("standards", []) if s.get("level") == "target")
        for p in phases
    )

    lines = []
    lines.append(AUTOGEN_HEADER.format(source="phases-spec.yaml"))
    lines.append("# Phases OmarTop")
    lines.append("")
    lines.append(
        f"La methode OmarTop est structuree en **{len(phases)} phases** "
        f"couvrant **{total_standards} standards** au total "
        f"(`{total_required}` obligatoires, `{total_target}` cibles)."
    )
    lines.append("")
    lines.append(
        "> Source de verite : `/home/omar/23-Offre/actifs/omar-top/phases-spec.yaml` "
        f"— version `{spec.get('version', '0.1')}` ({spec.get('date', '?')})"
    )
    lines.append("")

    # Matrice
    lines.append("## Matrice")
    lines.append("")
    lines.append("| Phase | Theme | Standards | Required | Target |")
    lines.append("|-------|-------|-----------|----------|--------|")
    for p in phases:
        stds = p.get("standards", [])
        n_req = sum(1 for s in stds if s.get("level") == "minimum_required")
        n_tar = sum(1 for s in stds if s.get("level") == "target")
        icon = p.get("icon", "")
        link = f"[{p['id']}]({slug_for_phase(p['id'])}.md)"
        lines.append(
            f"| {icon} **{link}** | {p['name']} | {len(stds)} | {n_req} | {n_tar} |"
        )
    lines.append(f"| | **Total** | **{total_standards}** | **{total_required}** | **{total_target}** |")
    lines.append("")

    # Roadmap
    roadmap = spec.get("roadmap_extensions", [])
    if roadmap:
        lines.append("## Roadmap (phases envisagees V1+)")
        lines.append("")
        lines.append("| Phase | Nom | Quand | Rationale |")
        lines.append("|-------|-----|-------|-----------|")
        for r in roadmap:
            lines.append(
                f"| `{r['id']}` | {r['name']} | `{r['when']}` | {r.get('rationale', '')} |"
            )
        lines.append("")

    # Audit
    lines.append("## Audit global")
    lines.append("")
    lines.append("```bash")
    lines.append("oa-doctor --check-all")
    lines.append("```")
    lines.append("")
    lines.append(
        "L'outil [`oa-doctor`](../outils/index.md) audite chaque phase et calcule "
        "le pourcentage de configuration du VPS."
    )
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("*Page auto-generee depuis `phases-spec.yaml`. Editer le YAML, pas ce fichier.*")
    lines.append("")

    return "\n".join(lines)


def render_l1_baseline_page(data: dict) -> str:
    """Genere docs/catalogue/L1-baseline.md."""
    apps = data.get("apps", [])
    total = data.get("total_count", len(apps))
    mandatory = data.get("mandatory_status_active", 0)
    optional = data.get("optional_disponible", 0)

    # Group by pilier
    piliers: dict[str, list] = {}
    for app in apps:
        pilier_key = f"{app.get('pilier_number', '??')} — {app.get('pilier', 'inconnu')}"
        piliers.setdefault(pilier_key, []).append(app)

    lines = []
    lines.append(AUTOGEN_HEADER.format(source="templates/L1-baseline.yaml"))
    lines.append("# Catalogue L1 — Baseline VPS OA")
    lines.append("")
    lines.append(
        f"Toutes les apps **L1 obligatoires** que tout VPS OA (master ou client) "
        f"doit avoir avant validation P3 ([L1 baseline](../phases/P3.md))."
    )
    lines.append("")
    lines.append("## Vue d'ensemble")
    lines.append("")
    lines.append("| Metrique | Valeur |")
    lines.append("|----------|--------|")
    lines.append(f"| Total apps L1 | **{total}** |")
    lines.append(f"| Status Active obligatoires | **{mandatory}** |")
    lines.append(f"| Status Disponible (optionnels) | **{optional}** |")
    lines.append(f"| Piliers couverts | **{len(piliers)}** |")
    lines.append(f"| Version YAML | `{data.get('version', '0.1')}` ({data.get('date', '?')}) |")
    lines.append("")

    # Table globale
    lines.append("## Toutes les apps L1")
    lines.append("")
    lines.append("| Slug | Label | Pilier | Type | Status | Check |")
    lines.append("|------|-------|--------|------|--------|-------|")
    for app in sorted(apps, key=lambda a: (a.get("pilier_number", "99"), a.get("slug", ""))):
        slug = app.get("slug", "")
        label = app.get("label", "").replace("|", "\\|")
        pilier = f"`{app.get('pilier_number', '??')}` {app.get('pilier', '')}"
        type_cap = app.get("type_capacite", "")
        status = render_status_badge(app.get("status_target", ""))
        check = app.get("check_present", "").replace("|", "\\|")
        # Tronquer check si trop long pour la table
        check_short = check if len(check) < 60 else check[:57] + "..."
        lines.append(f"| `{slug}` | {label} | {pilier} | `{type_cap}` | {status} | `{check_short}` |")
    lines.append("")

    # Detail par pilier
    lines.append("## Par pilier")
    lines.append("")
    for pilier_key in sorted(piliers.keys()):
        pilier_apps = piliers[pilier_key]
        lines.append(f"### Pilier {pilier_key}")
        lines.append("")
        for app in pilier_apps:
            slug = app.get("slug", "")
            label = app.get("label", "")
            status = render_status_badge(app.get("status_target", ""))
            type_cap = app.get("type_capacite", "")
            why = app.get("why", "")
            check = app.get("check_present", "")
            version_min = app.get("check_version_min", "")
            lines.append(f"#### `{slug}` — {label} {status}")
            lines.append("")
            lines.append(f"- **Type** : `{type_cap}`")
            if version_min:
                lines.append(f"- **Version min** : `{version_min}`")
            lines.append(f"- **Pourquoi** : {why}")
            lines.append("")
            lines.append("```bash")
            lines.append(f"# Check de presence")
            lines.append(check)
            lines.append("```")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        f"*Source : `{L1_YAML}` — auteur `{data.get('auteur', '?')}` — "
        f"doctrine `{data.get('doctrine_ref', '?')}`.*"
    )
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    # Validation
    if not PHASES_YAML.exists():
        print(f"ERROR: phases YAML introuvable : {PHASES_YAML}", file=sys.stderr)
        return 1
    if not L1_YAML.exists():
        print(f"ERROR: L1 baseline YAML introuvable : {L1_YAML}", file=sys.stderr)
        return 1

    # Load
    spec = yaml.safe_load(PHASES_YAML.read_text(encoding="utf-8"))
    l1_data = yaml.safe_load(L1_YAML.read_text(encoding="utf-8"))

    # Mkdir
    PHASES_DIR.mkdir(parents=True, exist_ok=True)
    CATALOGUE_DIR.mkdir(parents=True, exist_ok=True)

    generated = []

    # Pages par phase
    for phase in spec.get("phases", []):
        slug = slug_for_phase(phase["id"])
        out_path = PHASES_DIR / f"{slug}.md"
        out_path.write_text(render_phase_page(phase), encoding="utf-8")
        generated.append(out_path)

    # Index phases (regenere depuis YAML)
    index_path = PHASES_DIR / "index.md"
    index_path.write_text(render_phases_index(spec), encoding="utf-8")
    generated.append(index_path)

    # Catalogue L1
    l1_path = CATALOGUE_DIR / "L1-baseline.md"
    l1_path.write_text(render_l1_baseline_page(l1_data), encoding="utf-8")
    generated.append(l1_path)

    # Report
    print(f"Genere {len(generated)} fichiers :")
    for p in generated:
        rel = p.relative_to(SITE_ROOT)
        print(f"  - {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
