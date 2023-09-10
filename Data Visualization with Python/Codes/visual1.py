#matplotlib inLine
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd


#Histogram with 100 random values
x = np.random.randn(10000)
plt.hist(x,100)     # 100 represents no. of bins
plt.title(r'Normal distribution with $\mu=0, \sigma=1$')
plt.show()

#Alternative to display plots
#df.plot(kind="list")

#url='E:\BasicPythonCode\Data Analysis\Data Visualization with Python\Canada.xlsx'


#Reading Dataframe
df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')

#Show first five rows of the data
des=df_can.describe(include = "all")
print(df_can)
print(df_can.columns)
#df_can.set_index('Country', inplace=True)

#ypoints = np.array(df_can['Country'])#:'Haiti'])

#plt.plot(ypoints)


#Line plot
years = list(map(str, range(1980, 2014)))
ypoints = np.array(df_can['Country'])
plt.title('Immigration from all countries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.plot(ypoints)
plt.show()

#Area Plot

sort=df_can.sort_values(['Total'],ascending=False,axis=0,inplace = True) #For descending #by=['Total']
print(df_can)

headers=["India","China","United Kingdom","Philippiines","Pakistan"]
#Transpose
top5=df_can.head()
top5= top5[years].transpose()
top5.columns = headers
print(top5)


top5.plot(kind='area')
plt.title('Immigration trends of top five countries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()

#Histogram
count, bin_edges = np.histogram(df_can['2013'])  # To display proper ranging in xlabel to read data appropriately 
df_can['2013'].plot(kind='hist',xticks=bin_edges)
plt.title('Histogram of Immigration from 195 countries in 2013')
plt.xlabel('Number of immigrants')
plt.ylabel('Number of Countries')
plt.show()

#Bar chart
Years = list(map(str, range(1980, 2014)))
#df_iceland = df_can.loc['Iceland',Years]    #kind=barh for horizontal bar chart
#df_iceland.plot(kind='bar')
#plt.title('Bar chart of Immigrants from Iceland to Canada till 2014')
#plt.ylabel('Number of immigrants')
#plt.xlabel('Years')
#plt.show()

#Pie Chart
df_continents=df_can.groupby('Continent',axis=0).sum()
#print(df_continents)
df_continents['Total'].plot(kind='pie',figsize=(7,7),
                            autopct='%1.1f%%',labels=None,pctdistance=1.12,startangle=45)   # the ratio between the center of each pie slice and the start of the text generated by autopct 
                             # add in percentages     # ,startangle=90, shadow=True)
plt.title('Pie chart of Immigrants from all Continents to Canada from 1980 to 2014')
#plt.axis('equal')
plt.legend(labels=df_continents.index, loc='lower left')
plt.show()


#Box plot
df_asia=df_continents.groupby('Country',axis=0).sum()
top=df_asia
top= top[years].transpose()
print(top)
#df_japan=df_can.loc[df_can['Japan'],years].transpose()
#top['Australia'].plot(kind='box')
#plt.title('Box plot of Immigrants from Japan from 1980 to 2014')
#plt.xlabel('Number of immigrants')
#plt.show()

#Scatter plot
#x=['1980', '1981', '1982',
 #      '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991',
 #      '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000',
 #      '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
 #      '2010', '2011', '2012', '2013']
#y=['Total']
#plt.scatter(x,y)
#plt.title('Box plot of Immigrants from Japan from 1980 to 2014')
#plt.ylabel('Number of immigrants')
#plt.xlabel('Years')
#plt.show()