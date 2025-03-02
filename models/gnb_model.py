from sklearn.naive_bayes import GaussianNB
from utils.evaluate import evaluate_model

class gnb_model():
    def __init__(self):
        self.gnb = GaussianNB()

    def train(self, X_train, y_train):
        self.gnb.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.gnb.predict(X_test)
        prob = self.gnb.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)