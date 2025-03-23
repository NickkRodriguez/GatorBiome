from sklearn.neighbors import KNeighborsClassifier
from utils.evaluate import evaluate_model
from sklearn.model_selection import GridSearchCV

class knn_model():
    def __init__(self, seed=0):
        self.model = KNeighborsClassifier()
    
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)

    def getParams(self):
        params ={
            "n_neighbors" : [1,3,5,10,15],
            "weights" : ['uniform', 'distance'],
            "algorithm" : ['auto', 'ball_tree', 'kd_tree', 'brute'],
            "leaf_size" : [10, 30, 50, 75],
            "p" : [1, 2, 5]

        }
        return params
    
    def initCV(self, params):
        self.grid_search = GridSearchCV(
            estimator=KNeighborsClassifier(),
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