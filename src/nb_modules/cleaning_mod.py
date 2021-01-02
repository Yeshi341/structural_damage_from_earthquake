# importing utility packages
import pandas as pd
import numpy as np

# importing graphing packages
import matplotlib.pyplot as plt
import seaborn as sns

# Series converter
def convert_to_num(df, to_convert_feature, converted_feature):
    
    '''
    Function creates a numeric series corresponding to a 
    nominal series
    
    Note: The number representing the nominal value is 
    in order of proportion of values in the series.
    
    Parameters :
    -----------
    df : unquoted str
         dataframe to which the feature to be converted
         belongs to. Also the dataframe where the new 
         feature will be added
    
    to_convert_feature : str
                         the dataframe label of the nominal
                         column that needs to be converted
        
    converted_feature : str
                        the dataframe label to give to the 
                        new numeric column
                        
    Returns :
    --------
    Returns the numeric converted series containing counts
    of unique values sorted in frequencies '''
    
    # defining count index
    count_index = list(df[to_convert_feature].value_counts().index)
    
    # defining choice of numeric value
    choices = range(1, len(count_index)+1)
    
    # defining and adding conditions to list
    conditions = []
    for value in count_index:
        conditions.append(df[to_convert_feature] == value)
    
    # making value selection based on conditions
    df[converted_feature]= np.select(conditions, choices)
    
    return df[converted_feature].value_counts()