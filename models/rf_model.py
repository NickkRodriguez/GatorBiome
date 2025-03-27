from sklearn.ensemble import RandomForestClassifier
from utils.evaluate import evaluate_model
from sklearn.model_selection import GridSearchCV
class rf_model():

    def __init__(self, seed=0):
        if(seed==0):
            self.model = RandomForestClassifier(n_estimators=10)
        else:
            self.model = RandomForestClassifier(n_estimators=10, random_state=seed)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)[:, 1]
        return evaluate_model(y_test, pred, prob)

    def getParams(self):
        params ={
            "n_estimators": [25,50,100,150,250,500],
            "criterion":["gini", "entropy", "log_loss"],
            "max_depth":[None, 3,5,10,15,20,25],
            "min_samples_split": [2, 5, 10, 20],
            "min_samples_leaf": [1,2,5,10],
            "max_features":[None, "sqrt", "log2"]
        }
        return params
    
    def initCV(self, params):
        self.grid_search = GridSearchCV(
            estimator=RandomForestClassifier(),
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