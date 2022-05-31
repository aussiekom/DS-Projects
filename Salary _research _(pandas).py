import pandas as pd

# read csv as dataframe
sal = pd.read_csv('Salaries.csv')

# check the head of the df
sal.head()

# find out how many entries there are
sal.info() # 148654 Entries

# exploring the data
sal['BasePay'].mean()
sal['OvertimePay'].max()

# find job title in specify query
sal[sal['EmployeeName'] =='JOSEPH DRISCOLL']['JobTitle']
sal[sal['EmployeeName'] =='JOSEPH DRISCOLL']['TotalPayBenefits']

# check the highest and the lowest paid persons
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]

# the average BasePay of all employees per year?
sal.groupby('Year').mean()['BasePay']

# how many unique job titles
sal['JobTitle'].nunique()

# what are the top 5 most common jobs?
sal['JobTitle'].value_counts().head(5)

# how many Job Titles were represented by only one person in 2013?
sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1)

# how many people have the word Chief in their job title?
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False

sum(sal['JobTitle'].apply(lambda x: chief_string(x)))

# checking a possible correlation between lenght of the job title string and salary
sal['title_len'] = sal['JobTitle'].apply(len)
sal[['title_len', 'TotalPayBenefits']].corr()   # no correlation


