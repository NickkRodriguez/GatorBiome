from sklearn.tree import DecisionTreeClassifier
from utils.evaluate import evaluate_model

class dt_model():
    
    def __init__(self, seed=0):
        if(seed==0):
            self.dt = DecisionTreeClassifier()
        else:
            self.dt = DecisionTreeClassifier(random_state=seed)

    def train(self, X_train, y_train):
        self.dt.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):
        pred = self.dt.predict(X_test)
        prob = self.dt.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)
