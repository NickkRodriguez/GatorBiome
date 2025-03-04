from xgboost import XGBClassifier
from utils.evaluate import evaluate_model

class xgb_model():
    def __init__(self, seed=42):
        self.xgb = XGBClassifier(eval_metric="logloss", random_state=seed)

    def train(self, X_train, y_train):
        self.xgb.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.xgb.predict(X_test)
        prob = self.xgb.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)