class Student:
    #attributes
    college_name = "IIT Bombay" #class attributes

    #instance attributes
    def __init__(self, name, age, dob):
        print("constructor has been called")
        self._name = name
        self._age = age
        self._dob = dob

    def print_name(self):
        print("Student name:"+ self._name)

    def increment_age(self):
        self._age = self._age + 1
        print("Age for student" + self._name + "is:" + str(self._age))
student_1 = Student("Raj", 23,"09/05/1994")
student_2 = Student("Rahul",21,"05/09/1995")

#print(student_1._name, student_1._age, student_1._dob, student_1.college_name)
#print(student_2._name, student_2._age, student_2._dob, student_2.college_name)

student_1.increment_age()
student_2.increment_age()
