from lightgbm import LGBMClassifier
from sklearn.model_selection import GridSearchCV
from utils.evaluate import evaluate_model
import pandas as pd

import optuna
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
import numpy as np
import os


class lgbm_model():

    def __init__(self, seed=0):
        if(seed==0):
            self.model = LGBMClassifier(min_data_in_leaf= 5, verbose=-1, class_weight='balanced')
        else:
            self.model = LGBMClassifier(random_state=seed, min_data_in_leaf= 5, verbose=-1, class_weight='balanced')

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)[:, 1]
        return evaluate_model(y_test, pred, prob)
    
    def objective(self, trial, X, y):
        num_leaves = trial.suggest_int("num_leaves", 10, 300)
        min_data_in_leaf = trial.suggest_int("min_data_in_leaf", 5, 30)
        max_depth = trial.suggest_int("max_depth", 3,50)
        learning_rate = trial.suggest_float("learning_rate", -3,3)
        num_iterations = trial.suggest_int("num_iterations", 10,100)
        lgbm = LGBMClassifier(verbose=-1,
                              num_leaves=num_leaves,
                              min_data_in_leaf=min_data_in_leaf,
                              max_depth=max_depth,
                              learning_rate=learning_rate,
                              num_iterations=num_iterations,
                              class_weight='balanced')

        try:
            score = cross_val_score(lgbm, X, y, cv=StratifiedKFold(5), scoring="accuracy")
            return np.mean(score)
        except Exception as e:
            print(f"Skipping due to error")
            raise optuna.exceptions.TrialPruned()
        
    def tune_params(self, x, y, trials, model_name, dataset_name):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        results_dir = os.path.join(base_dir, "../results/tuning/")
        os.makedirs(results_dir, exist_ok=True)
        db_path = os.path.join(results_dir, "tuning_results.db")
        study = optuna.create_study(direction="maximize", study_name= model_name + " " +dataset_name, storage = f"sqlite:///{os.path.abspath(db_path)}")
        study.optimize(lambda trial: self.objective(trial, x, y), n_trials=trials, timeout=360)

    def reset(self,model_name,dataset_name):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        results_dir = os.path.join(base_dir, "../results/tuning/")
        os.makedirs(results_dir, exist_ok=True)
        db_path = os.path.join(results_dir, "tuning_results.db")
        try:
            optuna.delete_study(study_name= model_name + " " +dataset_name, storage = f"sqlite:///{os.path.abspath(db_path)}")
        except KeyError as e:
            print("Failed delete, record does not exist")