#!/usr/bin/env bash
#
# deploy.sh — Deploie omar-top-site sur top.omar.paris (Tailnet-only)
#
# Pourquoi sudo est necessaire :
#   - Caddy tourne en user `caddy` avec PrivateTmp=true (sandbox /tmp)
#   - Source /home/omar/ est en 750 omar:omar (caddy ne peut pas traverser)
#   - Cible /var/www/top-omar/ exige root pour mkdir + chown caddy:caddy
#
# Pre-requis :
#   - venv mkdocs : /home/omar/.local/venv-mkdocs/
#   - Stanza Caddyfile pour top.omar.paris (cf. scripts/caddy-stanza.txt)
#
# Usage (alex sur OA-master) :
#   sudo bash /home/omar/23-Offre/actifs/omar-top-site/scripts/deploy.sh
#
# Idempotent : peut etre reexecute pour mettre a jour.

set -euo pipefail

PROJECT_ROOT="/home/omar/23-Offre/actifs/omar-top-site"
VENV="/home/omar/.local/venv-mkdocs"
SOURCE="$PROJECT_ROOT/site"
TARGET="/var/www/top-omar"
CADDY_USER="caddy"
CADDY_GROUP="caddy"
CADDYFILE="/etc/caddy/Caddyfile"

if [[ $EUID -ne 0 ]]; then
  echo "ERROR: sudo bash $0" >&2
  exit 1
fi

echo "[1/5] Build MkDocs (strict) via venv"
# Build en tant qu'omar pour ne pas creer de fichiers root dans le repo
sudo -u omar bash -c "source '$VENV/bin/activate' && cd '$PROJECT_ROOT' && mkdocs build --strict --clean"

if [[ ! -d "$SOURCE" ]]; then
  echo "ERROR: build MkDocs a echoue, $SOURCE introuvable" >&2
  exit 1
fi

echo "[2/5] Creation $TARGET"
mkdir -p "$TARGET"

echo "[3/5] Copie site/ -> $TARGET (rsync --delete)"
rsync -a --delete "$SOURCE/" "$TARGET/"

echo "[4/5] Permissions (caddy:caddy + r-x)"
chown -R $CADDY_USER:$CADDY_GROUP "$TARGET"
find "$TARGET" -type d -exec chmod 755 {} \;
find "$TARGET" -type f -exec chmod 644 {} \;

echo "[5/5] Validation + reload Caddy"
caddy validate --config "$CADDYFILE" --adapter caddyfile 2>&1 | tail -1
systemctl reload caddy

echo ""
echo "=== TESTS ==="
sleep 2
echo -n "GET https://top.omar.paris/ : "
curl -sS -k -o /dev/null -w "HTTP %{http_code}\n" --resolve top.omar.paris:443:127.0.0.1 https://top.omar.paris/ -m 5 || true
echo -n "GET https://top.omar.paris/vision/ : "
curl -sS -k -o /dev/null -w "HTTP %{http_code}\n" --resolve top.omar.paris:443:127.0.0.1 https://top.omar.paris/vision/ -m 5 || true

echo ""
echo "Deploy OK. Visite https://top.omar.paris/ depuis Tailnet."
echo "Source files vivants dans $TARGET (caddy peut lire)"
echo "Pour iterer : modifie docs/ dans $PROJECT_ROOT puis re-run ce script."
