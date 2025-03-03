from sklearn.neural_network import MLPClassifier
from utils.evaluate import evaluate_model

class mlp_model():
    def __init__(self, seed=42):
        self.mlp = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='adam', max_iter=1000, random_state=seed) # max iter change since the default solver was struggling to converge

    def train(self, X_train, y_train):
        self.mlp.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.mlp.predict(X_test)
        prob = self.mlp.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)