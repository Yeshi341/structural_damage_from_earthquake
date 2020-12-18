import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def dict_maker(feat_list, df):
    '''
    Takes in a list of feature names
    Returns a dictionary of features with its value_counts as values
    and draws a horizontal bar plot to show the dictionary items
    '''
    building_count= {}
    for use in feat_list:
        building_count[use]=df[use].value_counts(ascending=True)[1]
    print(building_count)
    x=list(building_count.keys())
    y=list(building_count.values())
    
    plt.figure(figsize=(10,5))
    plt.barh(x, y);
    return
    

def valuecounts(feature, df):
    '''
    Takes in feature and pandas dataframe
    returns the normalized proportions of the features in percentage up to 2 decimals
    '''
    print(round(df[feature].value_counts(normalize=True)*100,2))
    return 

def box_hist(df, feature):
    figure, axs = plt.subplots(1,2, figsize=(9,5))
    axs[0].boxplot(df[feature],1)
    axs[0].set_title('{} Boxplot'.format(feature))
    axs[1].hist(df[feature])
    axs[1].set_title('{} Histogram'.format(feature))
    plt.subplots_adjust(bottom=0.15, wspace=0.25);
    return