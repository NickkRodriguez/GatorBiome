from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from utils.evaluate import evaluate_model
from sklearn.model_selection import GridSearchCV

class lda_model():
    def __init__(self):
        self.model = LinearDiscriminantAnalysis()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)

    def getParams(self):
        params ={
            "solver" : ['svd','lsqr','eigen'],
            "shrinkage" : ['auto', None, 0.1 ,0.25, 0.5, 1]
        }
        return params
    
    def initCV(self, params):
        self.grid_search = GridSearchCV(
            estimator=LinearDiscriminantAnalysis(),
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