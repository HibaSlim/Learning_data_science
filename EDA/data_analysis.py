from statistics import median
import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

file = 'histogram_data.csv'
data=pd.read_csv(file)
df=pd.DataFrame(data)
'''print('\n',data.head())
print('\n',df.tail())
print('\n',df.describe())
print('\n',df.info())
print ('\n',df.isnull().sum())
year_of_sale_median=df['Year of sale'].median()
print('the median of the year of sale is :',year_of_sale_median)
median_month_of_sale=df['Month of sale'].median()
print('the median of the month of sale is :',median_month_of_sale)'''
df_copy=df.copy()
numeric_cols = df_copy.select_dtypes(include=[np.number]).columns
df_copy[numeric_cols] = df_copy[numeric_cols].fillna(df_copy[numeric_cols].median())
print(df_copy)
print ('\n',df_copy.isnull().sum())

cleaned_file = 'cleaned_data.csv'
df_copy.to_csv(cleaned_file)

'''Profile= ProfileReport(df_copy,title='property')
Profile.to_file('cleaned_report.html')'''
df_update=df_copy.rename(columns={'Type of property':'property_type'})
print(df_update.info())
df_encoded =pd.get_dummies(df_update,columns=['property_type'],dtype=int)
print(df_encoded)
print(df_encoded.describe())
print(df_encoded.info())
df_encoded.to_csv('encoded_report.csv')
profile_encoded=ProfileReport(df_encoded, title='property encoded')
profile_encoded.to_file('encoded_report.html')
df_encoded.to_excel('encoded_report.xlsx',index=False)







