from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(y_true, y_pred):
    metrics = []
    
    metrics.append(accuracy_score(y_true, y_pred))
    metrics.append(precision_score(y_true, y_pred, average="weighted"))
    metrics.append(recall_score(y_true, y_pred, average="weighted"))
    metrics.append(f1_score(y_true, y_pred, average="weighted"))
    
    return metrics