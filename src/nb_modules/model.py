import pandas as pd
import numpy as np
from sklearn.metrics import recall_score, make_scorer, f1_score

def dummify(df, feature):
    dummy= pd.get_dummies(df[feature],drop_first= True, prefix=feature)
    return dummy


def recall_score_class(y_true, y_pred):
    scorer= recall_score(y_true, y_pred, average=None)[2]
    return scorer

def scorer_recall():
    scorer = make_scorer(recall_score_class)
    return scorer

def f1_score_class(y_true, y_pred):
    scorer= f1_score(y_true, y_pred, average=None)[2]
    return scorer

def scorer_f1():
    scorer = make_scorer(f1_score_class)
    return scorer