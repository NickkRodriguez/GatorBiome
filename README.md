# GatorBiome

## Objectives
The team aims to develop a **machine learning algorithm** that maps human gut microbiome data to disease states. The ultimate goal is to use this algorithm to **predict diseases** based on microbiome readings.

## Team Responsibilities
- **Nick Rodriguez** – Team lead: Oversees progress, sets timelines, ensures adherence to objectives, and contributes to ML algorithms and training.
- **Connor McLoon** – Works on ML algorithms and training; assists with data cleaning.
- **Lachyn Almazova** – Focuses on frontend development and ML integration.
- **David Alvarez** – Works on ML algorithms and training.

## Docs

### Project Structure
- `training_pipeline.ipynb` – Model training.
- `feature_engineering.ipynb` – Feature selection & evaluation.
- Model classes are in `models/`, and utility functions are in `utils/`.
- Datasets (currently a placeholder) are in `data/`.
- The best-performing model from training is stored in `data/best_model.txt`.

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
