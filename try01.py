# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 
file = 'C:/Users/karth/Desktop/mark.xlsx'
df1 = pd.read_excel(file)
#df2 = df1.set_index("State", drop = False)
df2 = df1.set_index("NAME")
print ( "the mark of guna is" ,df2.loc["GUNA","MARK3"])
print ("the total of guna is",df2.loc["GUNA","TOTAL"])
df2.ix["GUNA","MARK3"]=90