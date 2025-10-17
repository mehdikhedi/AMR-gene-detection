# AMR Gene Detection Demo

<details open>
  <summary>🇬🇧 English</summary>
A compact Python + Jupyter project that showcases the workflow for scanning bacterial
DNA sequences against a tiny catalog of antimicrobial resistance (AMR) genes.

## Project Highlights

- **Input formats**: DNA sequences in FASTA and reference genes in CSV.
- **Similarity scoring**: Base-by-base identity with the top match reported per isolate.
- **Automation**: Command-line interface plus a notebook for exploratory analysis.
- **Outputs**: Tabular summary with similarity percentages and optional CSV export.

## Repository Structure

```
AMR-gene-detection/
├── data/
│   ├── resistance_genes_reference.csv   # Example AMR gene catalog
│   ├── sample_sequences.fasta           # Demo isolate sequences
│   └── amr_matches_report.csv           # Generated report
├── notebooks/
│   └── AMR_demo.ipynb                   # Interactive exploration notebook
├── src/
│   ├── compare_to_reference.py          # Sequence comparison logic
│   └── report_generator.py              # Report orchestration & CSV export
├── requirements.txt                     # Project dependencies
└── README.md                            # Final documentation deliverable
```

## Quick Start

### 1. Set up the environment

```powershell
git clone https://github.com/mehdikhedi/AMR-gene-detection.git
cd AMR-gene-detection

python -m venv .venv
.venv\Scripts\Activate.ps1  # PowerShell (Windows)
# source .venv/bin/activate  # macOS / Linux

pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Run the comparison (CLI)

```powershell
python -m src.report_generator
```

This reads the FASTA and CSV from `data/`, identifies the closest AMR gene per sample,
prints the summary table, and saves `data/amr_matches_report.csv`.

### 3. Explore via notebook

1. Launch Jupyter (`jupyter notebook` or `jupyter lab`).
2. Open `notebooks/AMR_demo.ipynb`.
3. Select the `.venv` Python interpreter.
4. Run all cells to regenerate the report, view the DataFrame, and confirm the CSV export.

## Example Output

```text
Sample_ID Closest_AMR_Gene  Similarity(%)
isolate_1           blaTEM          100.0
isolate_2             tetA          100.0
```

## Next Steps (Ideas)

- Extend the similarity scoring with alignment algorithms (e.g., Smith-Waterman).
- Support larger reference catalogs or REST data sources.
- Visualize similarity distributions across isolates.
- Integrate the report generator into a broader VetPathogen pipeline.

## Credits

Created by Mehdi Khedi as part of a bioinformatics learning track. Suggestions,
issues, and improvements are welcome!
</details>


<details> 
  <summary>🇫🇷 Français</summary>
Un projet Python + Jupyter compact qui illustre comment comparer des séquences
ADN bactériennes à un petit catalogue de gènes de résistance aux antimicrobiens (AMR).

## Points clés du projet

- **Formats d'entrée** : séquences ADN au format FASTA et gènes de référence en CSV.
- **Score de similarité** : identité base par base avec le meilleur gène reporté pour
  chaque isolat.
- **Automatisation** : interface en ligne de commande et notebook pour l'analyse
  exploratoire.
- **Résultats** : tableau de synthèse avec pourcentages de similarité et export CSV
  optionnel.

## Organisation du dépôt

```
AMR-gene-detection/
├── data/
│   ├── resistance_genes_reference.csv   # Petit catalogue AMR d'exemple
│   ├── sample_sequences.fasta           # Séquences d'isolats de démonstration
│   └── amr_matches_report.csv           # Rapport généré
├── notebooks/
│   └── AMR_demo.ipynb                   # Notebook d'exploration interactive
├── src/
│   ├── compare_to_reference.py          # Logique de comparaison de séquences
│   └── report_generator.py              # Génération du rapport et export CSV
├── requirements.txt                     # Dépendances du projet
└── README.md                            # Documentation finale
```

## Mise en route

### 1. Préparer l'environnement

```powershell
git clone https://github.com/mehdikhedi/AMR-gene-detection.git
cd AMR-gene-detection

python -m venv .venv
.venv\Scripts\Activate.ps1  # PowerShell (Windows)
# source .venv/bin/activate  # macOS / Linux

pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Lancer la comparaison (CLI)

```powershell
python -m src.report_generator
```

La commande lit les fichiers FASTA/CSV dans `data/`, identifie pour chaque échantillon
le gène AMR le plus proche, affiche le tableau récapitulatif et enregistre
`data/amr_matches_report.csv`.

### 3. Explorer avec le notebook

1. Lancer Jupyter (`jupyter notebook` ou `jupyter lab`).
2. Ouvrir `notebooks/AMR_demo.ipynb`.
3. Sélectionner l'interpréteur Python de `.venv`.
4. Exécuter toutes les cellules pour régénérer le rapport, visualiser le DataFrame et
   vérifier l'export CSV.

## Exemple de sortie

```text
Sample_ID Closest_AMR_Gene  Similarity(%)
isolate_1           blaTEM          100.0
isolate_2             tetA          100.0
```

## Idées pour aller plus loin

- Utiliser des algorithmes d'alignement (p. ex. Smith-Waterman) pour affiner les scores.
- Supporter des catalogues de référence plus grands ou des sources REST.
- Visualiser les distributions de similarité entre isolats.
- Intégrer le générateur de rapports dans une chaîne de traitement VetPathogen plus large.

## Crédits

Projet réalisé par Mehdi Khedi dans le cadre d'un parcours d'apprentissage
en bio-informatique. Vos retours et suggestions sont les bienvenus !
</details>
