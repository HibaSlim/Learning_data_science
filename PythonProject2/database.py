import pandas as pd
from student import Student

class StudentDatabase:
    def __init__(self, file_path="students.csv"):
        self.file_path = file_path
        self.load_students()

    def add_student(self, student):
        new_data = pd.DataFrame({
            'ID': [student.student_id],
            'Name': [student.name],
            'Grades': [student.grades]
        })
        new_data.to_csv(self.file_path, mode='a', header=False, index=False)

    def get_all_students(self):
        return pd.read_csv(self.file_path)

    def load_students(self):
        try:
            self.students_df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            self.students_df = pd.DataFrame(columns=['ID', 'Name', 'Grades'])