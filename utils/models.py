from models.dt_model import dt_model
from models.rf_model import rf_model
from models.gb_model import gb_model
from models.xgb_model import xgb_model
from models.lgbm_model import lgbm_model
from models.extra_trees_model import extra_trees_model
from models.adaboost_model import adaboost_model
from models.lr_model import lr_model
from models.lr_l1_model import lr_l1_model
from models.lr_l2_model import lr_l2_model
from models.lr_enet_model import lr_enet_model
from models.svm_linear_model import svm_linear_model
from models.svm_non_linear_model import svm_non_linear_model
from models.knn_model import knn_model
from models.lda_model import lda_model
from models.gnb_model import gnb_model
from models.mlp_model import mlp_model



# model dictionary for pipelines
model_mapping = {
    "Decision Tree": dt_model,
    "Random Forest": rf_model,
    "Gradient Boosting": gb_model,
    "Extreme Gradient Boosting": xgb_model,
    "Light Gradient Boosting Model": lgbm_model,
    "Extremely Randomized Trees": extra_trees_model,
    "Adaptive Boosting": adaboost_model,
    "Logistic Regression": lr_model,
    "Logistic Regression - Lasso (L1)": lr_l1_model,
    "Logistic Regression - Ridge (L2)": lr_l2_model,
    "Logistic Regression - Elastic Net": lr_enet_model,
    "Linear SVM": svm_linear_model,
    "Non-linear SVM": svm_non_linear_model,
    "K-Nearest Neighbors": knn_model,
    "Linear Discriminant Analysis": lda_model,
    "Gaussian Naive Bayes": gnb_model,  
    "Multilayer Perceptron": mlp_model,
}