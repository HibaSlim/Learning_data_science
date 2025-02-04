import numpy as np
''' Problem: Sales Data Analysis

You are given monthly sales data for a company's three products across five different regions.
Create a NumPy program to analyze this data and answer specific questions.

Tasks:
Create a 3D array (5 regions × 3 products × 12 months) with random sales data
Calculate total sales per region
Find the best-performing product in each region
Calculate month-over-month growth for each product
Identify the region with the most consistent sales (lowest standard deviation)
Find the peak season (quarter) for each product'''

np.random.seed(42) # For reproducibility
sales_data = np.random.randint(100, 1000, size=(5, 3, 12))
regions = ['North', 'South', 'East', 'West', 'Central']
products = ['Product A', 'Product B', 'Product C']
print(sales_data)

# Calculate total sales per region
total_sales_per_region = sales_data.sum(axis =(1,2))
print(total_sales_per_region)
#ou bien
for i , j in zip(regions,sales_data):
    print(i,'has a total sales of : ', j.sum ())

#Find the best-performing product in each region

best_performing_product = sales_data.sum(axis =2)
for i, region_sale in enumerate(best_performing_product):
    max_sale = max(region_sale)
    best = list(region_sale).index(max_sale)
    print(f'{regions[i]}:{products[best]}')
    


#Calculate month-over-month growth for each product
monthly_sales = sales_data.mean(axis =0)  # Average across region
print(monthly_sales)
growth = np.diff(monthly_sales, axis=1)/monthly_sales[ : , :-1]*100 #calculate growth
print(growth)
for product, prod_growth in zip(products,growth):
    print(f'{product}:{prod_growth.mean():.1f}%')
print(growth)

# Most consistent region (lowest variance, lowest standard deviation
consistency = sales_data.std(axis = (1,2))
most_consistent = regions[consistency.argmin()]
print(most_consistent)

# Find the peak season (quarter) for each product

quarter_sales = sales_data.reshape(5,3,4,3).mean(axis=3)
print(quarter_sales)
peak_quarter = quarter_sales.mean(axis=0).argmax(axis = 1)
print(peak_quarter)

for product, quarter in zip(products, peak_quarter + 1):
    print(f'{product} : q{quarter}')