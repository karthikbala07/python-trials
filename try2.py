# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 06:46:29 2018

@author: karth
"""

import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import summary_table

file = 'https://raw.githubusercontent.com/Avik-Jain/100-Days-Of-ML-Code/master/datasets/Social_Network_Ads.csv'
df1 = pd.read_csv(file)
#df2 = df1.set_index("State", drop = False)
df2 = df1.set_index("Age")
#print(df1)
#dataset = pd.read_csv(file)
#plt.scatter(dataset['Age'],dataset['Gender'])
#df1.plot('Age', ['Gender'])
#plt.show()
def histogram(data, x_label, y_label, title):
    _, ax = plt.subplots()
    ax.hist(data, color = '#539caf')
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)

# Call the function to create plot
histogram(data = df1['EstimatedSalary']
           , x_label = 'Check outs'
           , y_label = 'Frequency'
           , title = 'Distribution of Registered Check Outs')

#df1_filtered = df1.query('Age>35','Gender=Male')
df1_filtered = df1[(df1.Age >= 35) & (df1.Age <= 40) & (df1.Gender == 'Male') & (df1.EstimatedSalary >= 40000) & (df1.Purchased == 1)]
... print(df1_filtered)
