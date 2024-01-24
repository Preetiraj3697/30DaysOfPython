# Exercises: Day9
# Exercises: Level 1
# 1. Get user input using input(“Enter your age: ”).
# If user is 18 or older, give feedback:
# You are old enough to drive. If below 18 give feedback to 
# wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
age = int(input("Enter your age: "))
if age >=18:
    print("You are old enough to drive")
else:
    print(f"You need {18-age} more years to learn to drive.")
# 2. Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get 
# the age as input. You can use a nested condition to print 'year' 
# for 1 year difference in age, 'years' for bigger differences, 
# and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
my_age = 22
your_age = int(input("Enter your age: "))
if my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print(f"You are 1 year older than me.")
    else:
        print(f"You are {age_difference} years older than me.")
elif my_age < your_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print(f"I am 1 year older than you.")
    else:
        print(f"I am {age_difference} years older than you.")
else:
    print("We are the same age.")
# 3. Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b
# return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


# Exercise Level 2
# write a code which gives grade to students according to theirs scores:
'''
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
'''
score = int(input("Enter your score: "))
if 80 <= score <= 100:
    grade = "A"
elif 70 <= score <= 89:
    grade = "B"
elif 60 <= score <= 69:
    grade = "C"
elif 50 <= score <= 59:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")

# 2. Check if the season is Autumn, Winter, Spring or Summer.
# If the user input is: September, October or November, the season
# is Autumn. December, January or February, the season is Winter.
# March, April or May, the season is Spring June, July or August, 
# the season is Summer
month = input("Enter the month: ").lower()

if month in ['september', 'october', 'november']:
    season = 'Autumn'
elif month in ['december', 'january', 'february']:
    season = 'Winter'
elif month in ['march', 'april', 'may']:
    season = 'Spring'
elif month in ['june', 'july', 'august']:
    season = 'Summer'
else:
    season = 'Invalid month'
    
print(f"The season is {season}")

# 3. The following list contains some fruits:

# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit
# to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()

if new_fruit not in fruits:
    fruits.append(new_fruit)
    print(f"{new_fruit.capitalize()} added to the list. updated list: {fruits}")
else:
    print("That fruit already exists in the list.")
    
    
# Exercise Level 3

# 1. Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills_list = person['skills']
    if skills_list:
        middle_index = len(skills_list) // 2
        print(f"The middle skill is: {skills_list[middle_index]}")
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person and 'Python' in person['skills']:
    print("The Person has python skill.")

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person:
    skills_set = set(person['skills'])
    if skills_set == {'Javascript','React'}:
        print("He is a frontend developer.")
    elif skills_set == {'Node',"Python","MongoDB"}:
        print("He is a backend developer.")
    elif skills_set == {'React', 'Node', 'MongoDB'}:
        print('He is a full stack developer')
    else:
        print("Unknown title")

#  * If the person is married and if he lives in Finland, print the information in the following format:
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in Finland.")


