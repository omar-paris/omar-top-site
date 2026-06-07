# Doctrine Multi-Vault (A2)

> Source : [MANIFEST §12 — Renew OA V3 v1.2](https://omar.paris/doctrine/manifest)

**Architecture A2 : 1 Vault HashiCorp KV v2 par VPS.** Hub OA agrège metadata read-only via Tailnet. Pas de Vault central qui héberge les secrets des clients.

---

## Principe (décision Alex 3 juin 06h45)

> *« TRÈS TRÈS VITE JAB doit avoir SON propre Vault. »*

Souveraineté absolue : les secrets métier d'un client (PennyLane, Google OAuth, Outlook) ne quittent **jamais** le VPS du client (ni au repos, ni en transit).

---

## Topologie

```
┌─────────────────────────────┐         ┌──────────────────────────┐
│  VPS-OA-master              │ Tailnet │  VPS-JAB                 │
│  ─────────────────          │ HTTPS   │  ─────────────────       │
│  Vault HashiCorp :8202      │ ←─────→ │  Vault HashiCorp :8202   │
│  (48 secrets OA + cross-VPS)│   RO    │  (secrets JAB only)      │
│                             │         │                          │
│  hub.omar.paris/parametres/ │         │  hub.bouboutou-avocats.  │
│  vault                      │         │  com/parametres/vault    │
│  ↑ multi-vault selector     │         │  ↑ vault local           │
│    affiche les N vaults     │         │    + agrégation OA RO    │
└─────────────────────────────┘         └──────────────────────────┘
```

---

## Souveraineté

- Secrets métier client (PennyLane, Google OAuth, Outlook) = **sur VPS client uniquement**
- Hub OA ne stocke **jamais** les valeurs (metadata-only via Vault policy `hub-readonly`)
- Token Hub OA pour scan VPS distants = scope `metadata/list+read` uniquement, jamais `data/*`
- Lecture in-terminal jamais UI (cohérent oadmin pattern + secret pro)

---

## 2 patterns Vault coexistants

Recadrage Alex 20h50 (V0.5.3) : la doctrine A2 distingue **2 catégories de secrets** qui vivent dans **2 endroits différents**.

### Pattern 1 — Vault HashiCorp par VPS client (secrets métier)

- **Quoi** : tokens API SaaS clients (PennyLane, Google Workspace, Outlook, Stripe), credentials internes (DB, Hermes profils), certificats clients
- **Où** : Vault HashiCorp KV v2 installé sur **le VPS du client** lui-même (`100.x.x.x:8202` Tailnet local)
- **Pourquoi** : souveraineté absolue. Le secret ne quitte JAMAIS le VPS du client.
- **Accès Hub OA** : metadata-only via Tailnet RO avec policy `hub-readonly` scope `metadata/*`
- **Exemple** : `secret/pennylane/api-key` sur Vault VPS-JAB (jamais sur Vault OA)

### Pattern 2 — Vault OA-master `secret/clients/<id>/*` (secrets connexion)

- **Quoi** : authkeys Tailscale clients (provisioning + onboarding), bearer tokens *côté consommateur* OA (ex : token `omniscience-jab` que VPS-OA utilise pour appeler VPS-JAB), refresh tokens admin OA
- **Où** : Vault HashiCorp KV v2 OA-master sous préfixe `secret/clients/<id>/`
- **Pourquoi** : ces secrets sont *consommés par OA*, pas par le client. OA en a besoin pour orchestrer.
- **Multi-tenant** : préfixes `secret/clients/jab/*`, `secret/clients/maryse/*`, etc.
- **Exemple** : `secret/clients/jab/omniscience-bearer` (token que VPS-OA utilise pour appeler VPS-JAB en RO)

### Règle de tri (en cas de doute)

> *« Si OA disparaît demain, ce secret reste-t-il utile au client ? »*

- **OUI** → secret métier → Vault VPS client (Pattern 1)
- **NON** → secret connexion → Vault OA-master `secret/clients/<id>/` (Pattern 2)

---

## Pattern technique

1. **Chaque VPS expose son Vault** sur Tailnet (loopback localhost + Tailnet ACL stricte)
2. **Hub OA `vault-scanner.py`** (CCSA) lit `~/.config/oa-hub/vaults.yaml` qui liste les Vaults distants
3. **Pour chaque vault listé**, walk récursif via Tailnet → génère `vault.json` avec N vaults visibles

### Format `vaults.yaml`

```yaml
vaults:
  - slug: oa-master
    name: OA Vault Central
    addr: http://127.0.0.1:8202
    token_env: VAULT_TOKEN
  - slug: jab
    name: JAB Vault
    addr: http://100.x.y.z:8200
    token_ref: secret/oadmin/vault-tokens/jab-hub-readonly
```

---

## UI Hub V0.5.3

Page `/parametres/vault` affiche 2 labels distincts :

- `🏛 Vault local VPS-JAB` (métier client)
- `🌉 Vault OA-master secret/clients/jab/*` (connexion cross-VPS)

→ Évite confusion utilisateur (Alex, futurs admins clients).

---

## État au 3 juin 06h45 (V0.5.0)

- **VPS-OA-master** : Vault HashiCorp KV v2 installé sur `:8202` → 48 secrets (préfixes : `agent-keys/`, `agora/`, `clients/`, `cockpit/`, `connexions/`, `gog/`, `integrations/`, `llm/`, `mattermost/`, `oadmin/`, `openclaw/`)
- **VPS-OA dispersés** : 14 secrets identifiés en clair sur disque (audit gap, migration progressive vers Vault central)
- **VPS-JAB** : à installer (mission CCCU urgent — Vault Docker + 5 secrets initiaux pennylane/google/outlook/edilia/ssh)

---

## Anti-patterns

- Centraliser les secrets clients sur Vault OA-master (rupture souveraineté)
- Hub OA stocke ou cache valeurs secrets (pas même temporairement)
- Token de scan Hub avec permissions `data/*` (doit être `metadata/*` strict)
- Réplication cross-VPS automatique des secrets (chaque VPS est autonome)
- Lecture valeur via UI Hub (toujours `vault kv get` in-terminal)

---

## Évolution prévue

- **V0.6** : scan multi-VPS effectif (CCCU + CCSA), Hub OA affiche sélecteur Vault N entrées
- **V1.0** : helper `ssh-from-vault`, cron `h-omar` 5min auto-rescan
- **V2.0** : audit log 365j RGPD + rotation auto (R-054)

---

## Cross-référence opérationnelle

Doctrine détaillée opérationnelle (5 principes intangibles, V0.1 Vault HashiCorp, V0.2 SOPS, V1.0 3 options vault central, anti-patterns) gravée par CCSV dans :

`/home/omar/23-Offre/actifs/omar-catalogue/VAULT-DOCTRINE.md` (~280 lignes)

Cohérent avec MANIFEST §12 (architecture A2). Toute évolution doctrine Vault doit synchroniser **les 2 fichiers** (MANIFEST §12 = vision OA, VAULT-DOCTRINE.md = opérationnel CCSV).

---

## Voir aussi

- [Vision OmarTop](../vision/index.md)
- [Phase P3.5 — Vault setup](../phases/P3.5.md)
- [Sites publics OA](../vision/sites-oa.md)
