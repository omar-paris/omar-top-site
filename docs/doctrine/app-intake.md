# AppIntake — Workflow d'intégration d'une app au catalogue

> Source : [CONTRACTS §AppIntake — Renew OA V3 V0.8](https://omar.paris/doctrine/contracts)

Procédure standardisée pour intégrer une nouvelle application au catalogue OA. Évite le pattern « catalogue à l'arrache sans audit » (squelettes vides type Lot A V0.6).

---

## Workflow récurrent (5 étapes)

Alex découvre une app → audit CCMA → décision → fiche L1 publiée.

| Étape | Quoi | Owner | Effort |
|---|---|---|---|
| **1. Capture** | Alex transmet URL (article, GitHub, site officiel) à CCMA | Alex | 5 s |
| **2. Audit auto** | CCMA fetch + analyse 10 critères standardisés | CCMA | 5 min |
| **3. Verdict CTO** | CCMA recommande **GO / GO-CONDITIONNEL / NOGO** + justification | CCMA | 2 min |
| **4. Décision Alex** | Tranche sur la base du verdict | Alex | 10 s |
| **5. Production fiche L1** | CCSV produit `README.md` + `CONFIG.md` + `LOG.md` format strict | CCSV | 30 min |

---

## Grille d'audit — 10 critères CCMA

1. **Nom + URL officielle**
2. **Licence** (MIT / Apache / AGPL / proprio — impact distribution)
3. **Stack technique** (langage + framework)
4. **Cible déploiement** : `vps-server` / `desktop` / `mobile` / `saas-only` / `mixed`
5. **Multi-user + auth** (clé pour cabinets / équipes)
6. **Storage** : `local` / `cloud` / `hybride`
7. **Maturité** : stars + dernière release + actif / abandonné
8. **Compatibilité doctrine OA** : souveraineté + offline-first ?
9. **Persona cible** : laquelle des 5 personas OU axe personnel ?
10. **Risques** : RGPD / vendor lock-in / sécurité / licence copyleft

---

## Verdict CTO

CCMA produit un des 3 verdicts :

- **GO** — l'app passe tous les critères, intégration immédiate au catalogue
- **GO-CONDITIONNEL** — l'app passe avec réserves (ex : licence à clarifier, multi-user à valider, persona à confirmer)
- **NOGO** — l'app ne passe pas (souveraineté rompue, RGPD incompatible, vendor lock-in, abandonné)

Chaque verdict est accompagné d'une justification concise (1-3 lignes max).

---

## Outillage

### Script `oa-app-intake`

```bash
oa-app-intake <url>
```

Script bash qui :

1. Fetch l'URL fournie
2. Parse les métadonnées (titre, description, langage, licence, stars)
3. Produit le rapport markdown pré-rempli des 10 critères
4. Renvoie un brouillon de verdict CTO

→ Implémentation : `omar-top/bin/oa-app-intake` (POC V0.3 CCMA, 3 juin).

### Template fiche L1

`omar-catalogue/templates/_INTAKE_TEMPLATE/` — template fiche L1 pré-rempli des 10 champs (CCSV scope).

### Skill Claude Code

`using-app-intake` invocable par tous les CC (V0.6+).

---

## Schéma fiche L1 (extension V0.8)

Champs obligatoires liés au `DeploymentTarget` :

```yaml
deployment_target: vps-server         # vps-server | desktop | mobile | saas-only | mixed
client_devices_compatible:            # liste si deployment_target ∈ {desktop, mobile, mixed}
  - macos
  - windows
  - linux
  # - ios | android
install_method: docker                # apt | snap | docker | dmg | exe | appimage | homebrew | npm | pip | manual
```

### Filtre UI Hub catalogue

Page `/catalogue` propose un filtre `deployment_target` :

- **VPS Server** (Caddy, Vault, OpenWebUI, PennyLane...)
- **Client Device** (Scratch Notes, Cursor, Obsidian...)
- **Hybride** (apps avec serveur ET client)
- **SaaS** (Stripe, Google Calendar...)

`deployment_target` est **orthogonal** au pilier. Une brique Pilier 08-Connaissance peut être server (Paperless) ou desktop (Scratch).

---

## Anti-patterns

- Catalogue à l'arrache sans audit (= squelettes vides type Lot A V0.6)
- Skip étape verdict CTO (Alex submergé de décisions sans analyse)
- Production fiche L1 sans `validate-fiche.sh PASS`
- Mélange axes business + personnel dans même fiche

---

## Voir aussi

- [Vision OmarTop](../vision/index.md)
- [Piliers — Business + Personnel](../vision/piliers.md)
- [Catalogue L1 baseline](../catalogue/L1-baseline.md)
- [Outils — `oa-app-intake`](../outils/oa-app-intake.md)
