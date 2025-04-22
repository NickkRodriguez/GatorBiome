from sklearn.svm import SVC
from utils.evaluate import evaluate_model

class svm_non_linear_model():
    def __init__(self):
        # rbf for complex non-linear relationships (open to change)
        self.model = SVC(kernel='rbf', probability=True) # set to true for auc
        
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)[:, 1]
        return evaluate_model(y_test, pred, prob)