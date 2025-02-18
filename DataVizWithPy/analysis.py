import pandas as pd
from ydata_profiling import ProfileReport

df=pd.read_csv('histogram_data.csv')
'''profile = ProfileReport(df,title='Property Report')
profile.to_file('PropertyReport.html')'''
'''print(len(df))
print(df.head())
print(df.info())
print(df.isnull())'''

print(df['Year of sale'].mode())
print(df['Month of sale'].mode())
df['Year of sale'] = df['Year of sale'].fillna(value=2007)
df['Month of sale']=df['Month of sale'].fillna(value =11)
print(df.tail())

profile=ProfileReport(df,title ='Cleaned Property Report')
'''profile.to_file('CleanPropertyReport.html')
df.to_csv('clean_histogram_data.csv')'''
print(df.info())
