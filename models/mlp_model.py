from sklearn.neural_network import MLPClassifier
from utils.evaluate import evaluate_model
from sklearn.model_selection import GridSearchCV

class mlp_model():
    def __init__(self, seed=42):
        self.model = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='adam', max_iter=1000, random_state=seed) # max iter change since the default solver was struggling to converge

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)[:, 1]
        return evaluate_model(y_test, pred, prob)

    def getParams(self):
        params ={
            "activation":['identity','logistic','tanh','relu'],
            "solver":['lbfgs', 'sgd','adam'],
            "alpha":[.00001, .0001, .001, .01, .1],
            "batch_size" : ['auto', 10, 50, 100, 200, 400, 750],
            "learning_rate" : ['constant', 'invscaling', 'adaptive'],
            "max_iter" : [50,100,200,400,750,1000]
        }
        return params
    
    def initCV(self, params):
        self.grid_search = GridSearchCV(
            estimator=MLPClassifier(),
            param_grid=params,
            cv=5,
            scoring='accuracy'
        )
    
    def CVTune(self, X_train, y_train, X_test, y_test):
        self.grid_search.fit(X_train, y_train)
    
    def CVResults(self):
        print("Best parameters found: ", self.grid_search.best_params_)
        print("Best score found: ", self.grid_search.best_score_)

    def CVPredict(self, X_test, y_test):
        best_model = self.grid_search.best_estimator_
        test_score = best_model.score(X_test, y_test)
        print("Test set accuracy of the best model: ", test_score)