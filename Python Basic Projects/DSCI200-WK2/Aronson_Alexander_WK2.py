# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
"""
Created on Fri Jul  8 12:37:15 2022

@author: Alexander Aronson
"""
""" Problem 1 
#Create a data frame with column and index names and shape (4, 3).
#Save the data frame as ‘my_table.csv’


#Problem 2  
#Go to the Canvas Week 2 Module to download the data ‘auto.csv’ to your Week 2 folder. Load the auto data and name it auto.
#Find length and the shape of auto.
#Drop the missing values and name the data auto again (Hint: auto=auto.dropna( ) ).
#Find the column names of auto.
#Find the first 20 rows of auto.
#Select columns ‘car’, ‘cylinders’ and ‘mpg’.
#Select the cell at the third row (row 2)and the fifth column 5(column 4)
#Select the data from row 30 to row 100 within the columns ‘mpg’ and ‘car’
#Sort auto by ‘origin’ and ‘cylinders’
#Drop auto columns ‘displacement’, ‘weight’, ‘acceleration’, and ‘model’ , and name the remaining data as ‘my_auto’
#In the data table my_auto, select the rows by the two conditions: origin is US and mpg greater than 30, and name the selected rows as ‘piece1’
#In the data table my_auto, select the rows by the two conditions: origin is Japan and mpg greater than 30, and name the selected rows as ‘piece2’
#Merge piece1 and piece 2 along rows, name the merged data as ‘auto_new’ and save it to ‘auto_new.xlsx’
#Group auto_new by ‘origin’ and ‘cylinders’, and calculate the mean of other numerical columns.
#####SPACER####################################################################
"""
'Problem 1'

"Create a Data Fame with column and index names and shape (4,3)"
data={'C1':['V1','V2','V3','V4'],'C2':['V5','V6','V7','V8'],'C3':['V9','V10','V11','V12']}
my_table = pd.DataFrame(data)
print(my_table)
###SPACE####
"Save the data frame as 'my_table.csv' "
my_table.to_csv('my_table.csv')
#####SPACER####################################################################
'Problem 2'
###############################################################################
'Go to the Canvas Week 2 Module to download the data ‘auto.csv’ to your Week 2 folder. Load the auto data and name it auto.'
auto= pd.read_csv('auto.csv')
print(auto)

'Find length and the shape of auto.'
print(len(auto))
print(auto.shape)

'Drop the missing values and name the data auto again (Hint: auto=auto.dropna( ) )'
auto=auto.dropna()
print(auto)

'Find the column names of auto.'
print(auto.columns)

'Find the first 20 rows of auto'
auto[0:21]

'Select columns ‘car’, ‘cylinders’ and ‘mpg’'
auto[['car','cylinders','mpg']]

'Select the cell at the third row (row 2)and the fifth column 5(column 4)'
auto.iloc[3,5]

'Select the data from row 30 to row 100 within the columns ‘mpg’ and ‘car’'
auto.loc[30:100,['car','mpg']]

'Sort auto by ‘origin’ and ‘cylinders’'
auto.sort_values(['origin','cylinders'])

'Drop auto columns ‘displacement’, ‘weight’, ‘acceleration’, and ‘model’ , and name the remaining data as ‘my_auto’'
my_auto=auto.drop(['displacement','weight','acceleration','model'],axis=1)
print(my_auto)

'In the data table my_auto, select the rows by the two conditions: origin is US and mpg greater than 30, and name the selected rows as ‘piece1’'
piece1 = auto[(my_auto.origin=='US') & (my_auto.mpg > 30)]
print(piece1)

'In the data table my_auto, select the rows by the two conditions: origin is Japan and mpg greater than 30, and name the selected rows as ‘piece2’'
piece2 =  auto[(my_auto.origin=='Japan') & (my_auto.mpg > 30)]
print(piece2)

'Merge piece1 and piece 2 along rows, name the merged data as ‘auto_new’ and save it to ‘auto_new.xlsx’'
auto_new = pd.concat([piece1,piece2])
print(auto_new)
auto_new.to_excel('auto_new.xlsx')

'Group auto_new by ‘origin’ and ‘cylinders’, and calculate the mean of other numerical columns.'
group_auto_new = auto_new.groupby(['origin','cylinders']).mean()
print(group_auto_new)