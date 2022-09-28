class Student:
    def __init__(self):
        self.name = "Monty"
    def get_grade(self):
        return self.__grade
    def set_grade(self, grade):
        if grade == "A" or grade == "B" or grade == "C" or grade == "D" or grade == "E" or grade == "F":
            self.__grade = grade
student = Student()
student.set_grade("B")
print(student.get_grade())
