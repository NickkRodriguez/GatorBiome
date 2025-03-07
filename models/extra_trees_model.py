from sklearn.ensemble import ExtraTreesClassifier
from utils.evaluate import evaluate_model

class extra_trees_model():
    def __init__(self, seed=42):
        self.et = ExtraTreesClassifier(n_estimators=100, random_state=seed)
    
    def train(self, X_train, y_train):
        self.et.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.et.predict(X_test)
        prob = self.et.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)