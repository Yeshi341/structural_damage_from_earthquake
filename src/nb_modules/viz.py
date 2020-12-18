import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns

def floor_type(df):
    '''
    This function takes the dataframe as an argument
    Returns a categorical plot and saves the figure
    '''
    sns.catplot(y="other_floor_type", hue="target",
                data=df, kind="count",
            height=5, aspect=1.25,legend=False,
               order=df['other_floor_type'].value_counts().index)

    # Set axes labels and title
    plt.xlabel('Number of Buildings')
    plt.ylabel("Floor Type")
    plt.title('Comparison on building damage based on floor type')

    # Set figure legend 
    plt.legend(title='Damage Severity ', loc='lower right', 
           labels=['Severe', 'Major', 'Minor'])
    plt.savefig('./images/Building_damage_on_floor_type', bbox_inches = "tight");
    
def foundation_type(df):
    '''
    This function takes the dataframe as an argument
    Returns a categorical plot and saves the figure
    '''
    
    sns.catplot(y="foundation_type", hue="target",
                data=df, kind="count",
            height=5, aspect=1.25,legend=False,
               order=df['foundation_type'].value_counts().index)

    # Set axes labels and title
    plt.xlabel('Number of Buildings')
    plt.ylabel("Foundation Type")
    plt.title('Comparison on building damage based on Foundation Type')

    # Set figure legend and savefig
    plt.legend(title='Damage Severity ', loc='lower right', 
           labels=['Severe', 'Major', 'Minor'])
    plt.savefig('./images/Building_damage_on_foundation_type.png', bbox_inches = "tight");

def roof_type(df):
    '''
    This function takes the dataframe as an argument
    Returns a categorical plot and saves the figure
    '''
    sns.catplot(y="roof_type", hue="target",
                data=df, kind="count",
            height=5, aspect=1.35,legend=False,
               order=df['roof_type'].value_counts().index)

    # Set axes labels and title
    plt.xlabel('Number of Buildings')
    plt.ylabel("Roof Type")
    plt.title('Comparison on building damage based on Roof Type')

    # Set figure legend and savefig
    plt.legend(title='Damage Severity ', loc='lower right', 
           labels=['Severe', 'Major', 'Minor'])
    plt.savefig('./images/Building_damage_on_Roof_type.png', bbox_inches = "tight");
    
def target_var(df):
    '''
    Function takes in a datframe
    Returns a barchart of the target variable. 
    The label name of the target variable is 'target'
    '''
    print("Proportion of type of Building damage")
    print(round(df['target'].value_counts(normalize=True)*100,2))
    
    # Categorical plot of target variable
    sns.catplot(x="target", kind="count", palette="ch:.25", data=df)
    
    #setting axes label and title
    plt.ylabel('Number of buildings')
    plt.title('Target variable distribution showing Class Imbalance')
    
    #saving fig
    plt.savefig('./images/target_variable_class_imbalance.png', bbox_inches = "tight");
    
def target_var_resample(df):
    '''
    Function takes in a datframe
    Returns a barchart of the target variable. 
    The label name of the target variable is 'target'
    '''
    print("Proportion of type of Building damage")
    print(round(df['target'].value_counts(normalize=True)*100,2))
    
    # Categorical plot of target variable
    sns.catplot(x="target", kind="count", palette="ch:.25", data=df)
    
    #setting axes label and title
    plt.ylabel('Number of buildings')
    plt.title('Target variable distribution')
    
    #saving fig
    plt.savefig('./images/target_variable_Resampled.png', bbox_inches = "tight")

