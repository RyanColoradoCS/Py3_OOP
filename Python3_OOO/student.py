# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Child class inheriting from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.student_id = student_id

    def display_student(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

    def __repr__(self):
        return f"Student(name='{self.name}', student_id='{self.student_id}')"

class Course:
    def __init__(self, courseName):
        self.roster = []
        self.courseName = courseName

    def addStudent(self, Student):
        self.roster.append(Student)

    def display(self):
        print(f"courseName: {self.courseName}, Students: {self.roster}")


# Create an instance of Student
student = Student("Alice", 20, "S12345")
student2 = Student("Bob", 21, "S22345")
student.display_student()

phys101 = Course("Physics 101")
phys101.addStudent(student)
phys101.addStudent(student2)
phys101.display()
try:
    raise Exception("This exception is raised here for no reason")
except:
    print("Caught exception")
    phys101.display()

try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("The exception arguments were", e.args)
finally:
    print("This is always called")

