# GatorBiome

## Objectives
The team aims to develop a **machine learning algorithm** that maps human gut microbiome data to disease states. The ultimate goal is to use this algorithm to **predict diseases** based on microbiome readings.

## Team Responsibilities

- **Nick Rodriguez** – Team Lead: Leads the design and implementation of the training pipeline, feature engineering, and ensemble modeling. Developed the majority of model classes and oversees system architecture, visualizations, and project direction.
- **Connor McLoon** – Designed the initial training pipeline structure and implemented the hyperparameter tuning logic across all supported models.
- **Lachyn Almazova** – Frontend Lead: Implements Vue.js dashboard and connects visual outputs.
- **David Alvarez** – Backend Lead: Develops Django REST API and prepares dashboard endpoints.
- **Advisor** – Fatemeh Tavassoli, PhD: Provides project guidance and microbiome dataset methodology.

## 📁 Docs

### Project Structure

- `training_pipeline.ipynb` – Trains all models on both CLR and rarefied datasets using 100 stratified train/test splits. Stores per-run predictions and metrics. Saves ROC curves, versioned pickles, and model summaries.
- `feature_engineering.ipynb` – Compares six feature engineering methods (3 selection, 3 extraction) across multiple feature counts using 100 randomized runs. Tracks per-run predictions and identifies the best method using concatenated predictions. Outputs JSON/CSV summaries, ROC plots, and visual comparisons.
- `ensemble_modeling.ipynb` – Evaluates cross-derivative ensembles (e.g., CLR + rarefied) using soft voting, hard voting, and logistic regression stacking. Aligns predictions by sample ID and saves ensemble ROC curves, performance tables, and JSON summaries.
- `evaluate.py` – Computes metrics (AUC, accuracy, precision, recall, F1), supports AUC fallback for multiclass cases, and returns predictions for reuse in ROC/ensemble.
- `models/` – Contains model wrapper classes (`.train()` and `.predict()` methods) for sklearn-compatible use in all pipelines.
- `utils/` – Evaluation metrics, selection/extraction utilities, and shared tools for ROC, CSV exports, and visualizations.

- `data/` – Place CLR and rarefied `.csv` files here (excluded from version control). Placeholder datasets like `wine.csv` have been moved to `archive/`.
- `archive/` – Stores legacy files (`main.ipynb`, `main.py`, `wine.csv`, etc.) that are no longer in use but retained for reference.

- `results/` – Stores all outputs from training, feature engineering, and ensemble evaluation.
  - `results/pickles/` – Pickle files storing complete outputs for reproducibility.
  - `results/summaries/` – JSON and CSV summaries (e.g., `best_models.json`, `ensemble_metrics.json`) for backend/frontend use.
  - `results/visuals/`
    - `training/` – ROC curves for training models
    - `feature/clr/`, `feature/rarefied/` – Heatmaps, trend plots, and ROC curves by feature method
    - `ensemble/` – ROC comparison of individual models vs ensemble strategies


### Archival
- `main.ipynb` has been archived in `archive/` for reference.
- Older files, including `main.py`, are in `archive/deprecated/`—delete if no longer needed.


## Setup Instructions
### Using Anaconda (or Miniconda)
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/NickkRodriguez/GatorBiome.git
   cd GatorBiome

2. **Create and Activate the Environment:**
   ```bash
   conda env create -f environment.yml
   conda activate gatorbiome_env

3. **Launch Jupyter Notebook to work on project:**
   ```bash
   jupyter notebook

4. **Close Jupyter Notebook and deactivate the Environment to leave**
   ```bash
   conda deactivate

## Optional: Ensure a Clean Conda Environment

- Why bother?
    - There's a chance of unexpected package behavior and conflicting dependencies. To ensure that your Conda environment uses only the packages installed within it (and ignores any global or user-site packages), you can set the environment variable `PYTHONNOUSERSITE` to `True`.

### Temporary (for the current terminal session):
   ```bash
   export PYTHONNOUSERSITE=True
   ```

### Permanent (can always remove it):

1. Add the following line to your shell configuration file:
   ```bash
   # for bash
   echo "export PYTHONNOUSERSITE=True" >> ~/.bashrc
   # or for Zsh:
   echo "export PYTHONNOUSERSITE=True" >> ~/.zshrc

2. Then reload your shell configuration.


## ⚠️ Dataset Access
- Due to data sharing restrictions, the microbiome datasets used in this project are **not included** in this repository.
- To run the training and feature engineering pipelines, place the appropriate `.csv` files inside the `data/` folder as specified in the documentation.
- If you're part of the **course staff** and need access to the datasets, please contact me (Nick Rodriguez) through my university email (visible to instructors on file).

---

## 🧬 Dataset Upload Requirements (For Web App)

To run the GatorBiome app via the local website, you must upload **two `.csv` datasets** that follow the exact format below.

---

### 📂 File & Upload Rules

- Upload exactly **two `.csv` files** using the upload form on the homepage
- File names can be anything (e.g., `clr.csv`, `set2.csv`, etc.)
- Files must **not** contain slashes (`/`, `\`) or be hidden files (no leading `.`)
- Files are saved into the backend's `./data/` folder automatically

---

### 📄 Required Column Format (Strict Order)

Each `.csv` file must contain **all of the following columns**, in this **exact order**:

| Column Name         | Position        | Description                                  |
|---------------------|------------------|----------------------------------------------|
| sampleid            | First            | Unique sample ID (not used in modeling)      |
| ASV Features        | 2nd to N-2       | All numeric microbiome features              |
| Diagnosis           | Second-to-last   | Human-readable label (e.g., “Normal”, “ASD”) |
| Diagnosis_labeled   | Last             | Only values of 0 or 1; used as the model target |

Column order must match exactly. The pipeline extracts features using positional slicing (`iloc[:, 1:-2]`).

### ⚠️ Additional Format Rules

- All feature values must be numeric only.
- Diagnosis_labeled must only contain values of 0 or 1.
- Missing values (NaN, blanks, or nulls) are not allowed.
- No extra columns beyond those listed above should be present.
- No text values are allowed in feature columns.
- Any preprocessing style is allowed (e.g., rarefied, CLR) as long as all values are numeric.

---

### 🧾 What You’ll See After Upload

Once both datasets are uploaded and the **Run Analysis** button is clicked:

- AUC, Accuracy, F1-score, and other metrics per dataset
- The best model + feature method for each dataset
- ROC curve plots
- Download buttons for `.csv` and `.json` summary results
- *(and any other available visualizations or insights)*

---


# Backend

## Architecture Overview
The GatorBiome backend is built with Django and Django REST Framework, providing a robust API to serve machine learning models, datasets, and prediction results to the frontend dashboard.

## Technologies
- **Django**: Web framework for the backend application
- **Django REST Framework**: Toolkit for building Web APIs
- **SQLite**: Database for development (configurable for production)

## Database Models
The backend uses the following key models:
- **Dataset**: Serves as foreign key to distinguish ModelMetrics
- **MLModel**: Serves as foreign key to distinguish ModelMetrics
- **ModelMetrics**: Records performance metrics (AUC, accuracy, precision, recall, F1) for each model-dataset combination
- **Wine**: Sample dataset for development and testing

## API Endpoints
The backend exposes the following REST API endpoints:

| Endpoint | Method | Description                                                   |
|----------|--------|---------------------------------------------------------------|
| `/api/datasets/` | GET    | List all available datasets                                   |
| `/api/datasets/` | POST   | Add a new dataset                                             |
| `/api/models/` | GET    | List all trained ML models                                    |
| `/api/models/` | POST   | Add an ML model                                               |
| `/api/model-metrics/` | GET    | Get metrics for models, filterable by model name and dataset name |
| `/api/model-metrics/` | POST   | Add metrics for a model-dataset combination                   |

## Backend Setup Instructions

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   
2. Create a virtual environment:
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
    ```bash
   pip install -r requirements.txt

4. Apply Migrations:
    ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Run the development server:
    ```bash
   python manage.py runserver

  The API will be available at http://127.0.0.1:8000/

6. Stopping the server:
Press Ctrl+C in the terminal to stop the server