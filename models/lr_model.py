from sklearn.linear_model import LogisticRegression
from utils.evaluate import evaluate_model
from sklearn.model_selection import GridSearchCV

#Because lr enet, lr l1, and lr l2 are all LR, just 1 gridsearchcv is needed
class lr_model():
    def __init__(self, seed=42):
        self.model = LogisticRegression(solver='lbfgs', max_iter=2000, random_state=seed)
    
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)[:, 1]
        return evaluate_model(y_test, pred, prob)

    def getParams(self):
        params ={
            "penalty" : ['l1','l2','elasticnet', None],
            "dual": [True, False],
            "solver":['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'],
            "multi_class":['auto', 'ovr', 'multinominal'],
            "max_iter":[25,50,100,500,1000,5000]
        }
        return params
    
    def initCV(self, params):
        self.grid_search = GridSearchCV(
            estimator=LogisticRegression(),
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