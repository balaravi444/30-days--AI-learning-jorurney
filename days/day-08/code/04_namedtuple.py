# Problem 4 = Structured Data Using namedtuple
# Day 08 - Collections Module

from collection import nametuple

Student = namedtuple("Student", ["name", "age", "course"])
s1 = Student(name="Bala", age=20, course="BCA")
print("Name:", s1.name)
print("Age::", s1.age)
print("Course:", s1.course)
