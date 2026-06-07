# omar-top-site

Site MkDocs Material pour la doctrine **OmarTop** — sert `top.omar.paris` (Tailnet-only).

## Description

Site doctrinal statique decrivant la methode OmarTop : 7 phases bootstrap VPS client, principes intangibles, piliers Business / Personnel, doctrine multi-vault, app-intake, install-wizard, et outils OA (`oa-doctor`, `oa-screenshot`, `oa-app-intake`).

Trois sections principales :

- **Vision** — promesse client, 7 principes intangibles, sites OA (Hub / Install / Top)
- **Doctrine** — multi-vault A2, app-intake, install-wizard
- **Outils** — oa-doctor, oa-screenshot, oa-app-intake

## Stack

- [MkDocs](https://www.mkdocs.org/) 1.6+
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 9.7+
- Plugins : `search`, `awesome-pages`, `mermaid2`
- venv : `/home/omar/.local/venv-mkdocs/`

## Quickstart developpement local

```bash
# Activer le venv
source /home/omar/.local/venv-mkdocs/bin/activate

# Serveur de dev (auto-reload, port 8000)
cd /home/omar/23-Offre/actifs/omar-top-site
mkdocs serve

# Acces : http://127.0.0.1:8000/
# (ou http://<host>:8000/ si serve --dev-addr 0.0.0.0:8000)

# Build statique (sortie : site/)
mkdocs build --strict --clean
```

## Procedure deploy prod

Le deploiement copie `site/` vers `/var/www/top-omar/` (owned `caddy:caddy`), puis recharge Caddy. Tout est idempotent et reexecutable.

### 1. Premiere fois : installer la stanza Caddyfile

Copier le contenu de `scripts/caddy-stanza.txt` a la fin de `/etc/caddy/Caddyfile`, puis :

```bash
sudo caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
sudo systemctl reload caddy
```

### 2. Build + deploy

```bash
sudo bash /home/omar/23-Offre/actifs/omar-top-site/scripts/deploy.sh
```

Le script fait :

1. `mkdocs build --strict` (en user `omar`, via venv)
2. `mkdir -p /var/www/top-omar/`
3. `rsync -a --delete site/ -> /var/www/top-omar/`
4. `chown -R caddy:caddy /var/www/top-omar/` + `755`/`644`
5. `caddy validate` + `systemctl reload caddy`
6. Smoke tests `curl` HTTP code

### 3. Iterer

Modifier `docs/`, puis re-run `sudo bash scripts/deploy.sh`.

## URL Tailnet

- **HTTPS Tailnet (cert interne Caddy)** : <https://top.omar.paris/>
- Accessible uniquement depuis le Tailnet OA (matcher `tailnet_only`, IPs `100.64.0.0/10` + `fd7a:115c:a1e0::/48`)
- Pas de DNS public : `top.omar.paris` doit etre resolu via MagicDNS Tailscale, ou via `--resolve top.omar.paris:443:<tailnet-ip>` cote client
- Quand le DNS public sera cree, retirer `tls internal` de la stanza Caddyfile pour basculer sur Let's Encrypt

## Sources

- Donnees phases : `/home/omar/23-Offre/actifs/omar-top/phases-spec.yaml`
- Doctrine source : `/home/omar/11-Pilotage/Renew OA V3/`
- MANIFEST OmarTop : `/home/omar/23-Offre/actifs/omar-top/MANIFEST.md`
- CONTRACTS OmarTop : `/home/omar/23-Offre/actifs/omar-top/CONTRACTS.md`

## Repo futur

`omar-paris/omar-top-site` (GitHub).
