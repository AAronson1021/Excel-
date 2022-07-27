# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 18:10:26 2022

@author: Alexander Aronson
"""

import pandas as pd
import numpy as np
"""

1. Load the data 'Top 100 Retailers 2015.csv  Download Top 100 Retailers 2015.csv' from Canvas Week 3 Module and name it 'Top_100'.

Name the index of Top_100 as Company (Hint: Top_100.index=Top_100.Company).

Delete the missing data if possible.

2. Select the companies with 10<Rank <=20 and name the 10 companies as a new data frame named 'Top_20', and sort 'Top_20' by Rank with ascending =True.

Save Top_20 to an excel file named 'Top_20.xlsx'

3. For the data frame 'Top_20',

    a) plot the bar chart of 'Worldwide_Retail_Sales_million', with x='Company'

    b) plot the horizontal bar chart of both 'USA_Retail_Sales_million' and 'Worldwide_Retail_Sales_million', with x='Company', rot=45 , stacked=True.

Save the figure as 'bar_chart.png'.

    c) plot pie charts for both 'USA_Retail_Sales_million' and 'Worldwide_Retail_Sales_million', with figsize=(16, 8), autopct=%1.1f%%, legend=False, subplots=True.

Save the figure as 'pie_chart.png'

4. For the data frame 'Top_100',

    a) plot lines of 'USA_Retail_Sales_million' and 'Worldwide_Retail_Sales_million'

    b) plot the histograms of all the numerical columns in Top_100 with bins=10, figsize=(6,8).

     Save the figure as 'histogram.png'

    c) plot the histogram of 'USA_percentage_Worldwide_Sales' in Top_100 with bins=20.

    d) graph scatter plot of 'USA_percentage_Worldwide_Sales' with x='USA_Retail_Sales_million', alpha=0.4, c='Rank', cmap=plt.get_cmap("jet"), colorbar=True.

      Save the figure as 'scatter.png'

    e) graph scatter plots for both 'USA_Retail_Sales_million' and Worldwide_Retail_Sales_million' with x='Rank' in one graph. Save the figure as 'scatter2.png'

    f) plot the scatter matrix for 'Top_100'. Save the figure as 'scatter matrix.png'

    g) graph the boxplot of 'USA_percentage_Worldwide_Sales'. Save the figure as 'boxplot.png'
"""
#######################%%SPACER%%############################################################################################
'Question 1'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Top_100=pd.read_csv('Top100.csv')
Top_100.index=Top_100.Company
Top_100=Top_100.dropna()
Top_100.shape

'Question 2'
Top_20=Top_100[(Top_100.Rank > 10) & (Top_100.Rank <= 20)]
print(Top_20)
Top_20.to_excel('Top_20.xlsx')

'Question 3'
'A)'
Top_20.plot.bar(y='Worldwide_Retail_Sales_million', x='Company')
plt.show()

'B)'
Top_20.plot.barh(stacked=True, y=['Worldwide_Retail_Sales_million','USA_Retail_Sales_million'], x='Company',rot=45)
plt.show()
'Save the figure as bar_chart.png'

'C)'
Pie_20=Top_20[['Worldwide_Retail_Sales_million','USA_Retail_Sales_million']]
Pie_20.plot.pie(figsize=(16, 8), autopct='%1.1f%%', legend=False, subplots=True)
'Save the figure as pie_chart.png'

'Question 4'
'A)'
Top_100.plot(y=['USA_percentage_Worldwide_Sales','Worldwide_Retail_Sales_million'],figsize=(20,10))
plt.show()

'B)'
Top_100.hist(bins=10, figsize=(6,8))
plt.show()

'C)'
Top_100.hist(column=['USA_percentage_Worldwide_Sales'],bins=20,figsize=(6,8))
plt.show()

'D)'
Top_100.plot.scatter(y='USA_percentage_Worldwide_Sales', x='USA_Retail_Sales_million', alpha=0.4, c='Rank', cmap=plt.get_cmap("jet"), colorbar=True)
plt.show()

'E)'

ax1= Top_100.plot.scatter(x='Rank', y='USA_Retail_Sales_million', c='y', marker='s',label='USA_Retail_Sales_million')
Top_100.plot.scatter(x='Rank',y='Worldwide_Retail_Sales_million', c='g', marker='o', label='Worldwide_Retail_Sales_million', ax=ax1)
plt.show()

'F)'
pd.plotting.scatter_matrix(Top_100, alpha=0.4, figsize=(15, 15))
plt.show()

'G)'
Top_100.boxplot(column='USA_percentage_Worldwide_Sales',grid=True)
plt.show()

















