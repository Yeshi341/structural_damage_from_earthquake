import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def convert_to_num(df, to_convert_feature, converted_feature):
    count_index = list(df[to_convert_feature].value_counts().index)
    choices = range(1, len(count_index)+1)
    conditions = []
    for value in count_index:
        conditions.append(df[to_convert_feature] == value)
    df[converted_feature]= np.select(conditions, choices)
    return df[converted_feature].value_counts()