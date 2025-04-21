from sklearn.svm import SVC
from utils.evaluate import evaluate_model
from sklearn.model_selection import GridSearchCV

import optuna
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
import numpy as np
import os


#Because there are 2 SVC models, only one needs grid search
class svm_linear_model():
    def __init__(self):
        self.model = SVC(kernel='linear', probability=True) # set to true for auc

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)[:, 1]
        return evaluate_model(y_test, pred, prob)

    def objective(self, trial, X, y):
        kernel = trial.suggest_categorical("kernel",['linear','poly','rbf','sigmoid','precomputed'])
        degree = trial.suggest_int("degree", 1,20)
        gamma = trial.suggest_categorical("gamma", ['scale', 'auto'])
        probability = trial.suggest_categorical("probability", [True, False])
        svc = SVC(kernel=kernel,
                       degree=degree,
                       gamma=gamma,
                       probability=probability)

        try:
            score = cross_val_score(svc, X, y, cv=StratifiedKFold(5), scoring="accuracy")
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