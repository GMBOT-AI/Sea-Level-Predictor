import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    sns.scatterplot(x='Year',y='CSIRO Adjusted Sea Level', data=df ,s=70)

    # Create first line of best fit
    slope1, intercept1, _, _, _ = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    years1=pd.Series(range(df['Year'].min(),2051))
    pred1= slope1 * years1 +intercept1 
    # Create second line of best fit
    df_2 = df[df['Year']>=2000]
    slope2, intercept2, _, _, _ = linregress(df_2['Year'],df_2['CSIRO Adjusted Sea Level'])
    years2 = pd.Series(range(2000,2051))
    pred2 = slope2 * years2 + intercept2
    # Add labels and title
    plt.plot(years1,pred1,label='1880-2050',color='red')
    plt.plot(years2,pred2, label='2000-2050' ,color='green')
    plt.xlabel('Year')
    plt.ylabel('Sea Level(Inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()