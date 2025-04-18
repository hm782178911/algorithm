import numpy as np
from sklearn.metrics import roc_auc_score, accuracy_score

def evaluate(y_true, y_pred):
    """计算AUC和准确率"""
    auc = roc_auc_score(y_true, y_pred)
    acc = accuracy_score(y_true, (y_pred >= 0.5).astype(int))
    return {"AUC": auc, "Accuracy": acc}