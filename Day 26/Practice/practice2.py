# dictionary list comprehension
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor"]
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)
# dictionary comprehension with key, value and test
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)