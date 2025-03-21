from sklearn.linear_model import LogisticRegression
from utils.evaluate import evaluate_model

class lr_l1_model():
    def __init__(self):
        self.model = LogisticRegression(penalty='l1', solver='saga', max_iter=2000, random_state=42) # max iterations change since the default solver was struggling to converge
        
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)
