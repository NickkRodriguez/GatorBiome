from sklearn.ensemble import RandomForestClassifier
from utils.evaluate import evaluate_model

class rf_model():

    def __init__(self, seed=0):
        if(seed==0):
            self.model = RandomForestClassifier(n_estimators=10)
        else:
            self.model = RandomForestClassifier(n_estimators=10, random_state=seed)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)