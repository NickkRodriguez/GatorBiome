from sklearn.ensemble import GradientBoostingClassifier
from utils.evaluate import evaluate_model

class gb_model():
    def __init__(self, seed=0):
        self.gb = GradientBoostingClassifier(random_state=seed)
    
    def train(self, X_train, y_train):
        self.gb.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):
        pred = self.gb.predict(X_test)
        prob = self.gb.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)
