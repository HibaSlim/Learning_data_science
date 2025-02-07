import numpy as np
import pandas as pd

Loan_prediction_dataset = 'Loan_prediction_dataset.csv'
data = pd.read_csv(Loan_prediction_dataset)
# print data to understand it's structure
print (data.head())
loan_amounts = data['LoanAmount'].dropna()
print(loan_amounts)
 #  Performing basic statistical analysis
mean_loan_amount = np.mean(loan_amounts)
print(f"Mean loan amount: {mean_loan_amount:.2f}")
median_loan_amount = np.median(loan_amounts)
print(f"Median loan amount: {median_loan_amount}")
std_loan_amount = np.std(loan_amounts)
print(f"Standard deviation of loan amounts: {std_loan_amount:.2f}")