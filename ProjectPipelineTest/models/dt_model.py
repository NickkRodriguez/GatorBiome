from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import auc, accuracy_score, precision_score, recall_score, f1_score
#import pandas as pd
#import numpy as np

class dt_model():

    dt = DecisionTreeClassifier

    def __init__(self, seed=0):
        if(seed==0):
            self.dt = DecisionTreeClassifier()
        else:
            self.dt = DecisionTreeClassifier(random_state=seed)

    def train(self, X_train, y_train):
        self.dt.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):

        evals = [0] * 4
        pred = self.dt.predict(X_test)
        evals[0] = accuracy_score(y_test, pred)
        evals[1] = precision_score(y_test, pred, average="weighted")
        evals[2] = recall_score(y_test, pred, average="weighted")
        evals[3] = f1_score(y_test, pred, average="weighted")

        return evals