import numpy as np
import pandas as pd

class StudentAnalysis:
    def __init__(self, database):
        self.database = database

    def compute_class_average(self):
        grades = []
        for index, row in self.database.get_all_students().iterrows():
            grades.extend(eval(row['Grades']))  # Convert string representation of list back to list
        return np.mean(grades) if grades else 0

    def find_top_student(self):
        top_student = None
        highest_average = 0
        for index, row in self.database.get_all_students().iterrows():
            student_grades = eval(row['Grades'])
            average = np.mean(student_grades)
            if average > highest_average:
                highest_average = average
                top_student = row['Name']
        return top_student, highest_average