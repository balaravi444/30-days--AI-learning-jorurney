# Problem 2 - Default Values Using defaultdict
# Day 08 - Collections Module

from collections import defaultdict

student_marks = defaultdict(int)
student_marks["Bala"] += 10
student_marks["Ravi"] += 20
print("Marks:", dict(student_marks))
