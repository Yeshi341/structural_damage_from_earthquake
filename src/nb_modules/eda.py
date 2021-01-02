import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def dict_to_fig(feat_list, df, title, ylabel, figname):
    '''
    Function creates a dictionary of values representing
    the count of records belonging to a label and draws
    a count plot of the labels
    
    Note: the figure from the function is saved under
    the images folder in the main directory of the repo
    
    Parameters :
    -----------
    feat_list : list (str)
                list of labels
    
    df : unquoted str
         name of dataframe 
         
    title : str
            title name to give the plot figure
    
    ylabel : str
             plot y axis label
    
    figname : str
              name to save the plot figure as
              
    Returns :
    --------
    Returns a horizontal bar plot showing the dictionary items
    '''
    
    # Defines and creates dictionary
    building_count= {}
    for label in feat_list:
        building_count[label]=round((df[label].value_counts(normalize=True, ascending=True)[1])*100,2)
    # print(building_count)
    
    # isolates x and y axis values from dictionary
    x=list(building_count.keys())
    y=list(building_count.values())
    
    # Sets up figure , axes and draws bar plot
    fig, ax = plt.subplots(figsize=(11,7))
    ax.barh(x, y)
    
    # Formats axis ticks as percentages
    ax.xaxis.set_major_formatter(ticker.PercentFormatter())
    ax.tick_params(axis='both', labelsize=15);
    
    # Set axes labels and title
    ax.set_xlabel('Percentage of Buildings', size = 15)
    ax.set_ylabel(ylabel, size=15)
    ax.set_title(title, size= 17, pad=17)
    
    # Saves figure in images folder of main repo directory
    fig.savefig('./images/{}.png'.format(figname), bbox_inches = "tight");
    return
    

def valuecounts(feature, df):
    '''
    Function returns a series containing the percentage 
    of unique values to 2 decimal points
    
    Parameters :
    -----------
    feature : str
              series label
    
    df : unquoted str
         dataframe name
         
    Returns : 
    --------
    The percentage of unique values up to 2 decimal points
    '''
    print(round(df[feature].value_counts(normalize=True)*100,2))
    return 

def box_hist(df, feature):
    '''
    Function draws two subplots.
    
    Parameteres :
    ------------
    df : unquoted str
         dataframe name
         
    feature : str
              series label
    
    Returns :
    --------
    Subplots of boxplot and histogram representation of feature
    '''
    figure, axs = plt.subplots(1,2, figsize=(9,5))
    axs[0].boxplot(df[feature],1)
    axs[0].set_title('{} Boxplot'.format(feature))
    axs[1].hist(df[feature])
    axs[1].set_title('{} Histogram'.format(feature))
    plt.subplots_adjust(bottom=0.15, wspace=0.25);
    return