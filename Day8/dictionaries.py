# Exercises: Day 8
# 1. Create an empty dictionary called dog
dog = {}
# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = "Buddy"
dog['color'] = "Brown"
dog['breed'] = "Labrador Retriever"
dog['legs'] = 4
dog['age'] = 3
# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'John',
    'last_name':'Doe',
    'gender':'Male',
    'age':22,
    'marital_status':'Single',
    'skills':['Python','Javascript'],
    'country':'USA',
    'city':'New York',
    'address':'123 Main St'
}
# 4. Get the length of the student dictionary
length_student = len(student)
print(length_student)
# 5. Get the value of skills and check the data type, it should be a list
skills_value = student['skills']
print(skills_value,type(skills_value))
# 6. Modify the skills values by adding one or two skills
student['skills'].extend(["HTML","CSS"])
# 7. Get the dictionary keys as a list
keys_list = list(student.keys())
print(keys_list)
# 8. Get the dictionary values as a list
values_list = list(student.values())
print(values_list)
# 9. Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print(student_items)
# 10. Delete one of the items in the dictionary
del student['marital_status']
# 11. Delete one of the dictionaries
del dog