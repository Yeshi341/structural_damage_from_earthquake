import pandas as pd
import numpy as np


def dummify(df, feature):
    dummy= pd.get_dummies(df[feature],drop_first= True, prefix=feature)
    return dummy