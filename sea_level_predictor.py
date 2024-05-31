import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', index_col = 'Year')

    # Create scatter plot
    plt.scatter(data = df, x = df.index, y = 'CSIRO Adjusted Sea Level')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df.index, df['CSIRO Adjusted Sea Level'])
    extended_year = np.arange(df.index[0], 2051, 1)
    plt.plot(extended_year, intercept + slope * extended_year, 'r')

    # Create second line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df.index[list(df.index).index(2000):], df['CSIRO Adjusted Sea Level'].loc[df.index >= 2000])
    extended_year = np.arange(df.index[list(df.index).index(2000)], 2051, 1)
    plt.plot(extended_year, intercept + slope * extended_year, 'b')

    # Add labels and title
    plt.xlabel("Year", fontsize = 10)
    plt.ylabel("Sea Level (inches)", fontsize = 10)
    plt.title("Rise in Sea Level", fontsize = 10)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()