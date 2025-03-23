from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def evaluate_model(y_true, y_pred, y_prob=None):
    metrics = []
    
    metrics.append(accuracy_score(y_true, y_pred))
    #metrics.append(precision_score(y_true, y_pred, average="weighted"))
    metrics.append(precision_score(y_true, y_pred, average="weighted", zero_division=0)) # struggling with undefined values
    metrics.append(recall_score(y_true, y_pred, average="weighted"))
    metrics.append(f1_score(y_true, y_pred, average="weighted"))
    
    if y_prob is not None:
        auc_score = roc_auc_score(y_true, y_prob, multi_class="ovr", average="weighted")
    else:
        auc_score = None

    metrics.append(auc_score)
        
    return metrics
