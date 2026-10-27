Voici le programme complet en format Markdown détaillé, prêt à être copié dans un fichier ou une application de prise de notes.

---
# 🗺️ ROADMAP DATA ENGINEERING & DEVOPS GCP + AI DEV TOOLS

> **Format :** Lundi, Mardi, Samedi, Dimanche uniquement
> **Rythme :** Cours d'abord → Projet ensuite
> **Ordre :** AI Dev Tools avant LLM (productivité d'abord, construction ensuite)

---

## 📅 PLANNING GLOBAL

| Phase | Contenu | Semaines | Durée | Période estimée |
|-------|---------|----------|-------|-----------------|
| 0 | PySpark Fondations | 1-8 | 2 mois | Nov-Déc 2026 |
| 1A | GCP Core + IAM | 9-11 | 1.5 mois | Jan 2027 |
| 1B | Terraform | 12-16 | 2.5 mois | Fév-Mar 2027 |
| 1C | Docker + CI/CD | 17-20 | 2 mois | Avr-Mai 2027 |
| 2 | BigQuery + Dataform + Viz | 21-27 | 2 mois | Mai-Juin 2027 |
| 3A | Archi Data Lakes/Warehouses | 28-31 | 1 mois | Juil 2027 |
| 3B | Batch Spark Serverless | 32-37 | 1.5 mois | Août 2027 |
| 3C | **Capstone Data Engineering** | 38-50 | **3 mois** | Sept-Nov 2027 |
| 4 | **AI Dev Tools Zoomcamp** | 51-56 | 1.5 mois | Déc 2027-Jan 2028 |
| 5 | **LLM Zoomcamp** | 57-68 | 3 mois | Fév-Avr 2028 |

**Total : ~68 semaines ≈ 16-17 mois**

---

# PHASE 0 : PYSPARK FONDATIONS (2 MOIS)

## 🎓 Période Cours — Semaines 1-3

### Semaine 1

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | Didacticiel DataFrames Apache Spark | 3-4h | Databricks Documentation officielle. Premières transformations, import CSV depuis interface Workspace |
| **Mardi** | DataCamp — Introduction to PySpark | 3-4h | Parcours : Associate Data Engineer in Databricks |

### Semaine 2

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | DataCamp — Introduction to PySpark (suite) | 3-4h | Fin du module si nécessaire |
| **Mardi** | DataCamp — Introduction to Spark SQL in Python | 3-4h | Même parcours DataCamp |
| **Samedi** | DataCamp — Introduction to Spark SQL in Python (suite) + exercices | 4-5h | Pratique intensive Databricks Free Edition |
| **Dimanche** | DataCamp — Data Transformation with Spark SQL in Databricks | 4-5h | Début du module |

### Semaine 3

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | DataCamp — Data Transformation with Spark SQL in Databricks (suite) | 3-4h | |
| **Mardi** | DataCamp — Cleaning Data with PySpark | 3-4h | Cours individuel DataCamp |
| **Samedi** | Révision + pratique libre Databricks | 4-5h | Reproduire tous les exercices dans vrai Workspace |
| **Dimanche** | Révision + consolidation | 4-5h | Identifier points faibles, revenir dessus |

### 📚 Ressources complètes Phase 0 Cours

| Ressource | Type | URL | Notes |
|-----------|------|-----|-------|
| Didacticiel DataFrames Apache Spark | Documentation officielle | https://docs.databricks.com | Gratuit, Databricks Free Edition |
| Associate Data Engineer in Databricks | Parcours DataCamp | https://datacamp.com | Payant, certif optionnelle |
| Introduction to PySpark | Module DataCamp | Inclus dans parcours | |
| Introduction to Spark SQL in Python | Module DataCamp | Inclus dans parcours | |
| Data Transformation with Spark SQL in Databricks | Module DataCamp | Inclus dans parcours | |
| Cleaning Data with PySpark | Cours DataCamp individuel | https://datacamp.com | Inclus ou à l'unité |

> ⚠️ **Pratique obligatoire :** Databricks Free Edition pour tous les exercices. Les labs DataCamp ne remplacent pas la manipulation dans un vrai Workspace.

---

## 🔧 Période Projet — Semaines 4-8

### Objectif
Pipeline ETL batch complet avec dataset public, démontrant maîtrise des DataFrames, Spark SQL, cleaning, transformations complexes.

### Semaine 4 — Ingestion et Exploration

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi** | Choix dataset public + ingestion dans DBFS/GCS/S3 | Notebook 01_ingestion.ipynb |
| **Mardi** | Exploration initiale : schéma, statistiques, profiling | Notebook 02_exploration.ipynb |

### Semaine 5 — Cleaning et Transformations de base

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Samedi** | Cleaning : nulls, doublons, types incohérents, outliers | Notebook 03_cleaning.ipynb |
| **Dimanche** | Transformations : colonnes dérivées, dates, catégories | Notebook 04_transformations.ipynb |

### Semaine 6 — Transformations Avancées

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi** | Jointures entre datasets | Notebook 05_jointures.ipynb |
| **Mardi** | Agrégations groupBy, fenêtres temporelles | Notebook 06_aggregations.ipynb |

### Semaine 7 — Optimisation et Tests

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Samedi** | Partitionnement, caching, optimisation requêtes | Notebook 07_optimisation.ipynb |
| **Dimanche** | Tests unitaires Spark, validation qualité | tests/ + Notebook 08_tests.ipynb |

### Semaine 8 — Finalisation

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi** | Documentation README, architecture | README.md |
| **Mardi** | Git push final, review code | Repo GitHub complet |
| **Samedi** | Présentation orale (si possible) ou enregistrée | demo.md ou vidéo |
| **Dimanche** | Buffer / corrections dernière minute | Release v1.0 |

### 📁 Structure repo attendue

```
projet-phase0-pyspark/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/           # données brutes
│   └── processed/     # données finales
├── notebooks/
│   ├── 01_ingestion.ipynb
│   ├── 02_exploration.ipynb
│   ├── 03_cleaning.ipynb
│   ├── 04_transformations.ipynb
│   ├── 05_jointures.ipynb
│   ├── 06_aggregations.ipynb
│   ├── 07_optimisation.ipynb
│   └── 08_tests.ipynb
├── src/               # scripts Python modulaires
├── tests/             # tests unitaires
└── docs/              # documentation technique
```

---

# PHASE 1A : GCP CORE + IAM (1.5 MOIS)

## 🎓 Période Cours — Semaines 9-10

### Semaine 9

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | Google Cloud Fundamentals: Core Infrastructure | 3-4h | Google Cloud Skills Boost. Concepts GCP, infrastructure, services stockage |
| **Mardi** | Google Cloud Fundamentals: Core Infrastructure (suite) | 3-4h | Fin du cours |
| **Samedi** | Pratique console GCP : créer projet, naviguer services | 4-5h | Compte GCP avec crédits free tier |
| **Dimanche** | Révision quiz, documentation complémentaire | 4-5h | |

### Semaine 10

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | Essential Google Cloud Infrastructure: Core Services | 3-4h | IAM granulaire, stockage avancé, facturation, surveillance |
| **Mardi** | Essential Google Cloud Infrastructure: Core Services (suite) | 3-4h | Fin du cours |
| **Samedi** | Pratique IAM : comptes de service, rôles custom, policies | 4-5h | Console + gcloud CLI |
| **Dimanche** | Révision + quiz final | 4-5h | |

### 📚 Ressources complètes Phase 1A Cours

| Ressource | Type | URL | Langue | Durée |
|-----------|------|-----|--------|-------|
| Google Cloud Fundamentals: Core Infrastructure | Cours Skills Boost | https://www.cloudskillsboost.google/course_templates/60?locale=fr | 🇫🇷 Français | ~6h30 |
| Essential Google Cloud Infrastructure: Core Services | Cours Skills Boost | https://www.cloudskillsboost.google/course_templates/49?locale=fr | 🇫🇷 Français | ~6h |
| Documentation IAM officielle | Référence | https://cloud.google.com/iam/docs | 🇫🇷/🇬🇧 | Continue |
| Documentation Cloud Billing | Référence | https://cloud.google.com/billing/docs | 🇫🇷/🇬🇧 | Continue |

---

## 🔧 Période Projet — Semaine 11

| Jour | Tâche | Commandes/Actions clés |
|------|-------|------------------------|
| **Lundi** | Créer projet GCP dédié apprentissage | `gcloud projects create` |
| **Mardi** | Configurer IAM granulaire | Créer comptes de service par usage, rôles minimaux |
| **Samedi** | Activer APIs : BigQuery, Storage, Dataproc, Compute | Console ou `gcloud services enable` |
| **Dimanche** | Budget + alertes + audit logs | Cloud Billing, Cloud Audit Logs, monitoring basique |

### Livrables
- [ ] Projet GCP fonctionnel avec naming convention
- [ ] Document IAM : qui a accès à quoi
- [ ] Budget configuré avec alertes 50%/80%/100%
- [ ] Audit logs activés et consultables

---

# PHASE 1B : TERRAFORM (2.5 MOIS)

## 🎓 Période Cours — Semaines 12-14

### Semaine 12

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | Getting Started with Terraform for Google Cloud | 3-4h | Google Cloud Skills Boost. Init, plan, apply, state |
| **Mardi** | Getting Started with Terraform for Google Cloud (suite) | 3-4h | Variables, outputs, ressources de base |
| **Samedi** | Pratique : premier bucket GCS avec Terraform | 4-5h | Local + remote state test |
| **Dimanche** | Révision + exercices variables/outputs | 4-5h | |

### Semaine 13

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | Build Infrastructure with Terraform on Google Cloud | 3-4h | Parcours Cloud Engineer. Modules, remote state |
| **Mardi** | Build Infrastructure with Terraform on Google Cloud (suite) | 3-4h | |
| **Samedi** | Pratique : module réutilisable VPC | 4-5h | Networking GCP |
| **Dimanche** | Pratique : module réutilisable GCS | 4-5h | Lifecycle, versioning |

### Semaine 14

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | Infrastructure as Code avec Terraform — atelier | 3-4h | Google Cloud Skills Boost. Atelier pratique en français |
| **Mardi** | Atelier (suite) + modules avancés | 3-4h | |
| **Samedi** | Pratique : remote state GCS backend, locking | 4-5h | Production-ready |
| **Dimanche** | Révision globale + sécurité state | 4-5h | ⛔ Ne jamais commiter .tfstate |

### 📚 Ressources complètes Phase 1B Cours

| Ressource | Type | URL | Langue | Durée |
|-----------|------|-----|--------|-------|
| Getting Started with Terraform for Google Cloud | Cours Skills Boost | https://www.cloudskillsboost.google/course_templates/443 | 🇬🇧 | ~6h30 |
| Build Infrastructure with Terraform on Google Cloud | Cours Skills Boost | https://www.cloudskillsboost.google/paths/20/course_templates/636 | 🇬🇧 | ~6h |
| Infrastructure as Code avec Terraform — atelier | Atelier Skills Boost | https://www.cloudskillsboost.google/focuses/15842?locale=fr | 🇫🇷 Français | ~2h |
| Documentation Terraform GCP provider | Référence | https://registry.terraform.io/providers/hashicorp/google/latest/docs | 🇬🇧 | Continue |

### ⚠️ Règles de sécurité absolues

```
☐ terraform init / plan / apply / destroy maîtrisés
☐ Variables dans terraform.tfvars (non versionné)
☐ Outputs pour ressources partagées
☐ Remote state GCS avec versioning
☐ .tfstate et .tfstate.backup dans .gitignore
☐ Secrets jamais dans le code → Secret Manager
```

---

## 🔧 Période Projet — Semaines 15-16

### Architecture cible

```
modules/
├── vpc/                    # Réseau + sous-réseaux
├── gcs_bucket/             # Bucket avec lifecycle
├── bigquery_dataset/       # Dataset + tables de base
└── service_account/        # Compte + IAM binding
```

### Semaine 15

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi** | Développement module VPC | modules/vpc/ |
| **Mardi** | Développement module GCS | modules/gcs_bucket/ |
| **Samedi** | Développement module BigQuery | modules/bigquery_dataset/ |
| **Dimanche** | Développement module Service Account | modules/service_account/ |

### Semaine 16

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi** | Assemblage root module, remote state GCS | main.tf, backend.tf |
| **Mardi** | Tests terraform validate, plan, fmt | CI-ready |
| **Samedi** | Documentation, exemples d'usage | README.md, examples/ |
| **Dimanche** | Git push, review, release module v1.0 | Repo public/privé |

---

# PHASE 1C : DOCKER + CI/CD (2 MOIS)

## 🎓 Période Cours — Semaines 17-18

### Semaine 17 — Docker

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | Docker — Get Started (documentation officielle) | 3-4h | Dockerfile, build, run, images, conteneurs |
| **Mardi** | Docker avancé : multi-stage builds, Compose | 3-4h | Optimisation taille images, orchestration locale |
| **Samedi** | Pratique : image Python pour job Spark/DE | 4-5h | Dockerfile optimisé, .dockerignore |
| **Dimanche** | Google Container Registry / Artifact Registry | 4-5h | Push images, versioning |

### Semaine 18 — CI/CD GCP

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | Implement CI/CD Pipelines on Google Cloud | 3-4h | Google Cloud Skills Boost. Cloud Build, triggers |
| **Mardi** | cloudbuild.yaml approfondi | 3-4h | Syntaxe, étapes, artefacts |
| **Samedi** | Séparation CI vs CD | 4-5h | CI : test/validate. CD : deploy avec garde-fous |
| **Dimanche** | Secrets management, IAM build | 4-5h | Secret Manager, compte de service dédié |

### 📚 Ressources complètes Phase 1C Cours

| Ressource | Type | URL | Notes |
|-----------|------|-----|-------|
| Docker — Get Started | Documentation | https://docs.docker.com/get-started/ | Gratuit |
| Dockerfile reference | Référence | https://docs.docker.com/engine/reference/builder/ | |
| Implement CI/CD Pipelines on Google Cloud | Cours Skills Boost | https://www.cloudskillsboost.google/course_templates/276 | |
| Cloud Build documentation | Référence | https://cloud.google.com/build/docs | |
| Secret Manager documentation | Référence | https://cloud.google.com/secret-manager/docs | |

### Pratiques guidées Docker

```
☐ Installer Docker Desktop (Mac/Windows) ou Docker Engine (Linux)
☐ docker build -t mon-image .
☐ docker run -d -p 8080:8080 -v $(pwd)/data:/data -e ENV=dev mon-image
☐ docker stop / rm / ps / logs
☐ docker-compose up -d
☐ Fichier .dockerignore optimisé
```

---

## 🔧 Période Projet — Semaines 19-20

### Architecture pipeline CI/CD

```
Push/PR sur feature/* →
  ├── terraform fmt -check
  ├── terraform validate
  ├── terraform plan (non destructif)
  └── tests unitaires si code Python

Merge sur main →
  ├── terraform plan (review obligatoire)
  └── ⛔ terraform apply MANUEL (pas auto)
```

### Semaine 19

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi** | Configurer trigger Cloud Build GitHub | cloudbuild.yaml CI |
| **Mardi** | Étapes CI : fmt, validate, plan, tests | Fonctionnel sur PR |
| **Samedi** | Cloud Build CD : plan sur main, apply manuel | cloudbuild.yaml CD |
| **Dimanche** | IAM build service account, permissions minimales | Documentation |

### Semaine 20

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi** | Intégration Secret Manager | Secrets hors repo |
| **Mardi** | Tests end-to-end pipeline | Scénarios PR, merge, fail |
| **Samedi** | Documentation runbook CI/CD | docs/ci-cd-runbook.md |
| **Dimanche** | Git push, repo exemple public | Portfolio DevOps |

---

# PHASE 2 : BIGQUERY + DATAFORM + VISUALISATION (2 MOIS)

## 🎓 Période Cours — Semaines 21-23

### Semaine 21 — BigQuery

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | BigQuery for Data Analysts | 3-4h | Google Cloud training. ~5h total |
| **Mardi** | BigQuery for Data Analysts (suite) | 3-4h | |
| **Samedi** | Documentation BigQuery : datasets, tables, SQL | 4-5h | cloud.google.com/bigquery/docs |
| **Dimanche** | Partitions, clustering, chargement depuis GCS | 4-5h | Optimisation performance/coût |

### Semaine 22 — Dataform

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | Dataform — Quickstart créer workflow SQL | 3-4h | Documentation Google Cloud |
| **Mardi** | Dataform — Workflows SQL | 3-4h | Modèles, dépendances, exécutions |
| **Samedi** | Dataform — Assertions de qualité | 4-5h | Tests intégrés dans le pipeline |
| **Dimanche** | Dataform — Cycle de vie dev/prod | 4-5h | Git intégration, releases |

### Semaine 23 — Consolidation

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | Looker Studio — connexion BigQuery | 3-4h | Dashboard basique |
| **Mardi** | Looker Studio — visualisations avancées | 3-4h | Filtres, paramètres, calculs |
| **Samedi** | Révision architecture complète BQ+Dataform+Looker | 4-5h | |
| **Dimanche** | Pratique intégrée | 4-5h | Mini-projet guidé |

### 📚 Ressources complètes Phase 2 Cours

| Ressource | Type | URL | Langue | Durée |
|-----------|------|-----|--------|-------|
| BigQuery for Data Analysts | Cours Google Cloud | https://cloud.google.com/learn/training/data-engineering-and-analytics | 🇬🇧 | ~5h |
| Documentation BigQuery | Référence | https://cloud.google.com/bigquery/docs | 🇫🇷/🇬🇧 | Continue |
| Dataform — Quickstart | Documentation | https://docs.cloud.google.com/dataform/docs/quickstart-create-workflow?hl=fr | 🇫🇷 Français | ~2h |
| Dataform — Présentation | Référence | https://cloud.google.com/dataform/docs/overview | 🇫🇷/🇬🇧 | |
| Dataform — Workflows SQL | Référence | https://cloud.google.com/dataform/docs/sql-workflows | 🇫🇷/🇬🇧 | |
| Dataform — Assertions | Référence | https://cloud.google.com/dataform/docs/assertions | 🇫🇷/🇬🇧 | |
| Dataform — Cycle de vie | Référence | https://cloud.google.com/dataform/docs/managing-code-lifecycle | 🇫🇷/🇬🇧 | |
| Looker Studio | Documentation | https://support.google.com/looker-studio | 🇫🇷/🇬🇧 | |

---

## 🔧 Période Projet — Semaines 24-27

### Architecture cible

```
Sources (CSV/API) → GCS landing → BigQuery raw 
    → Dataform (staging → intermediate → marts) 
    → Looker Studio dashboard
```

### Semaine 24 — Infrastructure

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi** | Terraform : datasets BQ (raw, staging, mart) | Terraform modifié Phase 1B |
| **Mardi** | Config Dataform repository, connexion BigQuery | Projet Dataform initialisé |

### Semaine 25 — Développement Dataform

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Samedi** | Models staging : sources propres, types, renommage | definitions/staging/ |
| **Dimanche** | Models intermediate : jointures, métriques métier | definitions/intermediate/ |

### Semaine 26 — Qualité et Marts

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi** | Models marts : tables finales analytiques | definitions/marts/ |
| **Mardi** | Assertions qualité : unicité, nulls, référentiel | assertions/ |

### Semaine 27 — Visualisation et Documentation

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Samedi** | Dashboard Looker Studio : KPIs, filtres, UX | Dashboard publié |
| **Dimanche** | Documentation auto-générée Dataform, README | Site docs/ ou dbt-docs-like |

---

# PHASE 3A : ARCHITECTURE DATA LAKES & WAREHOUSES (1 MOIS)

## 🎓 Période Cours — Semaines 28-29

### Semaine 28

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | Introduction to Data Engineering on Google Cloud | 3-4h | Skills Boost. Rôle DE, composants, modèles pipelines |
| **Mardi** | Introduction to Data Engineering on Google Cloud (suite) | 3-4h | |
| **Samedi** | Modernizing Data Lakes and Data Warehouses with Google Cloud — début | 4-5h | ~8h total, en français |
| **Dimanche** | Modernizing (suite) : lacs de données | 4-5h | GCS, formats ouverts |

### Semaine 29

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | Modernizing (suite) : entrepôts de données | 3-4h | BigQuery comme warehouse |
| **Mardi** | Créer des lacs de données et entrepôts de données sur Google Cloud | 3-4h | Cours spécifique du parcours, ~5h |
| **Samedi** | Build a Data Warehouse with BigQuery | 4-5h | ~1h15, pratique guidée |
| **Dimanche** | Révision + documentation Cloud Storage | 4-5h | cloud.google.com/storage/docs |

### 📚 Ressources complètes Phase 3A Cours

| Ressource | Type | URL | Langue | Durée |
|-----------|------|-----|--------|-------|
| Introduction to Data Engineering on Google Cloud | Cours Skills Boost | https://www.cloudskillsboost.google/course_templates/1157?locale=fr | 🇫🇷 Français | ~5h |
| Modernizing Data Lakes and Data Warehouses with Google Cloud | Cours Skills Boost | https://www.cloudskillsboost.google/paths/16?locale=fr | 🇫🇷 Français | ~8h |
| Créer des lacs de données et entrepôts de données | Cours du parcours | Inclus ci-dessus | 🇫🇷 Français | ~5h |
| Build a Data Warehouse with BigQuery | Cours du parcours | Inclus ci-dessus | 🇫🇷 Français | ~1h15 |
| Documentation Cloud Storage | Référence | https://cloud.google.com/storage/docs | 🇫🇷/🇬🇧 | |

---

## 🔧 Période Projet — Semaines 30-31

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi S30** | Architecture zones GCS : bronze (raw), silver (cleaned), gold (aggregated) | Terraform GCS buckets avec lifecycle |
| **Mardi S30** | Intégration avec Dataform existant : raw = external BQ tables | Adaptation models staging |
| **Samedi S31** | Pipeline ingestion automatisée : Cloud Functions ou Cloud Run | Fonction déclenchée par nouveau fichier GCS |
| **Dimanche S31** | Tests intégration, documentation architecture | Diagramme architecture, README |

---

# PHASE 3B : BATCH SPARK SERVERLESS (1.5 MOIS)

## 🎓 Période Cours — Semaines 32-34

### Semaine 32-33

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi S32** | Building Batch Data Pipelines on Google Cloud — début | 3-4h | Skills Boost. Pipelines batch, Dataproc |
| **Mardi S32-S33** | Building Batch Data Pipelines (suite) | 3-4h | Spark sur Dataproc, jobs PySpark |
| **Samedi S33** | Building Batch Data Pipelines (fin) | 4-5h | |
| **Dimanche S33** | Documentation Dataproc officielle | 4-5h | cloud.google.com/dataproc/docs |

### Semaine 34

| Jour | Cours | Durée | Détails |
|------|-------|-------|---------|
| **Lundi** | Dataproc Serverless for Apache Spark | 3-4h | ⭐ PRIORITAIRE. Sans gestion cluster |
| **Mardi** | Comparaison Dataproc classique vs Serverless | 3-4h | Quand utiliser quoi |
| **Samedi** | Pratique Serverless : premier job PySpark | 4-5h | Console + gcloud |
| **Dimanche** | Optimisation : batch sizing, autoscaling | 4-5h | Coûts, performance |

### 📚 Ressources complètes Phase 3B Cours

| Ressource | Type | URL | Langue | Durée |
|-----------|------|-----|--------|-------|
| Building Batch Data Pipelines on Google Cloud | Cours Skills Boost | https://www.cloudskillsboost.google/paths/16/course_templates/53?locale=fr | 🇫🇷 Français | ~9h15 |
| Documentation Dataproc | Référence | https://cloud.google.com/dataproc/docs | 🇫🇷/🇬🇧 | |
| Dataproc Serverless | Référence | https://docs.cloud.google.com/dataproc-serverless/docs/overview | 🇬🇧 | |
| Dataproc Serverless — Submit PySpark jobs | Guide | https://docs.cloud.google.com/dataproc-serverless/docs/quickstarts/jupyterlab-plugin | 🇬🇧 | |

> ⭐ **Dataproc Serverless est l'option par défaut.** Clusters gérés uniquement mentionnés comme contexte historique ou besoins très spécifiques.

---

## 🔧 Période Projet — Semaines 35-37

### Pipeline cible

```
CSV/Parquet GCS landing 
    → Dataproc Serverless PySpark (transformations lourdes)
    → Parquet GCS processed (partitionné)
    → BigQuery external table ou native load
    → Dataform mart (SQL)
    → Dashboard
```

### Semaine 35

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi** | Job PySpark Serverless : lecture GCS, transformations | script_spark.py |
| **Mardi** | Écriture Parquet partitionné GCS | Optimisation format |

### Semaine 36

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Samedi** | Intégration BigQuery : external tables vs load native | Terraform + test performance |
| **Dimanche** | Connexion Dataform : nouveau source = tables Spark | Adaptation pipeline SQL |

### Semaine 37

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi** | CI/CD Cloud Build pour le job Spark | cloudbuild.yaml adapté |
| **Mardi** | Monitoring Cloud Monitoring, alerting | Dashboard ops |
| **Samedi** | Optimisation coûts Serverless : right-sizing | Analyse coût/performance |
| **Dimanche** | Documentation, tests finaux | Pipeline documentée, testée |

---

# PHASE 3C : CAPSTONE DATA ENGINEERING (3 MOIS)

## 🔧 Projet intégré — Semaines 38-50

### Architecture complète production-like

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   SOURCES       │     │   ORCHESTRATION │     │   LANDING ZONE  │
│  - API batch    │────→│  Cloud Composer │────→│   GCS bronze/   │
│  - Fichiers     │     │  ou Cloud       │     │   raw/          │
│    périodiques  │     │  Functions +    │     │   YYYY/MM/DD    │
│  - (optionnel   │     │  Cloud Scheduler│     │                 │
│    streaming    │     │                 │     │                 │
│    Pub/Sub)     │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                              ┌───────────────────────┘
                              ▼
                    ┌─────────────────┐
                    │  TRANSFORMATION │
                    │  Dataproc       │
                    │  Serverless     │
                    │  PySpark        │
                    │                 │
                    │  - Validation   │
                    │  - Enrichissement│
                    │  - Anonymisation│
                    │  - Standardisation│
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐     ┌─────────────────┐
                    │  PROCESSED ZONE │────→│   BIGQUERY      │
                    │  GCS silver/    │     │   raw dataset   │
                    │  cleaned/       │     │   (external     │
                    │  Parquet        │     │   tables)       │
                    └─────────────────┘     └─────────────────┘
                                                    │
                              ┌───────────────────────┘
                              ▼
                    ┌─────────────────┐
                    │   DATAFORM      │
                    │   TRANSFORMATION│
                    │                 │
                    │  staging/       │
                    │  intermediate/  │
                    │  marts/         │
                    │                 │
                    │  - Business logic│
                    │  - Aggregations │
                    │  - Tests qualité│
                    │    (assertions) │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐     ┌─────────────────┐
                    │  MARTS BIGQUERY │────→│  LOOKER STUDIO  │
                    │  gold/          │     │  DASHBOARD      │
                    │  analytics      │     │                 │
                    │  tables         │     │  - KPIs métier  │
                    └─────────────────┘     │  - Filtres      │
                              │              │  - Alertes      │
                              ▼              └─────────────────┘
                    ┌─────────────────┐
                    │   MONITORING &  │
                    │   GOVERNANCE    │
                    │                 │
                    │  - Cloud        │
                    │    Monitoring   │
                    │  - Data quality │
                    │    alerts       │
                    │  - Lineage      │
                    │    (Data Catalog)│
                    └─────────────────┘
```

---

## Itération par semaine type (Semaines 38-50)

| Jour | Focus | Activités types |
|------|-------|---------------|
| **Lundi** | Développement feature | Nouveau composant, intégration, bugfix |
| **Mardi** | Intégration composants | Tests inter-modules, résolution conflits |
| **Samedi** | Tests, monitoring, optimisation | Tests end-to-end, bench performance, réduction coûts |
| **Dimanche** | Review, documentation, planning | Code review, docs, rétro, plan semaine suivante |

### Jalons clés

| Semaine | Jalon | Validation |
|---------|-------|------------|
| 41 | MVP ingestion → Spark → BQ fonctionnel | Données traversent pipeline |
| 44 | Dataform + dashboard intégrés | Valeur métier visible |
| 47 | CI/CD complet, monitoring actif | Pipeline "production-like" |
| 50 | Livrable final, portfolio prêt | Présentation, démo enregistrée |

### Livrables finaux

- [ ] **Repo GitHub** : code complet, documenté, testé
- [ ] **Documentation architecture** : diagrammes, choix techniques, trade-offs
- [ ] **Runbook opérationnel** : comment débuguer, scaler, récupérer
- [ ] **Dashboard public** (si données permissives) ou démo enregistrée
- [ ] **Analyse coûts** : architecture optimisée, justifications
- [ ] **Présentation 10 min** : storytelling du projet

---

# PHASE 4 : AI DEV TOOLS ZOOMCAMP (1.5 MOIS)

## 🎓 Période Cours — Semaines 51-56

### Programme officiel
- **Organisateur** : DataTalksClub
- **URL** : https://github.com/DataTalksClub/ai-dev-tools-zoomcamp
- **Durée** : ~6 semaines

### Semaine 51-52 — Modules 1-2 : Setup et premiers outils

| Jour | Contenu | Durée | Détails |
|------|---------|-------|---------|
| **Lundi S51** | Module 1 : Introduction, écosystème AI dev tools | 3-4h | Landscape 2024, comment choisir |
| **Mardi S51-S52** | Module 2 : GitHub Copilot approfondi | 3-4h | Prompts, contexte, génération de tests |
| **Samedi S52** | Alternative : Continue.dev (open source) | 4-5h | Self-hosted, modèles locaux |
| **Dimanche S52** | Alternative : Codeium | 4-5h | Gratuit illimité, comparaison |

### Semaine 53-55 — Modules 3-6 : Agents et intégration

| Jour | Contenu | Durée | Détails |
|------|---------|-------|---------|
| **Lundi S53** | Module 3 : Agents IA — Auto-GPT, BabyAGI | 3-4h | Concepts, limites, cas d'usage |
| **Mardi S53-S54** | Module 4 : Prompt engineering avancé pour dev | 3-4h | Chain-of-thought, few-shot, structured output |
| **Samedi S54-S55** | Module 5 : Intégration IDE — VS Code, JetBrains | 4-5h | Workflows personnalisés |
| **Dimanche S55** | Module 6 : Automatisation — génération docs, tests | 4-5h | CI pour la génération |

### Semaine 56 — Module 7+ et consolidation

| Jour | Contenu | Durée | Détails |
|------|---------|-------|---------|
| **Lundi** | Module 7 : Outils émergents, veille | 3-4h | Cursor, Aider, Devin, etc. |
| **Mardi** | Pratique intensive : config environnement perso | 3-4h | Ton setup optimal |
| **Samedi** | Benchmark : avant/après productivité | 4-5h | Métriques subjectives |
| **Dimanche** | Documentation "mon workflow avec IA" | 4-5h | Article ou README |

---

## 🔧 Période Projet — Semaines 54-56 (chevauchement)

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi S54** | Configurer environnement DE optimisé IA | .cursorrules, prompts personnalisés |
| **Mardi S55** | Scripts d'automatisation générés par IA | generate_dag.py, generate_tests.py, etc. |
| **Samedi S55-S56** | Documentation "comment je code maintenant" | Article de blog ou README détaillé |
| **Dimanche S56** | Comparaison mesurée : tâche avec/sans IA | Benchmark concret |

---

# PHASE 5 : LLM ZOOMCAMP (3 MOIS)

## 🎓 Période Cours — Semaines 57-64

### Programme officiel
- **Organisateur** : DataTalksClub
- **URL** : https://github.com/DataTalksClub/llm-zoomcamp
- **Durée** : ~10 semaines

### Semaine 57-60 — Module RAG

| Jour | Contenu | Durée | Détails |
|------|---------|-------|---------|
| **Lundi S57** | Introduction RAG, embeddings | 3-4h | Concepts, quand l'utiliser |
| **Mardi S57-S58** | Vector databases : Chroma, Weaviate, Vertex AI Matching Engine | 3-4h | Comparaison, choix |
| **Samedi S58-S59** | Chunking stratégies, indexing | 4-5h | Optimisation retrieval |
| **Dimanche S59-S60** | Recherche sémantique, hybrid search | 4-5h | Re-ranking, métriques |

### Semaine 61-64 — Fine-tuning et évaluation

| Jour | Contenu | Durée | Détails |
|------|---------|-------|---------|
| **Lundi S61** | Fine-tuning : LoRA, QLoRA | 3-4h | Efficient fine-tuning |
| **Mardi S61-S62** | Vertex AI Training custom | 3-4h | Pipeline fine-tuning GCP |
| **Samedi S62-S63** | Évaluation : métriques, benchmark, human eval | 4-5h | Rouge, Bleu, MTEB, etc. |
| **Dimanche S63-S64** | Déploiement : Cloud Run, Cloud Functions, latence | 4-5h | Optimisation coût/latence |

---

## 🔧 Période Projet — Semaines 65-68

### Concept : RAG sur tes données Data Engineering

```
Question utilisateur (langage naturel)
    ↓
"Comment optimiser cette requête BigQuery ?"
    ↓
[Retrieval] Documentation techniques GCP/Spark collectées
            + Queries types du projet Capstone
            + Erreurs fréquentes et solutions
    ↓
[Augmented Prompt] Contexte récupéré + question
    ↓
[Generation] Réponse structurée : SQL optimisé + explications
    ↓
[Output] Code + liens documentation + exécution possible
```

### Semaine 65-66 — Développement

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi S65** | Collecte corpus : docs GCP, Spark, ton projet | data/corpus/ |
| **Mardi S65-S66** | Chunking, embedding, indexation vectorielle | Pipeline indexing |
| **Samedi S66** | API RAG : retrieval + generation | app/main.py |
| **Dimanche S66** | Tests qualité retrieval, ajustement | Métriques, iteration |

### Semaine 67 — Déploiement

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi S67** | Containerisation, push Artifact Registry | Dockerfile, CI/CD |
| **Mardi S67** | Déploiement Cloud Run | Service live |
| **Samedi S67** | Monitoring : logs, feedback utilisateur | Cloud Monitoring |
| **Dimanche S67** | Optimisation : cache, batch, coûts | Version optimisée |

### Semaine 68 — Finalisation

| Jour | Tâche | Livrable |
|------|-------|----------|
| **Lundi** | Tests charge, sécurité (rate limiting) | Rapport |
| **Mardi** | Documentation complète | README, architecture, runbook |
| **Samedi** | Démo enregistrée, article portfolio | Vidéo 5 min ou article |
| **Dimanche** | Release finale, repo public | Portfolio complet |

---

## 🎯 Livrable final Phase 5

| Élément | Description |
|---------|-------------|
| **Application accessible** | URL Cloud Run, utilisable par recruteur |
| **Repo documenté** | README, architecture, comment contribuer |
| **Démo enregistrée** | 5 min montrant la chaîne complète |
| **Narrative cohérente** | "Je maîtrise la chaîne données + IA" |

---

# 📎 ANNEXES

## Outils recommandés tout au long

| Usage | Outil | Alternative |
|-------|-------|-------------|
| Notes | Obsidian, Notion | Google Keep |
| Code | VS Code + extensions | JetBrains |
| Git | GitHub | GitLab, Bitbucket |
| Cloud | GCP Free Tier + crédits éducation | — |
| Coûts | GCP Cost Calculator, FinOps | — |

## Communautés et veille

| Ressource | URL | Usage |
|-----------|-----|-------|
| DataTalksClub Slack | datatalks.club | Questions Zoomcamp, networking |
| Google Cloud Community | cloud.google.com/community | Support GCP officiel |
| r/dataengineering | reddit.com/r/dataengineering | Veille, discussions |
| Last Week in AWS (et GCP équivalent) | newsletters | Veille cloud |

## Certifications possibles en parallèle (optionnel)

| Certification | Quand | Préparation |
|-------------|-------|-------------|
| Google Cloud Associate Cloud Engineer | Après Phase 1C | Examen pratique, pas théorique |
| Google Cloud Professional Data Engineer | Après Phase 3C | Nécessite expérience réelle |
| Databricks Data Engineer Associate | Si besoin | Déjà couvert par Phase 0 |

---

*Dernière mise à jour : Octobre 2026*
*Prochaine review suggérée : Fin Phase 0 (Décembre 2026)*
```

---


