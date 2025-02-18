from student import Student
from database import StudentDatabase
from analysis import StudentAnalysis

def main():
    db = StudentDatabase()
    analysis = StudentAnalysis(db)

    # Create student records
    students = [
        Student(1, "Alice", [85, 90, 78]),
        Student(2, "Bob", [88, 92, 95]),
        Student(3, "Charlie", [70, 75, 80])
    ]

    # Store them in the database
    for student in students:
        db.add_student(student)

    # Compute and display the class average and top student
    class_average = analysis.compute_class_average()
    top_student, top_average = analysis.find_top_student()

    print(f"Class Average: {class_average:.2f}")
    print(f"Top Student: {top_student} with an average of {top_average:.2f}")

if __name__ == "__main__":
    main()
