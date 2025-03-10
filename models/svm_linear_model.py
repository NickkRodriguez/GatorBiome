from sklearn.svm import SVC
from utils.evaluate import evaluate_model

class svm_linear_model():
    def __init__(self):
        self.model = SVC(kernel='linear', probability=True) # set to true for auc

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)