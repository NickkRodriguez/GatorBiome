# GatorBiome
- Overall objectives: What the team is trying to achieve?
    - The team will strive to achieve a machine learning algorithm that can map data of the human gut microbiome to disease states. The end goal of the project is to use this algorithm to predict disease through microbiome readings.
      
- Individual responsibilities: What each team member is expected to do?
    - Connor McLoon: Work on ML algorithms and training. Helping with data cleaning.
    - Nick Rodriguez: Oversee project progress, set timelines, and ensure adherence to objectives. Work on ML algorithms and training. 
    - Lachyn Almazova: Frontend/ML.
    - David Alvarez: Work on ML algorithms and training.

- Docs:
    - The main pipeline is now in ProjectPipelineTest in the Jupyter notebook: main.ipynb
    - main.ipynb currently controls main training/testing loop, model training, evaluation, and result presentation.
    - The model classes (e.g., models/name_model.py) are still used and imported into the notebook.
    - The main.py script has been archived in the archive/ directory for reference.


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
