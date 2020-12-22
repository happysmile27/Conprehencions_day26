# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items}
import random
names = ["Alex", "Olia", "Volodymyr", "Olenka", "Ave"]
students_score = {student: random.randint(60, 100) for student in names} # create dict
print(students_score)

student_4grade = {student: score for (student, score) in students_score.items() if score >= 75}
print(student_4grade)

