from sklearn.linear_model import LogisticRegression
from utils.evaluate import evaluate_model

class lr_model():
    def __init__(self, seed=0):
        self.model = LogisticRegression(random_state=seed)
    
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)