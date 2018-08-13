# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 07:25:06 2018

@author: karth
"""

import pandas as pd
#import re
#import numpy as np
file ='https://raw.githubusercontent.com/Avik-Jain/100-Days-Of-ML-Code/master/datasets/Social_Network_Ads.csv'
df1 = pd.read_csv(file)
#print(df1)
df1.rename(columns={'User ID': 'user'},inplace=True)
df2 = df1.set_index("Gender")
#df1['user'] = df1['user'].replace('0', '5')
print(df2)
##print (df2.loc["Gender","Purchased"])
##print(df2.user)

#num.replace(0, np.nan)
#num = (df2.user)

def convert0to5rec(num):
 
    
    if num == 0:
        return 0
    digit = num % 10
    
    if digit == 0:
        digit = 5
   
    return convert0to5rec(num/10) * 10 + digit
 

def convert0to5(num):
    if num == 0:
        return 5
    else:
        return convert0to5rec(num)
    
num = df1.iloc[:,:-4]
print (convert0to5(num))

    
   # print (df1)
#new_string = re.sub("0", "O",num)
#print(new_string)