from sklearn.linear_model import LogisticRegression
from utils.evaluate import evaluate_model

class lr_l2_model():
    def __init__(self, seed=42):
        self.model = LogisticRegression(penalty='l2', solver='lbfgs', max_iter=2000, random_state=seed)
        
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)[:, 1]
        return evaluate_model(y_test, pred, prob)
