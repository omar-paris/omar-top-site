<!--
  AUTO-GENERATED — DO NOT EDIT MANUALLY
  Source : templates/L1-baseline.yaml
  Generator : scripts/build-from-yaml.py
  Re-run : /home/omar/.local/venv-mkdocs/bin/python scripts/build-from-yaml.py
-->


# Catalogue L1 — Baseline VPS OA

Toutes les apps **L1 obligatoires** que tout VPS OA (master ou client) doit avoir avant validation P3 ([L1 baseline](../phases/P3.md)).

## Vue d'ensemble

| Metrique | Valeur |
|----------|--------|
| Total apps L1 | **18** |
| Status Active obligatoires | **12** |
| Status Disponible (optionnels) | **6** |
| Piliers couverts | **9** |
| Version YAML | `0.2` (2026-06-03) |

## Toutes les apps L1

| Slug | Label | Pilier | Type | Status | Check |
|------|-------|--------|------|--------|-------|
| `oa-doctor` | oa-doctor (audit standards OmarTop) | `01` pilotage | `Tool` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `test -x /home/omar/23-Offre/actifs/omar-top/bin/oa-doctor` |
| `hermes-agent` | Hermes Agent (multi-tenant uv) | `03` agents | `App` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `command -v uv && test -d ~/.hermes/profiles` |
| `docker` | Docker (containers services tiers) | `04` infra-dev | `App` | <span style="background:#757575;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">DISPONIBLE</span> | `command -v docker && systemctl is-active --quiet docker` |
| `postgres` | PostgreSQL (DB transactionnelle) | `04` infra-dev | `App` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `systemctl is-active --quiet postgresql \|\| command -v psql` |
| `caddy` | Caddy (reverse proxy HTTPS + Tailnet-only) | `05` reseau | `App` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `systemctl is-active --quiet caddy` |
| `dnsmasq` | dnsmasq (split DNS *.omar.paris) | `05` reseau | `App` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `systemctl is-active --quiet dnsmasq && test -f /etc/dnsma...` |
| `tailscale` | Tailscale (mesh VPN) | `05` reseau | `App` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `command -v tailscale` |
| `rclone` | rclone (offsite S3/Backblaze/StorageBox) | `06` data | `Tool` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `command -v rclone` |
| `borg` | Borg backup chiffré | `07` securite | `Tool` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `command -v borg` |
| `ufw` | UFW + fail2ban (firewall + brute-force) | `07` securite | `App` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `command -v ufw && systemctl is-active --quiet fail2ban` |
| `vault-hashicorp` | Vault HashiCorp KV v2 (production) | `07` securite | `App` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `command -v vault && curl -sk http://127.0.0.1:8202/v1/sys...` |
| `vault-sops` | Vault age/sops (fichiers chiffrés locaux) | `07` securite | `Tool` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `command -v sops && command -v age && test -f ~/.config/so...` |
| `code-server` | code-server (VSCode browser) | `08` connaissance | `App` | <span style="background:#757575;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">DISPONIBLE</span> | `systemctl is-active --quiet code-server@omar` |
| `gh-cli` | GitHub CLI | `08` connaissance | `Tool` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `command -v gh && gh auth status` |
| `agora` | Agora (Discourse forum interne OA) | `10` communication | `App` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `curl -sk https://agora.omar.paris/srv/status -o /dev/null` |
| `agora-cli` | Agora CLI (Discourse forum) | `10` communication | `Tool` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `test -x /home/omar/omar-alex-vps/scripts/agora-post.sh` |
| `openwebui` | OpenWebUI (chat UI multi-LLM) | `10` communication | `App` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `curl -sk http://127.0.0.1:3000/ -o /dev/null` |
| `pennylane` | PennyLane (compta SaaS) | `12` finance | `Service` | <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span> | `test -f ~/.vault/pennylane/api-key 2>/dev/null \|\| vault...` |

## Par pilier

### Pilier 01 — pilotage

#### `oa-doctor` — oa-doctor (audit standards OmarTop) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `Tool`
- **Pourquoi** : Auto-audit phases-spec sur ce VPS (V0.2 P0 #2 — MVP en cours).

```bash
# Check de presence
test -x /home/omar/23-Offre/actifs/omar-top/bin/oa-doctor
```

### Pilier 03 — agents

#### `hermes-agent` — Hermes Agent (multi-tenant uv) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `App`
- **Pourquoi** : Pont WhatsApp/Telegram/Discord pour agents Soul.md (doctrine 4 artefacts).

```bash
# Check de presence
command -v uv && test -d ~/.hermes/profiles
```

### Pilier 04 — infra-dev

#### `postgres` — PostgreSQL (DB transactionnelle) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `App`
- **Pourquoi** : DB par défaut (Supabase déjà déployé VPS-OA, cf clarification Alex).

```bash
# Check de presence
systemctl is-active --quiet postgresql || command -v psql
```

#### `docker` — Docker (containers services tiers) <span style="background:#757575;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">DISPONIBLE</span>

- **Type** : `App`
- **Pourquoi** : Pour services tiers (Vault HashiCorp, OpenWebUI, etc.). Pas pour code OA (privilégier systemd-user).

```bash
# Check de presence
command -v docker && systemctl is-active --quiet docker
```

### Pilier 05 — reseau

#### `caddy` — Caddy (reverse proxy HTTPS + Tailnet-only) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `App`
- **Version min** : `2.7.0`
- **Pourquoi** : Souveraineté trafic HTTPS + cert Let's Encrypt auto. Snippet tailnet_only obligatoire.

```bash
# Check de presence
systemctl is-active --quiet caddy
```

#### `tailscale` — Tailscale (mesh VPN) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `App`
- **Version min** : `1.50.0`
- **Pourquoi** : Pont mesh entre VPS-OA et clients. Identité Tailnet = ACL strictes.

```bash
# Check de presence
command -v tailscale
```

#### `dnsmasq` — dnsmasq (split DNS *.omar.paris) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `App`
- **Pourquoi** : Split DNS Tailscale : route *.omar.paris via dnsmasq local.

```bash
# Check de presence
systemctl is-active --quiet dnsmasq && test -f /etc/dnsmasq.d/omar-paris.conf
```

### Pilier 06 — data

#### `rclone` — rclone (offsite S3/Backblaze/StorageBox) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `Tool`
- **Pourquoi** : Offsite backup target (StorageBox Hetzner standard).

```bash
# Check de presence
command -v rclone
```

### Pilier 07 — securite

#### `ufw` — UFW + fail2ban (firewall + brute-force) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `App`
- **Pourquoi** : Hardening minimum : ports 22/80/443 only + ban SSH brute-force.

```bash
# Check de presence
command -v ufw && systemctl is-active --quiet fail2ban
```

#### `vault-sops` — Vault age/sops (fichiers chiffrés locaux) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `Tool`
- **Pourquoi** : Pattern doctrine multi-vault V0.5 : sops local par VPS pour secrets.

```bash
# Check de presence
command -v sops && command -v age && test -f ~/.config/sops/age/keys.txt
```

#### `vault-hashicorp` — Vault HashiCorp KV v2 (production) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `App`
- **Pourquoi** : Doctrine A2 multi-vault (§12 MANIFEST) — 1 Vault par VPS.

```bash
# Check de presence
command -v vault && curl -sk http://127.0.0.1:8202/v1/sys/health
```

#### `borg` — Borg backup chiffré <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `Tool`
- **Pourquoi** : Backup quotidien chiffré (standard P5 maintenance).

```bash
# Check de presence
command -v borg
```

### Pilier 08 — connaissance

#### `gh-cli` — GitHub CLI <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `Tool`
- **Pourquoi** : Workflow git omar-paris/* (Hub, Top, Catalogue, …).

```bash
# Check de presence
command -v gh && gh auth status
```

#### `code-server` — code-server (VSCode browser) <span style="background:#757575;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">DISPONIBLE</span>

- **Type** : `App`
- **Pourquoi** : Édition distante Tailnet sans X11.

```bash
# Check de presence
systemctl is-active --quiet code-server@omar
```

### Pilier 10 — communication

#### `agora-cli` — Agora CLI (Discourse forum) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `Tool`
- **Pourquoi** : Discord-like forum doctrine 3-way validation (CCMA+CCSV+CCSA).

```bash
# Check de presence
test -x /home/omar/omar-alex-vps/scripts/agora-post.sh
```

#### `openwebui` — OpenWebUI (chat UI multi-LLM) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `App`
- **Pourquoi** : Interface client front pour agents Hermes.

```bash
# Check de presence
curl -sk http://127.0.0.1:3000/ -o /dev/null
```

#### `agora` — Agora (Discourse forum interne OA) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `App`
- **Pourquoi** : Forum 3-way doctrine OA (RFC, journal CC, coordination).

```bash
# Check de presence
curl -sk https://agora.omar.paris/srv/status -o /dev/null
```

### Pilier 12 — finance

#### `pennylane` — PennyLane (compta SaaS) <span style="background:#2e7d32;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75em;font-weight:600;">ACTIVE</span>

- **Type** : `Service`
- **Pourquoi** : Compta + facturation client (use case Édilia/JAB).

```bash
# Check de presence
test -f ~/.vault/pennylane/api-key 2>/dev/null || vault kv get -field=key secret/pennylane 2>/dev/null
```

---

*Source : `/home/omar/23-Offre/actifs/omar-top/templates/L1-baseline.yaml` — auteur `cc-manager (CCMA)` — doctrine `MANIFEST §7 (OmarTop) + §11 (Piliers V3) + §12 (Multi-Vault A2)`.*
