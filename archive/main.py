#handles getting dataset
#handles training loop 
#split and preprocesses dataset
#sends training requests to model classes
#averages model evaluation metrics returned by model classes


#import sklearn.datasets
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
#from sklearn.metrics import auc, accuracy_score, precision_score, recall_score, f1_score
#from xgboost import XGBClassifier
import pandas as pd
import numpy as np

#importing models
from models.dt_model import dt_model
from models.rf_model import rf_model
from models.gb_model import gb_model
from models.knn_model import knn_model
from models.lr_model import lr_model

#choose seed for run
seed = 123456
#set number of training runs desired
runs = 10

#Loading wine dataset as proof of concept
df = pd.read_csv("../wine.csv")
target_column = "Wine"
X = df.drop(columns=[target_column])
y = df[target_column]
df.head()

#define helper models
dt = dt_model()
rf = rf_model()
gb = gb_model()
knn = knn_model()
lr = lr_model()

#define results arrays
dtEvalResults = np.zeros((runs, 4))
rfEvalResults = np.zeros((runs,4))
gbEvalResults = np.zeros((runs, 4))
knnEvalResults = np.zeros((runs, 4))
lrEvalResults = np.zeros((runs, 4))

for r in range(runs):
    #first, split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8)

    #next, preprocess data
    #TODO: HANDLE DIFFERENT SCALING
    #TODO: Variance Threshold

    le = LabelEncoder()
    y_train = le.fit_transform(y_train)
    y_test = le.transform(y_test)

    scaler = MinMaxScaler()
    X_train_scaled_standard = scaler.fit_transform(X_train)
    X_test_scaled_standard = scaler.transform(X_test)

    # Training the models and storing the evaluation results
    
    # decision tree
    dt.train(X_train_scaled_standard, y_train)
    dtEvalResults[r] = dt.predict(X_test_scaled_standard, y_test)
    
    # random forest
    rf.train(X_train_scaled_standard, y_train)
    rfEvalResults[r] = rf.predict(X_test_scaled_standard, y_test)
    
    # gradient boosting
    gb.train(X_train_scaled_standard, y_train)
    gbEvalResults[r] = gb.predict(X_test_scaled_standard, y_test)

    # k-nearest neighbors
    knn.train(X_train_scaled_standard, y_train)
    knnEvalResults[r] = knn.predict(X_test_scaled_standard, y_test)
    
    # logistic regression
    lr.train(X_train_scaled_standard, y_train)
    lrEvalResults[r] = lr.predict(X_test_scaled_standard, y_test)

#once done with all models, average the results and score
dt_avg_accuracy = np.mean(dtEvalResults[:,0])
dt_avg_precision = np.mean(dtEvalResults[:,1])
dt_avg_recall = np.mean(dtEvalResults[:,2])
dt_avg_f1 = np.mean(dtEvalResults[:,3])

#print scores
print("Average Accuracy:")
print(dt_avg_accuracy)
print("Average Precision:")
print(dt_avg_precision)
print("Average Recall:")
print(dt_avg_recall)
print("Average F1:")
print(dt_avg_f1)



