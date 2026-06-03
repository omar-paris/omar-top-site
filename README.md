# omar-top-site

Site MkDocs Material pour la doctrine **OmarTop** (top.omar.paris).

## Stack

- [MkDocs](https://www.mkdocs.org/) 1.6+
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 9.7+
- Plugins : `search`, `awesome-pages`, `mermaid2`

## Developpement local

```bash
# Activer le venv
source /home/omar/.local/venv-mkdocs/bin/activate

# Serveur de dev
cd /home/omar/23-Offre/actifs/omar-top-site
mkdocs serve

# Build statique
mkdocs build --strict
```

Le site est ensuite servi par **Caddy** depuis `site/` sur `top.omar.paris` (Tailnet-only).

## Sources

- Donnees : `/home/omar/23-Offre/actifs/omar-top/phases-spec.yaml`
- Doctrine : `/home/omar/11-Pilotage/Renew OA V3/`

## Repo futur

`omar-paris/omar-top-site` (GitHub).
