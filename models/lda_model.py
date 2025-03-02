from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from utils.evaluate import evaluate_model

class lda_model():
    def __init__(self):
        self.lda = LinearDiscriminantAnalysis()

    def train(self, X_train, y_train):
        self.lda.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.lda.predict(X_test)
        return evaluate_model(y_test, pred)