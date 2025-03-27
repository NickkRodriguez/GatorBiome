# GatorBiome

## Objectives
The team aims to develop a **machine learning algorithm** that maps human gut microbiome data to disease states. The ultimate goal is to use this algorithm to **predict diseases** based on microbiome readings.

## Team Responsibilities

- **Nick Rodriguez** – Team Lead: Leads ML pipeline design and implementation, oversees system architecture, and drives project direction and deliverables.
- **Connor McLoon** – Focuses on model training, hyperparameter tuning, and optimization strategy.
- **Lachyn Almazova** – Frontend Lead: Implements Vue.js dashboard and connects visual outputs.
- **David Alvarez** – Backend Lead: Develops Django REST API and prepares dashboard endpoints.
- **Advisor** – Fatemeh Tavassoli: Provides project guidance and microbiome dataset methodology.

## 📁 Docs

### Project Structure

- `training_pipeline.ipynb` – Trains 17 models on both CLR and rarefied datasets; selects the best based on AUC and other metrics.
- `feature_engineering.ipynb` – Compares six feature selection/extraction methods against the baseline model.
- `models/` – Contains model wrapper classes (with custom `.train()` and `.predict()` logic).
- `utils/` – Contains evaluation functions and shared utilities.
- `data/` – Place CLR and rarefied `.csv` files here (excluded from repo).
- `results/` – Auto-generated JSON and text outputs for model performance (used by frontend).

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


## ⚠️ Dataset Access:
- Due to data sharing restrictions, the microbiome datasets used in this project are **not included** in this repository.
- To run the training and feature engineering pipelines, place the appropriate `.csv` files inside the `data/` folder as specified in the documentation.
- If you're part of the **course staff** and need access to the datasets, please contact me (Nick Rodriguez) through my university email (visible to instructors on file).