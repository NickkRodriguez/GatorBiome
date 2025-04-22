from sklearn.tree import DecisionTreeClassifier
from utils.evaluate import evaluate_model
from sklearn.model_selection import GridSearchCV

import optuna
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
import numpy as np
import os



class dt_model():
    
    def __init__(self, seed=0):
        if(seed==0):
            self.model = DecisionTreeClassifier()
        else:
            self.model = DecisionTreeClassifier(random_state=seed)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)[:, 1]
        return evaluate_model(y_test, pred, prob)

    def objective(self, trial, X, y):
        criterion = trial.suggest_categorical("criterion",["gini", "entropy", "log_loss"])
        splitter = trial.suggest_categorical("splitter",["best","random"])
        max_depth = trial.suggest_int("max_depth", 3,50)
        min_samples_split = trial.suggest_int("min_samples_split",2,20)
        min_samples_leaf = trial.suggest_int("min_samples_leaf",1,20)
        max_features = trial.suggest_categorical("max_features", [None, "sqrt", "log2"])
        dtc = DecisionTreeClassifier(criterion=criterion,
                                     splitter=splitter,
                                     max_depth=max_depth, 
                                     min_samples_split=min_samples_split,
                                     min_samples_leaf=min_samples_leaf,
                                     max_features=max_features,)

        try:
            score = cross_val_score(dtc, X, y, cv=StratifiedKFold(5), scoring="accuracy")
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