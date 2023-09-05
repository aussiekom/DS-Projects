# 911 CALLS PROJECTS
import numpy as np
import pandas as pd

# visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

df = pd.read_csv('/10-Data-Capstone-Projects/911.csv')
df.info()
df.head(3)

#%%
# What are the top 5 zipcodes for 911 calls?
df['zip'].value_counts().head(5)

# What are the top 5 townships (twp) for 911 calls?
df['twp'].value_counts().head(5)

# Take a look at the 'title' column, how many unique title codes are there?
df['title'].nunique()

#%%
# creating a new column 'Reason' with .apply()
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])

# the most common Reason for a 911 call based off of this new column
df['Reason'].value_counts()

# create a countplot of 911 calls by Reason with seaborn
sns.countplot(x='Reason',data=df,palette='viridis')

# data type of the objects in the timeStamp column
type(df['timeStamp'].iloc[0])

# convert the column from strings to DateTime objects
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

#%%
# creating three new columns with .apply()
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)

#  create a countplot of the Day of Week column with the hue based off of the Reason column
sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')

# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# same for Month
sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')

# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#%%
# data of 9,10 and 11 months was missing
# create a gropuby object called byMonth, where you group the DataFrame by the month column
byMonth = df.groupby('Month').count()
byMonth.head()

#%%
# create a simple plot off of the dataframe indicating the count of calls per month
byMonth['twp'].plot()

# create a linear fit on the number of calls per month
sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())

# create a new column called 'Date' that contains the date from the timeStamp column
df['Date']=df['timeStamp'].apply(lambda t: t.date())

# aggregate and create a plot of counts of 911 calls
df.groupby('Date').count()['twp'].plot()
plt.tight_layout()

# create 3 separate plots with each plot representing a Reason for the 911 call
# reason = traffic
df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()

# reason = fire
df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()

# reason = EMS
df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()


#%%
# restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week
dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
dayHour.head()

# create a HeatMap using this new DataFrame
plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')

# create a clustermap using this DataFrame
sns.clustermap(dayHour,cmap='viridis')


