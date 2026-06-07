# Modèle VPS OA

> Décision : **OmarTop est la colonne vertébrale**. Le Lab est une surface fille
> pour idées, POC, MVP et décisions; il ne définit ni la doctrine ni la maturité.

## Définition

Un **VPS OA** est une machine souveraine, identifiable, auditée et opérable,
rattachée à une phase OmarTop et à des preuves vérifiables.

Un VPS OA conforme possède :

1. une identité stable (`id`, nom, rôle, environnement) ;
2. une origine technique (`provider`, région, OS) ;
3. un réseau explicite (IP publique, Tailnet, domaine racine, split DNS) ;
4. une phase OmarTop courante ;
5. une baseline technique ;
6. des capacités déclarées ;
7. des apps rattachées ;
8. des agents autorisés ;
9. une gestion de secrets ;
10. des backups et une observabilité minimale ;
11. une capacité d'export/réversibilité ;
12. des sources/preuves sans secrets.

## Cycle de vie

| Statut | Phase | Sortie attendue |
|---|---:|---|
| `raw` | P0 | Intention commerciale ou machine non préparée |
| `provisioned` | P1 | VPS créé, OS/réseau de base en place |
| `audited` | P1.5 | Inventaire et décision GO/MIGRATE/STOP tracés |
| `baseline_ready` | P3 | Baseline OA installée et registry initialisé |
| `activated` | P4 | Agent/client/service démo réellement actif |
| `maintained` | P5 | Backups, healthchecks et alertes actifs |
| `exportable` | P6 | Export chiffré/restauration/réversibilité prouvés |
| `retired` | hors cycle | VPS archivé ou décommissionné |

## Objets standards

| Objet | Sens | Consommateurs |
|---|---|---|
| `vps` | Machine racine, auditée par OmarTop | Hub, QG, agents |
| `capability` | Ce qu'un VPS sait faire de façon vérifiable | Hub, QG, Lab |
| `app` | Surface produit utilisable rattachée à un VPS | Hub, Lab, catalogue |
| `agent` | Identité agentique opérant dans un périmètre | Hub, Kanban, QG |
| `lab_item` | Idée/POC/MVP non stabilisé | Lab, Builder, Alex |
| `audit_result` | Sortie normalisée d'`oa-doctor` | Hub, QG, Kanban |

## Exemple VPS

```yaml
id: oa-master
name: VPS OA principal
provider: hetzner
region: nbg1
os: ubuntu-24.04
role: master
environment: production
lifecycle_status: baseline_ready
network:
  public_ip: 195.201.20.17
  tailnet_ip: 100.79.68.6
  domain_root: omar.paris
  split_dns: true
  caddy_tailnet_only: true
omartop:
  phase: P3.5
  score: null
  required_pass: null
  required_fail: null
  target_warn: null
```

Les champs `score`, `required_pass`, `required_fail` et `target_warn` restent à
`null` tant qu'un rapport `oa-doctor` normalisé n'a pas été produit. On ne devine
pas une maturité.

## Frontières des surfaces

| Surface | Rôle |
|---|---|
| `top.omar.paris` | Doctrine, phases, standards, modèles, runbooks |
| `hub.omar.paris` | OS local du VPS courant : apps, capacités, santé |
| `lab.omar.paris` | Petite surface OmarTop pour idées, POC, MVP, décisions |
| `qg.omar.paris` | Supervision future multi-VPS via résumés sûrs |

## Règles

1. Aucun objet OA officiel sans rattachement VPS ou décision explicite de rattachement futur.
2. Champs inconnus = `null`, jamais inventés.
3. Le Lab ne publie pas directement une app/capacité stable : il prépare une décision OmarTop.
4. Hub affiche l'état local; QG agrège plus tard des résumés sûrs.
5. `oa-doctor` doit devenir l'auditeur réel du modèle.

## Sources

- Modèle machine-readable : `/home/omar/23-Offre/actifs/omar-top/core-model.yaml`
- Schémas : `/home/omar/23-Offre/actifs/omar-top/schemas/`
- Exemples : `/home/omar/23-Offre/actifs/omar-top/examples/`
