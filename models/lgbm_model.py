from lightgbm import LGBMClassifier
from utils.evaluate import evaluate_model
import pandas as pd


class lgbm_model():

    def __init__(self, seed=0):
        if(seed==0):
            self.lgbm = LGBMClassifier(min_data_in_leaf= 5, verbose=-1, class_weight='balanced')
        else:
            self.lgbm = LGBMClassifier(random_state=seed, min_data_in_leaf= 5, verbose=-1, class_weight='balanced')

    def train(self, X_train, y_train):
        self.lgbm.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):
        pred = self.lgbm.predict(X_test)
        prob = self.lgbm.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)