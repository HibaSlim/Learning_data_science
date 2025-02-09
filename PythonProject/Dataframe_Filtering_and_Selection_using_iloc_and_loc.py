import pandas as pd

data = {'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
        'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'],
        'Age': [30, 40, 25, 35, 45, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'Salary': [50000, 60000, 45000, 55000, 70000, 55000],
        'Experience': [3, 7, 2, 5, 10, 4]}

employee_df = pd.DataFrame(data)
print( employee_df)
first_three_rows= employee_df.iloc[0:3]
print(f'\n the first three rows are : \n {first_three_rows}')
Marketing_rows = employee_df.loc[employee_df['Department'] == 'Marketing']
print(f'\n Marketing rows are:\n{Marketing_rows} ')
first_4_rows= employee_df.iloc[0:4,2:4]
print(f'\nfirst 4 rows of the age and gender columns:\n{first_4_rows}')
Male_salary_experience = employee_df.loc[employee_df['Gender']=='Male',['Salary','Experience']]
print(f'\nSalary and experience for male employee are:\n{Male_salary_experience}')
