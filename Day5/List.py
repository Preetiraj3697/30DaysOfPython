empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Modifying list

fruits = ['banana', 'orange', 'mango', 'lemon'] 
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the end index
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1] # it does not include the end index
orange_mango_lemon = fruits[-3:]


fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado' 
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
print(fruits)

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()     
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)     
print(fruits)       # ['orange', 'mango'] 

# del 
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]     
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]     
print(fruits)       # ['orange', 'lemon']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()     
print(fruits)       # []

# copying a lits

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()     
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# join
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

# join with extend
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) 
# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) 

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) 
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 
ages.sort(reverse=True)
print(ages) 
# Exercises: Day 5

# Exercises: Level 1

# 1. Declare an empty list
lst = list()
print(lst)
empty_list = []

# 2. Declare a list with more than 5 items
my_list = [1, 'apple', 3.14, True, 'banana', [7, 8, 9], 'elephant', {'key': 'value'}, 10]
print(my_list)

# 3. Find the length of your list
length = len(my_list)
print(length)

# 4. Get the first item, the middle item and the last item of the list
# Get the first item
first_item = my_list[0]
# Get the middle item (rounded down for odd-length lists)
middle_item = my_list[len(my_list) // 2]
# Get the last item
last_item = my_list[-1]
print("First Item:", first_item)
print("Middle Item:", middle_item)
print("Last Item:", last_item)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Paarthav', 30, 175.5, False, '123 Main Street, Cityville']

# Accessing individual elements
name = mixed_data_types[0]
age = mixed_data_types[1]
height = mixed_data_types[2]
marital_status = mixed_data_types[3]
address = mixed_data_types[4]
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Marital Status:", marital_status)
print("Address:", address)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
# 7. Print the list using _print()_
print(it_companies);
# 8. Print the number of companies in the list
num_companies = len(it_companies)
print("Number of companies:", num_companies)
# 9. Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies)//2]
last_company = it_companies[-1]
print("First company:", first_company)
print("Middle company:", middle_company)
print("Last company:", last_company)
# 10. Print the list after modifying one of the companies
it_companies[2] = "Microsoft Corporation"
print("Modified list:", it_companies)
# 11. Add an IT company to it_companies
it_companies.append("Intel")
print("After adding Intel:", it_companies)
# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, "Cisco")
print("After inserting Cisco in the middle:", it_companies)
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[4] = it_companies[4].upper()
print("After changing IBM to uppercase:", it_companies)
# 14. Join the it_companies with a string '#;&nbsp; '
joined_companies = '#;&nbsp; '.join(it_companies)
print("Joined companies:", joined_companies)
# 15. Check if a certain company exists in the it_companies list.
company_to_check = "Microsoft Corporation"
company_exists = company_to_check in it_companies
print(f"Does '{company_to_check}' exist in the list? {company_exists}")
# 16. Sort the list using sort() method
it_companies.sort()
print("Sorted list:", it_companies)
# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print("Reversed list:", it_companies)
# 18. Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print("First three companies:", first_three_companies)

# 19. Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print("Last three companies:", last_three_companies)
# 20. Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
middle_company = it_companies[middle_index] if len(it_companies) % 2 != 0 else it_companies[middle_index-1:middle_index+1]
print("Middle company:", middle_company)
# 21. Remove the first IT company from the list
it_companies.pop(0)
print("After removing the first company:", it_companies)
# 22. Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
it_companies.pop(middle_index) if len(it_companies) % 2 != 0 else it_companies.pop(middle_index-1)
print("After removing the middle company:", it_companies)
# 23. Remove the last IT company from the list
it_companies.pop()
print("After removing the last company:", it_companies)
# 24. Remove all IT companies from the list
it_companies.clear()
print("After removing all companies:", it_companies)
# 25. Destroy the IT companies list
del it_companies
# 26. Join the following lists:
#     front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#     back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print("Full stack technologies:", full_stack)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')

print("Updated full stack technologies:", full_stack)