from sklearn.neighbors import KNeighborsClassifier
from utils.evaluate import evaluate_model

class knn_model():
    def __init__(self, seed=0):
        self.knn = KNeighborsClassifier()
    
    def train(self, X_train, y_train):
        self.knn.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):
        pred = self.knn.predict(X_test)
        prob = self.knn.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)