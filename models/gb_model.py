from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import auc, accuracy_score, precision_score, recall_score, f1_score

class gb_model():
    def __init__(self, seed=0):
        self.gb = GradientBoostingClassifier(random_state=seed)
    
    def train(self, X_train, y_train):
        self.gb.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):
        evals = [0] * 4
        pred = self.gb.predict(X_test)
        evals[0] = accuracy_score(y_test, pred)
        evals[1] = precision_score(y_test, pred, average="weighted")
        evals[2] = recall_score(y_test, pred, average="weighted")
        evals[3] = f1_score(y_test, pred, average="weighted")
        return evals
