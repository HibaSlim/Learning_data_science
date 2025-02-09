import numpy as np
import pandas as pd

Loan_prediction_dataset = 'Loan_prediction_dataset.csv'
with open(Loan_prediction_dataset, 'r'):
    data = np.genfromtxt(Loan_prediction_dataset, delimiter=',', skip_header= 0,names = True, dtype=None, encoding=None)
print(data)
loan_amounts = data['LoanAmount']
print(loan_amounts)
 #  Performing basic statistical analysis
mean_loan_amount = np.mean(loan_amounts)
print(f"Mean loan amount: {mean_loan_amount:.2f}") #141.13
median_loan_amount = np.median(loan_amounts)
print(f"Median loan amount: {median_loan_amount}")   #125.0
std_loan_amount = np.std(loan_amounts)
print(f"Standard deviation of loan amounts: {std_loan_amount:.2f}")   #88.33

'''
#opening it using pandas
Loan_prediction_dataset = 'Loan_prediction_dataset.csv'
data = pd.read_csv(Loan_prediction_dataset)
# print data to understand it's structure
print (data.head())
loan_amounts = data['LoanAmount'].dropna()
print(loan_amounts)
 #  Performing basic statistical analysis
mean_loan_amount = np.mean(loan_amounts)
print(f"Mean loan amount: {mean_loan_amount:.2f}") #146.41
median_loan_amount = np.median(loan_amounts)
print(f"Median loan amount: {median_loan_amount}")  #128.0
std_loan_amount = np.std(loan_amounts)
print(f"Standard deviation of loan amounts: {std_loan_amount:.2f}")  #85.52
'''