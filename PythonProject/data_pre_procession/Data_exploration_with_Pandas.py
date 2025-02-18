import pandas as pd

#1
file = 'STEG_BILLING_HISTORY.csv'
data = pd.read_csv(file)
client_0_bills = data[0:11]
print('the first 10 lignes are: \n',client_0_bills)
#2
print('the type of client_0_bills is : \n',type(client_0_bills))
#3
df=pd.DataFrame(data)
num_rows, num_columns = df.shape
print(f'\nNumber of rows: {num_rows}\nNumber of columns: {num_columns}')

categorical_features = df.select_dtypes(include=['object', 'category']).columns
number_categorical_features = len(categorical_features)
print(f'\nNumber of categorical features: {number_categorical_features}')

memory_usage = df.memory_usage(deep=True).sum()
print(f'\nmemory usage is: {memory_usage} bytes')
#4
missing_values=df.isnull().sum()
print(f'\nmissing values in each columns:\n{missing_values[missing_values!=0]}')
#5
'''the counter number and the reading remarque are not important information and does not affect the analysis and the output 
the missing values of the conter number are insignifiant 48 rows that is why we can delete these rows
for the reading_remarque the number of missing values is important so we will fill it with the median 
'''
#6
numeric_cols = df.select_dtypes(include=['number']).columns
print('\nnumeric column are:',numeric_cols)
print('\n',df[numeric_cols].describe())
#7

print('\nthe bills records for the client with an id =train_Client_0',df.query("client_id == 'train_Client_0'"))#1st methode
print('\nthe bills records for the client with an id =train_Client_0',df.loc[df['client_id']=='train_Client_0']) #2nd methode
print('\nthe bills records for the client with an id =train_Client_0', df[df.filter(like='client_id')['client_id']=='train_Client_0'])#3rd methode
#8
df_counter_type=pd.DataFrame({'counter_type':['ELEC','GAZ']})
one_hot_df = pd.get_dummies(df, columns=['counter_type'])
print(one_hot_df)

#9
df_manipulated=df.drop(columns=['counter_statue'])
print('Result after deleting counter_statue',df_manipulated)




