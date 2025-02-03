import numpy as np

#grades analysis

grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
print(grades)

#Use numpy functions to calculate the mean, median, and standard deviation of the grades.
print('the mean of the grades is: ',grades.mean()) # 87.5
print('the median of the grades is:',np.median(grades)) # 88.5
print('the standard deviation of the grades is: ',grades.std()) # 6.591

# Use numpy function to find the maximum and minimum of the grades.
print(grades.max())  #98
print(grades.min())  #75

# Use numpy function to sort the grades in ascending order.
print(np.sort(grades))  #[75 80 83 85 88 89 90 92 95 98]

# Use numpy function to find the index of the highest grade in the array.
print('index o the highest grades is: ',np.unravel_index(np.argmax(grades), grades.shape))  # 7

# Use numpy function to count the number of students who scored above 90.
print(np.sum(grades>90),'students have more than 90 in grades')  #3

#Use numpy function to calculate the percentage of students who scored above 90.
print(np.mean((grades>90)*100))

# Use numpy function to calculate the percentage of students who scored below 75.
print('the percentage of student who scored below 75 is: ',np.sum(grades < 75)*100/grades.size,'%') # 0.0%

# Use numpy function to extract all the grades above 90 and put them in a new array called "high_performers".
high_performers= (grades[grades>90])
print('the grades greater than 90 are:',high_performers)  #[92 95 98]
#  Create a new array called "passing_grades" that contains all the grades above 75.
passing_grades= (grades[grades>=75])
print('the passing grades are: ',passing_grades)   #[85 90 88 92 95 80 75 98 89 83]

