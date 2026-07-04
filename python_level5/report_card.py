class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
    def add_grade(self, subject, score):
        self.grades[subject] = score
    def get_average(self):
        if len(self.grades) == 0:
            return 0
        total = sum(self.grades.values())
        return total / len(self.grades)
    def report(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        for subject, score in self.grades.items():
            print(f"{subject}: {score}")
        print(f"\nAverage Score: {self.get_average():.2f}")
student = Student("Monii", 101)
student.add_grade("Maths", 95)
student.add_grade("Science", 90)
student.add_grade("English", 85)
student.report()