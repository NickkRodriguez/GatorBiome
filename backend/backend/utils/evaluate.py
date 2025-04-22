import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def evaluate_model(y_true, y_pred, y_prob=None):
    y_true = np.array(y_true).astype(int)
    y_pred = np.array(y_pred).astype(int)
    y_prob = np.array(y_prob) if y_prob is not None else None

    # checking for length mismatches
    if len(y_true) != len(y_pred):
        raise ValueError(f"Mismatch: len(y_true)={len(y_true)} vs len(y_pred)={len(y_pred)}")
    if y_prob is not None and len(y_true) != len(y_prob):
        raise ValueError(f"Mismatch: len(y_true)={len(y_true)} vs len(y_prob)={len(y_prob)}")


    results = {}

    # computing AUC with graceful fallback for multi-class
    if y_prob is not None:
        try:
            results["AUC"] = roc_auc_score(y_true, y_prob)
        except ValueError as e:
            if y_prob.ndim == 2 and y_prob.shape[1] > 1:
                results["AUC"] = roc_auc_score(
                    y_true, y_prob, multi_class="ovr", average="weighted"
                )
            else:
                raise e
    else:
        results["AUC"] = None

    # standard classification metrics
    results["Accuracy"] = accuracy_score(y_true, y_pred)
    results["Precision"] = precision_score(y_true, y_pred, average="weighted", zero_division=0)
    results["Recall"] = recall_score(y_true, y_pred, average="weighted")
    results["F1"] = f1_score(y_true, y_pred, average="weighted")

    # saving prediction arrays for ensemble pipeline
    results["y_pred"] = y_pred.tolist()
    results["y_prob"] = y_prob.tolist() if y_prob is not None else []

    return results
