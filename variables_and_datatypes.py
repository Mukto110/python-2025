'''
1. Create 5 variables of different data types (int, float, str, bool, list).
Print each one and its type using type().
'''
a = 5
b = 2.5
c = "Mukto"
d = True
names = ["Mukto", "Tushar", "Emon"] # List

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(names, type(names))


'''
2. Store your name, age, and country in variables and print a sentence using them:
Example output: “Hi, I’m Mukto, 27 years old, from Bangladesh.”
'''
name = "Mukto"
age = 27
country = "Bangladesh"

print(f"Hi, I'm {name}, {age} years old, from {country}")

'''
3. Create a dictionary named student with your details (name, roll, grade, passed=True).
Print it in a readable way.”
'''
student = {"name": "Mukto", "roll": 28, "grade": "A", "passed": True}
my_name = student.get("name")
my_roll = student.get("roll")
my_grade = student.get("grade")
am_I_passed = student.get("passed")

print(f'''
Name: {my_name}
Roll: {my_roll}
Grade: {my_grade}
Pass: {am_I_passed}
''')


'''
4. Create two variables x and y, swap their values without using a third variable.
'''
x = 2
y = 4
x = x + y # 6
y = x - y # 2
x = x - y

print(f"x = {x}, y = {y}")

'''
5. Given the list marks = [85, 90, 78, 92], store:
The first mark in math
The last mark in science
Print both using formatted strings like:
print(f"My math mark is {math} and science mark is {science}")
'''