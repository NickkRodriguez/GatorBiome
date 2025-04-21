from xgboost import XGBClassifier
from utils.evaluate import evaluate_model
from sklearn.model_selection import GridSearchCV

import optuna
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
import numpy as np
import os

#Not sure yet if this one works since it's different packages, but if lgbm does this one should too
class xgb_model():
    def __init__(self, seed=42):
        self.model = XGBClassifier(eval_metric="logloss", random_state=seed)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)[:, 1]
        return evaluate_model(y_test, pred, prob)

    def objective(self, trial, X, y):
        n_estimators = trial.suggest_int("n_estimators", 25,500)
        max_depth = trial.suggest_int("max_depth", 3,50)
        max_leaves = trial.suggest_int("max_leaves", 0,1000)
        learning_rate = trial.suggest_float("learning_rate", -3, 3)
        grow_policy = trial.suggest_categorical("grow_policy", ['depthwise', 'lossguide'])

        xgb = XGBClassifier(n_estimators=n_estimators,
                            max_depth=max_depth,
                            max_leaves=max_leaves,
                            learning_rate=learning_rate,
                            grow_policy=grow_policy)

        try:
            score = cross_val_score(xgb, X, y, cv=StratifiedKFold(5), scoring="accuracy")
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