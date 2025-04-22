from sklearn.neural_network import MLPClassifier
from utils.evaluate import evaluate_model
from sklearn.model_selection import GridSearchCV

import optuna
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
import numpy as np
import os


class mlp_model():
    def __init__(self, seed=42):
        self.model = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='adam', max_iter=1000, random_state=seed) # max iter change since the default solver was struggling to converge

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)[:, 1]
        return evaluate_model(y_test, pred, prob)

    def objective(self, trial, X, y):
        activation = trial.suggest_categorical("activation", ['identity','logistic','tanh','relu'])
        solver = trial.suggest_categorical("solver", ['lbfgs', 'sgd','adam'])
        learning_rate = trial.suggest_categorical("learning_rate", ['constant', 'invscaling', 'adaptive'])
        batch_size = trial.suggest_int("batch_size", 10,500)
        alpha = trial.suggest_float("alpha", .00001, 1)
        max_iter = trial.suggest_int("max_iter", 25, 500)
        mlp = MLPClassifier(activation=activation,
                            solver=solver,
                            learning_rate=learning_rate,
                            batch_size=batch_size,
                            alpha=alpha,
                            max_iter=max_iter)

        try:
            score = cross_val_score(mlp, X, y, cv=StratifiedKFold(5), scoring="accuracy")
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