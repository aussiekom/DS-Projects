# for manipulations
import numpy as np
import pandas as pd

# for data visualizations
import seaborn as sns
import matplotlib.pyplot as plt

# for interactivity
from ipywidgets import interact

# %%
# read the dataset
data = pd.read_csv('/Users/janekom/Library/Containers/com.microsoft.Excel/Data/Desktop/data.csv')

# check the shape of the dataset
print('Shape of the Dataset is: ', data.shape)

# check the head of the ds
data.head()

# check the missing values
# 0s everywhere which means there is no missing values
data.isnull().sum()

# check the crops present in this ds
data['label'].value_counts()

# %%
# check summary for all the crops
print('Average Ratio of Nitrogen in the Soil: {0:.2f}'.format(data['N'].mean()))
print('Average Ratio of Phosphorous in the Soil: {0:.2f}'.format(data['P'].mean()))
print('Average Ratio of Potassium in the Soil: {0:.2f}'.format(data['K'].mean()))
print('Average Temperature in Celsius: {0:.2f}'.format(data['temperature'].mean()))
print('Average Relative Humidity in %: {0:.2f}'.format(data['humidity'].mean()))
print('Average PH Value of the soil: {0:.2f}'.format(data['ph'].mean()))
print('Average Rainfall in mm: {0:.2f}'.format(data['rainfall'].mean()))


# %%
# check the summary statistics for each of the crops
@interact
def summary(crops=list(data['label'].value_counts().index)):
    x = data[data['label'] == crops]
    print('-----------------------')
    print('Statistics for Nitrogen')
    print('Minimum Nitrogen required: {0:.2f}'.format(x['N'].min()))
    print('Average Nitrogen required: {0:.2f}'.format(x['N'].mean()))
    print('Maximum Nitrogen required: {0:.2f}'.format(x['N'].max()))
    print('-----------------------')
    print('Statistics for Phosphorous')
    print('Minimum Phosphorous required: {0:.2f}'.format(x['P'].min()))
    print('Average Phosphorous required: {0:.2f}'.format(x['P'].mean()))
    print('Maximum Phosphorous required: {0:.2f}'.format(x['P'].max()))
    print('-----------------------')
    print('Statistics for Potassium')
    print('Minimum Potassium required: {0:.2f}'.format(x['K'].min()))
    print('Average Potassium required: {0:.2f}'.format(x['K'].mean()))
    print('Maximum Potassium required: {0:.2f}'.format(x['K'].max()))
    print('-----------------------')
    print('Statistics for Temperature')
    print('Minimum Temperature required: {0:.2f}'.format(x['temperature'].min()))
    print('Average Temperature required: {0:.2f}'.format(x['temperature'].mean()))
    print('Maximum Temperature required: {0:.2f}'.format(x['temperature'].max()))
    print('-----------------------')
    print('Statistics for Humidity')
    print('Minimum Humidity required: {0:.2f}'.format(x['humidity'].min()))
    print('Average Humidity required: {0:.2f}'.format(x['humidity'].mean()))
    print('Maximum Humidity required: {0:.2f}'.format(x['humidity'].max()))
    print('-----------------------')
    print('Statistics for PH')
    print('Minimum PH required: {0:.2f}'.format(x['ph'].min()))
    print('Average PH required: {0:.2f}'.format(x['ph'].mean()))
    print('Maximum PH required: {0:.2f}'.format(x['ph'].max()))
    print('-----------------------')
    print('Statistics for Rainfall')
    print('Minimum Rainfall required: {0:.2f}'.format(x['rainfall'].min()))
    print('Average Rainfall required: {0:.2f}'.format(x['rainfall'].mean()))
    print('Maximum Rainfall required: {0:.2f}'.format(x['rainfall'].max()))


# %
# compare the average requirement for each crops with average condition
@interact
def compare(conditions=['N', 'P', 'K', 'temperature', 'ph', 'humidity', 'rainfall']):
    print('Average Value for ', conditions, 'is {0:.2f}'.format(data[conditions].mean()))
    print('-----------------------')
    print('Rice: {0:.2f}'.format(data[(data['label'] == 'rice')][conditions].mean()))
    print('Black Grams: {0:.2f}'.format(data[(data['label'] == 'blackgram')][conditions].mean()))
    print('Banana: {0:.2f}'.format(data[(data['label'] == 'banana')][conditions].mean()))
    print('Jute: {0:.2f}'.format(data[(data['label'] == 'jute')][conditions].mean()))
    print('Coconut: {0:.2f}'.format(data[(data['label'] == 'coconut')][conditions].mean()))
    print('Apple: {0:.2f}'.format(data[(data['label'] == 'apple')][conditions].mean()))
    print('Papaya: {0:.2f}'.format(data[(data['label'] == 'papaya')][conditions].mean()))
    print('Muskmelon: {0:.2f}'.format(data[(data['label'] == 'muskmelon')][conditions].mean()))
    print('Grapes: {0:.2f}'.format(data[(data['label'] == 'grapes')][conditions].mean()))
    print('Watermelon: {0:.2f}'.format(data[(data['label'] == 'watermelon')][conditions].mean()))
    print('Kidney Beans: {0:.2f}'.format(data[(data['label'] == 'kidneybeans')][conditions].mean()))
    print('Mung Beans: {0:.2f}'.format(data[(data['label'] == 'mungbeans')][conditions].mean()))
    print('Oranges: {0:.2f}'.format(data[(data['label'] == 'orange')][conditions].mean()))
    print('Chick Peas: {0:.2f}'.format(data[(data['label'] == 'chickpea')][conditions].mean()))
    print('Lentils: {0:.2f}'.format(data[(data['label'] == 'lentil')][conditions].mean()))
    print('Cotton: {0:.2f}'.format(data[(data['label'] == 'cotton')][conditions].mean()))
    print('Maize: {0:.2f}'.format(data[(data['label'] == 'maize')][conditions].mean()))
    print('Moth Beans: {0:.2f}'.format(data[(data['label'] == 'mothbeans')][conditions].mean()))
    print('Pigeon Peas: {0:.2f}'.format(data[(data['label'] == 'pigeonpeas')][conditions].mean()))
    print('Mango: {0:.2f}'.format(data[(data['label'] == 'mango')][conditions].mean()))
    print('Pomegranate: {0:.2f}'.format(data[(data['label'] == 'pomegranate')][conditions].mean()))
    print('Coffee: {0:.2f}'.format(data[(data['label'] == 'coffee')][conditions].mean()))


# %%
# make this function more intuitive
@interact
def compare(conditions=['N', 'P', 'K', 'temperature', 'ph', 'humidity', 'rainfall']):
    print('Crops which require greater than average', conditions, '\n')
    print(data[data[conditions] > data[conditions].mean()]['label'].unique())
    print('-----------------------')
    print('Crops which require less than average', conditions, '\n')
    print(data[data[conditions] <= data[conditions].mean()]['label'].unique())


# %%
# check the distribution of Agricultural Conditions
plt.rcParams['figure.figsize'] = (15, 7)

plt.subplot(2, 4, 1)
sns.distplot(data['N'], color='lightgrey')
plt.xlabel('Ratio of Nitrogen', fontsize = 12)
plt.grid()

plt.subplot(2, 4, 2)
sns.distplot(data['P'], color='skyblue')
plt.xlabel('Ratio of Phosphorous', fontsize = 12)
plt.grid()

plt.subplot(2, 4, 3)
sns.distplot(data['K'], color='darkblue')
plt.xlabel('Ratio of Potassium', fontsize = 12)
plt.grid()

plt.subplot(2, 4, 4)
sns.distplot(data['temperature'], color='red')
plt.xlabel('Temperature', fontsize = 12)
plt.grid()

plt.subplot(2, 4, 5)
sns.distplot(data['humidity'], color='yellow')
plt.xlabel('Humidity', fontsize = 12)
plt.grid()

plt.subplot(2, 4, 6)
sns.distplot(data['ph'], color='green')
plt.xlabel('PH', fontsize = 12)
plt.grid()

plt.subplot(2, 4, 7)
sns.distplot(data['rainfall'], color='orange')
plt.xlabel('Rainfall', fontsize = 12)
plt.grid()

#%%
# find out some interesting facts
print('Some interesting Patterns')
print('-----------------------')
print('Crops which requires very High Ratio of Nitrogen Content in Soil:', data[data['N'] > 120]['label'].unique())
print('Crops which requires very High Ratio of Phosphorous Content in Soil:', data[data['P'] > 100]['label'].unique())
print('Crops which requires very High Ratio of Potassium Content in Soil:', data[data['K'] > 200]['label'].unique())
print('Crops which requires very High Rainfall:', data[data['rainfall'] > 200]['label'].unique())
print('Crops which requires very Low Temperature:', data[data['temperature'] < 10]['label'].unique())
print('Crops which requires very High Temperature:', data[data['temperature'] > 40]['label'].unique())
print('Crops which requires very High Rainfall:', data[data['rainfall'] > 200]['label'].unique())
print('Crops which requires very Low Humidity:', data[data['humidity'] < 20]['label'].unique())
print('Crops which requires very High pH:', data[data['ph'] > 9]['label'].unique())
print('Crops which requires very Low pH:', data[data['ph'] < 4]['label'].unique())


#%%
# understand which crops can only be grown in summer, winter and rainy season
print('Summer crops')
print(data[(data['temperature'] > 30) & (data['humidity'] > 50)]['label'].unique())
print('-----------------------')
print('Winter crops')
print(data[(data['temperature'] < 20) & (data['humidity'] > 30)]['label'].unique())
print('-----------------------')
print('Rainy crops')
print(data[(data['rainfall'] > 200) & (data['humidity'] > 30)]['label'].unique())

#%%
# try to cluster these crops
# import the warning library to avoid warnings

from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')

# select the spending score and annual income columns from the data
x = data.loc[:, ['N', 'P', 'K', 'temperature', 'ph', 'humidity', 'rainfall']].values

# check the shape of x
print(x.shape)

#convert this data into a dataframe
x_data = pd.DataFrame(x)
x_data.head()


#%%
# determine the optimum number of clusters within the dataset
plt.rcParams['figure.figsize'] = (10,4)

wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    km.fit(x)
    wcss.append(km.inertia_)

# plot the results
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method', fontsize = 20)
plt.xlabel('No. of Clusters')
plt.ylabel('wcss')
plt.show()

#%%
# implement the K Means algorithm to perform clustering analysis
km = KMeans(n_clusters = 4, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_means = km.fit_predict(x)

# find out the results
a = data['label']
y_means = pd.DataFrame(y_means)
z = pd.concat([y_means, a], axis = 1)
z = z.rename(columns = {0: 'cluster'})

# check the clusters for each crops
print('Check the results after applying the K Means clustering analysis \n')
print('Crops in the first cluster: ', z[z['cluster'] == 0]['label'].unique())
print('-----------------------')
print('Crops in the second cluster: ', z[z['cluster'] == 1]['label'].unique())
print('-----------------------')
print('Crops in the third cluster: ', z[z['cluster'] == 2]['label'].unique())
print('-----------------------')
print('Crops in the forth cluster: ', z[z['cluster'] == 3]['label'].unique())

#%%
# split the dataset for predictive modelling
y = data['label']
x = data.drop(['label'], axis = 1)

print('Shape of x: ', x.shape)
print('Shape of y: ', y.shape)

#%%
# create training and testing sets for validation of results
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

print('Shape of x train : ', x_train.shape)
print('Shape of x test: ', x_test.shape)
print('Shape of y train: ', y_train.shape)
print('Shape of y test: ', y_test.shape)

#%%
# create a predictive model
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict((x_test))

#%%
# evaluate the model performance
from sklearn.metrics import classification_report
#
# print classification report
cr = classification_report(y_test, y_pred)
print(cr)

#%%
# check the head of the dataset
data.head()

# suggestion
prediction = model.predict((np.array([[90,
                                      40,
                                      40,
                                      20,
                                      80,
                                      7,
                                      200]])))
print('The suggested crop for given climatic condition is: ', prediction)

#%%
# check the model for orange
data[data['label'] == 'orange'].head()
pred_orange = model.predict((np.array([[20,
                                         30,
                                         10,
                                         15,
                                         90,
                                         7.5,
                                         100]])))
print('The Suggested crop for given climatic condition is: ', pred_orange)

