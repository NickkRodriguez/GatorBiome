from lightgbm import LGBMClassifier
from sklearn.model_selection import GridSearchCV
from utils.evaluate import evaluate_model
import pandas as pd


class lgbm_model():

    def __init__(self, seed=0):
        if(seed==0):
            self.model = LGBMClassifier(min_data_in_leaf= 5, verbose=-1, class_weight='balanced')
        else:
            self.model = LGBMClassifier(random_state=seed, min_data_in_leaf= 5, verbose=-1, class_weight='balanced')

    #initialize GridSearchCV with given param grid
    def initCV(self, params):
        self.grid_search = GridSearchCV(
            estimator=LGBMClassifier(),
            param_grid=params,
            cv=5,
            scoring='accuracy'
        )

    #Tune CV with trianing set and eval set
    def CVTune(self, X_train, y_train, X_test, y_test):
        self.grid_search.fit(X_train, y_train, eval_set=[(X_test, y_test)])
    
    #get results
    def CVResults(self):
        print("Best parameters found: ", self.grid_search.best_params_)
        print("Best score found: ", self.grid_search.best_score_)

    #predict
    def CVPredict(self, X_test, y_test):
        best_model = self.grid_search.best_estimator_
        test_score = best_model.score(X_test, y_test)
        print("Test set accuracy of the best model: ", test_score)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test, y_test):
        pred = self.model.predict(X_test)
        prob = self.model.predict_proba(X_test)
        return evaluate_model(y_test, pred, prob)

    def getParams(self):
        params = {
            "num_leaves" : [30,50,100],
            "min_data_in_leaf" : [5, 10, 15,20],
            "max_depth" : [1,5,10,20],
            "learning rate" : [.001, .01, .05, .1],
            "num_iterations" : [10,25,50,75,100]
        }
        return params