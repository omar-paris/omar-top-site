# `oa-app-intake`

Script d'audit automatisé pour intégrer une nouvelle app au catalogue OA. Implémente le workflow [AppIntake](../doctrine/app-intake.md) côté CCMA (étape 2 + 3).

---

## Synopsis

```bash
oa-app-intake <url>
oa-app-intake <url> --output <path>
oa-app-intake <url> --persona avocat --axe business
```

---

## Cas d'usage

### Audit d'une URL d'app

```bash
oa-app-intake https://www.paperless-ngx.com/
```

Le script :

1. Fetch la page (et `/docs`, `/about`, `LICENSE` si dispos sur GitHub)
2. Parse les métadonnées (titre, description, langage, licence, stars, dernière release)
3. Évalue les **10 critères standardisés** (cf [grille](../doctrine/app-intake.md#grille-daudit-10-criteres-ccma))
4. Produit le rapport markdown pré-rempli
5. Propose un **verdict CTO brouillon** : GO / GO-CONDITIONNEL / NOGO

### Audit avec contexte persona

```bash
oa-app-intake https://github.com/excalidraw/excalidraw \
  --persona consultant --axe business
```

Adapte la priorité persona dans le rapport (`persona_priority` pondéré pour `consultant`).

### Audit axe personnel

```bash
oa-app-intake https://www.strava.com/ --axe personnel
```

Active le mapping piliers axe 4 (`41-46`) au lieu de l'axe business (`01-13`).

---

## Format du rapport produit

```markdown
# AppIntake — Paperless-ngx

## 1. Nom + URL
- Nom : Paperless-ngx
- URL : https://www.paperless-ngx.com/
- Repo : https://github.com/paperless-ngx/paperless-ngx

## 2. Licence
- GPL-3.0 (copyleft fort — distribution OK, modifications à publier)

## 3. Stack technique
- Backend : Python 3.x + Django
- Frontend : Angular
- DB : PostgreSQL / SQLite

## 4. Cible déploiement
- `deployment_target: vps-server`
- `install_method: docker`

## 5. Multi-user + auth
- Oui (Django auth + LDAP optionnel)

## 6. Storage
- Local (filesystem + DB)

## 7. Maturité
- ⭐ 17k stars GitHub
- Dernière release : v2.10.0 (mai 2026)
- Actif : oui (commits hebdo)

## 8. Compatibilité doctrine OA
- ✅ Souveraineté (self-hosted, no cloud lock-in)
- ✅ Offline-first (fonctionne air-gapped après install)

## 9. Persona cible
- `persona_priority`:
  - avocat: 1
  - consultant: 2
  - fleuriste: 4

## 10. Risques
- ⚠️ Stack lourd (Django + Angular + Postgres + Redis) — RAM ~1.5 Go
- ✅ RGPD : données restent sur VPS client
- ✅ Pas de vendor lock-in

---

## Verdict CTO brouillon
**GO-CONDITIONNEL**

Justification : stack lourd à valider sur VPS Hetzner CX22 (4 Go RAM partagé avec autres apps). Excellente fit doctrinale (souveraineté + offline-first + multi-user). Persona prioritaire = avocat (cabinet 5 collaborateurs minimum).

Conditions :
1. Valider performance sur VPS-JAB (test load avec 10k documents)
2. Définir politique de rétention (5 ans par défaut pour cabinet avocat)
```

---

## Architecture

### Implémentation

Script bash POC V0.3 (CCMA, 3 juin 2026) localisé dans `omar-top/bin/oa-app-intake`. Future réécriture Python pour parsing plus robuste (BeautifulSoup + GitHub API).

### Sources fetchées

- Page principale de l'URL fournie
- `<url>/docs` ou `/documentation` si dispo
- `<url>/about` ou `/team` si dispo
- GitHub API : stars, releases, languages, license (si repo GH détecté)

---

## Intégration

### Skill Claude Code

`using-app-intake` invocable par tous les CC (V0.6+). Wrapper qui appelle `oa-app-intake` et formate la réponse pour Alex.

### Workflow Hermes

`h-omar` peut recevoir une URL via Kanban → dispatche à CCMA → CCMA exécute `oa-app-intake` → résultat posté sur la carte.

### Validation CCSV

Après verdict GO d'Alex, CCSV produit la fiche L1 à partir du rapport en utilisant `omar-catalogue/templates/_INTAKE_TEMPLATE/`.

---

## Voir aussi

- [Doctrine AppIntake — workflow complet](../doctrine/app-intake.md)
- [Piliers — Business + Personnel](../vision/piliers.md)
- [Outil `oa-doctor`](oa-doctor.md)
- [Outil `oa-screenshot`](oa-screenshot.md)
