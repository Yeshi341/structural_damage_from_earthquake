import matplotlib.pyplot as plt
plt.style.use('ggplot')
import matplotlib.ticker as ticker
import seaborn as sns

def floor_type(df):
    '''
    This function takes the dataframe as an argument
    Returns a count plot and saves the figure
    '''
    fig, ax = plt.subplots(figsize=(9,7))

    sns.countplot(ax= ax, y="other_floor_type", hue="target",
                data=df, order=df['other_floor_type'].value_counts().index)

    # Set axes ticks
    ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax = 762106))
    ax.tick_params(axis='both',labelsize=15)
    
    # Set axes labels and title
    ax.set_xlabel('Percentage of Buildings', size = 15, labelpad=10)
    ax.set_ylabel("Floor Type", size = 15)
    ax.set_title('Comparison on building damage based on floor type', size = 17, pad =18)
    
    # Set axes legend and save figure
    ax.legend(title='Damage Severity ', loc='lower right', labels=['Severe', 'Major', 'Minor'], fontsize = 15)
    fig.savefig('./images/Building_damage_on_floor_type.png', bbox_inches = "tight");
    
def foundation_type(df):
    '''
    This function takes the dataframe as an argument
    Returns a categorical plot and saves the figure
    '''
    # Set figure, axes and draw
    fig, ax = plt.subplots(figsize= (9,7))
    sns.countplot(ax= ax,y="foundation_type", hue="target",
                data=df, order=df['foundation_type'].value_counts().index)
    
    # Set axes ticks
    ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=762106))
    ax.tick_params(axis='both', labelsize=15)
    
    # Set axes labels and title
    ax.set_xlabel('Percentage of Buildings', size=15, labelpad = 10)
    ax.set_ylabel("Foundation Type", size = 15)
    ax.set_title('Comparison on building damage based on Foundation Type', size= 17, pad =18)

    # Set axes legend and savefig
    ax.legend(title='Damage Severity ', loc='lower right', labels=['Severe', 'Major', 'Minor'], fontsize = 15)
    fig.savefig('./images/Building_damage_on_foundation_type.png', bbox_inches = "tight");

def roof_type(df):
    '''
    This function takes the dataframe as an argument
    Returns a categorical plot and saves the figure
    '''
    # Set figure, axes and draw
    fig, ax = plt.subplots(figsize=(9,7))
    sns.countplot(ax=ax,y="roof_type", hue="target",
                data=df,order=df['roof_type'].value_counts().index)

    # Set axes ticks
    ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax = 762106))
    ax.tick_params(axis='both', labelsize=15)
    
    # Set axes labels and title
    ax.set_xlabel('Percentage of Buildings', size = 15, labelpad=10)
    ax.set_ylabel("Roof Type", size = 15)
    ax.set_title('Comparison on building damage based on Roof Type', size = 17, pad =18)

    # Set figure legend and save fig
    ax.legend(title='Damage Severity ', loc='lower right', labels=['Severe', 'Major', 'Minor'], fontsize=15)
    fig.savefig('./images/Building_damage_on_Roof_type.png', bbox_inches = "tight");
    
def target_var(df, title, figname, xmax):
    '''
    Function takes in a datframe
    Returns a barchart of the target variable. 
    The label name of the target variable is 'target'
    '''
    print("Proportion of type of Building damage")
    print(round(df['target'].value_counts(normalize=True)*100,2))
    
    # Set up figure, axes and draw the plot
    fig, ax = plt.subplots(figsize=(8,6))
    sns.countplot(x="target", palette="ch:.25", data=df)
    
    #Set axes ticks
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax = xmax))
    ax.tick_params(axis='both', labelsize= 15)
    
    #set axes label and title
    ax.set_ylabel('Percentage of buildings', size=15)
    ax.set_xlabel('Degree of Building Damage', size = 15)
    ax.set_title(title, size=17, pad= 10)
    
    #save fig
    fig.savefig('./images/{}.png'.format(figname), bbox_inches = "tight");
    
# def target_var_resample(df):
#     '''
#     Function takes in a datframe
#     Returns a barchart of the target variable. 
#     The label name of the target variable is 'target'
#     '''
#     print("Proportion of type of Building damage")
#     print(round(df['target'].value_counts(normalize=True)*100,2))
    
#     # Set up figure, axes and draw plot
#     fig,
#     sns.catplot(x="target", kind="count", palette="ch:.25", data=df)
    
#     #setting axes label and title
#     plt.ylabel('Number of buildings')
#     plt.title('Target variable distribution')
    
#     #saving fig
#     plt.savefig('./images/target_variable_Resampled.png', bbox_inches = "tight")

