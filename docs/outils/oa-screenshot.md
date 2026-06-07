# `oa-screenshot`

Outil de capture d'écran pour les preuves attachées aux livrables OA (DOD owner + test + **preuve**).

---

## Synopsis

```bash
oa-screenshot <url> [--out <path>] [--full-page]
oa-screenshot --hub /apps/caddy --client jab
oa-screenshot --report <session-id>
```

---

## Cas d'usage

### Preuve d'un livrable

Le principe fondateur n°6 (cf [Vision](../vision/index.md#3-les-7-principes-fondateurs-intangibles)) exige : *« DOD owner + test + preuve »*. `oa-screenshot` produit la preuve visuelle attachée à une carte Kanban Hermes ou un post Agora.

```bash
oa-screenshot https://hub.bouboutou-avocats.com/apps/pennylane \
  --out preuves/jab-pennylane-active-$(date +%Y%m%d).png
```

### Capture page Hub

```bash
oa-screenshot --hub /apps/caddy --client jab
```

Résout automatiquement l'URL Tailnet correcte (`hub.bouboutou-avocats.com` pour JAB) et capture la page `/apps/caddy`.

### Capture batch (rapport)

```bash
oa-screenshot --report session-2026-06-03
```

Lit `~/.config/oa-screenshot/sessions/session-2026-06-03.yaml` qui liste N URLs et produit autant de captures dans `~/preuves/session-2026-06-03/`.

---

## Architecture

### Stack

- **Headless browser** : `chromium-headless-shell` (alternative légère à puppeteer/playwright)
- **Tailnet auth** : capture authentifiée via cookie de session ou magic link signé
- **Format sortie** : PNG full-page par défaut, JPEG sur option

### Format `session.yaml`

```yaml
session_id: session-2026-06-03
captures:
  - url: https://hub.bouboutou-avocats.com/apps/caddy
    name: jab-caddy-active
  - url: https://hub.bouboutou-avocats.com/parametres/vault
    name: jab-vault-multi-pattern
  - url: https://hub.bouboutou-avocats.com/apps/pennylane
    name: jab-pennylane-rodage
```

---

## Intégration

### Hermes Kanban

`oa-screenshot --kanban <card-id>` capture les preuves et les attache directement à la carte Hermes correspondante.

### Agora posts

Les posts Agora qui annoncent un livrable doivent inclure un lien vers la preuve attachée. Pattern :

```markdown
✅ Livrable : Page `/apps/pennylane` rendue + statut Rodage
📸 Preuve : ![capture](https://agora.omar.paris/uploads/jab-pennylane-rodage.png)
```

### Audit phase OmarTop

Certains standards `phases-spec.yaml` ont un champ `proof_capture: <url-pattern>` qui pointe vers la capture attendue. `oa-doctor` peut déclencher `oa-screenshot` automatiquement.

---

## Voir aussi

- [Outil `oa-doctor`](oa-doctor.md)
- [Outil `oa-app-intake`](oa-app-intake.md)
- [Sites publics OA](../vision/sites-oa.md)
