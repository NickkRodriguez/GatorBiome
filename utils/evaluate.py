from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def evaluate_model(y_true, y_pred, y_prob=None):
    results = {}
    if y_prob is not None:
        results["AUC"] = roc_auc_score(y_true, y_prob, multi_class="ovr", average="weighted")
    else: results["AUC"] = None
    
    results["Accuracy"] = accuracy_score(y_true, y_pred)
    results["Precision"] = precision_score(y_true, y_pred, average="weighted", zero_division=0)
    results["Recall"] = recall_score(y_true, y_pred, average="weighted")
    results["F1"] = f1_score(y_true, y_pred, average="weighted")
    
    return results