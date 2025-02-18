import numpy as np
import pandas as pd

class Student:
    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades  # Expecting a list of grades

    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Average Grade: {self.get_average():.2f}"