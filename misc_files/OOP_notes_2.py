class Student:
    def __init__(self, name, age, grade): # We have definied 3 attributes 'name', 'age' , 'grade'
        self.name = name
        self.age = age
        self.grade = grade # 0-100

    def get_grade(self): # This is a method that returns a students grade
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] # Attributes are whatever we want to define

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True # Will execute if student was added to the list
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.get_average_grade())

        