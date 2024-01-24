# Exercise Level 1
import math
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(5,4))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    return math.pi * radius * radius
print(area_of_circle(5))
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    if all(isinstance(num, (int, float)) for num in args):
        return sum(args)
    else:
        return "Please provide only numbers in the argument list."
print(add_all_nums(3,4,5,6,7))
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32 
print(f'{convert_celsius_to_fahrenheit(10)} °F')
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month"
month = int(input("Enter the month number: "))
print(check_season(month))
# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(4,5,6,7))
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        return "No real roots"
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(my_list):
    for item in my_list:
        print(item)
print_list(["mongo","apple","grape","papaya"])
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
def reverse_list(my_list):
    reversed_list = []
    for i in range(len(my_list)-1, -1, -1):
        reversed_list.append(my_list[i])
    return reversed_list
print(reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))  # Output: ["C", "B", "A"]
# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(my_list):
    return [item.capitalize() for item in my_list]
print(capitalize_list_items(["mongo","apple","grape","papaya"]))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
def add_item(my_list,item):
     my_list.append(item)
     return my_list
print(add_item(["mongo","apple","grape","papaya"],"Banana"))

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]
def remove_item(my_list, item):
    if item in my_list:
        my_list.remove(item)
    return my_list
print(remove_item([2, 3, 7, 9],3))
print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'],"Mango"))
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050
def sum_of_numbers(n):
    return sum(range(1, n + 1))
print(sum_of_numbers(100))
def sum_all_numbers(n):
    return sum(range(1, n + 1))
# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    return sum(x for x in range(1, n + 1) if x % 2 != 0)
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    return sum(x for x in range(1, n + 1) if x % 2 == 0)

# Results
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))  # Output: ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))       # Output: [2, 7, 9]

print(sum_of_numbers(5))             # Output: 15
print(sum_all_numbers(10))           # Output: 55
print(sum_all_numbers(100))          # Output: 5050

# Example for sum_of_odds and sum_of_even
print(sum_of_odds(10))               # Output: 25 (1 + 3 + 5 + 7 + 9)
print(sum_of_even(10))               # Output: 30 (2 + 4 + 6 + 8 + 10)


# Exercise level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
from math import factorial, sqrt
from collections import Counter

def evens_and_odds(number):
    evens = 0
    odds = 0
    for digit in range(number+1):
        if digit % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def calculate_factorial(n):
    return factorial(n)

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    return not bool(param)

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, 
# calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def calculate_mode(lst):
    counts = Counter(lst)
    mode = max(counts, key=counts.get)
    return mode

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    squared_diff = [(x - mean) ** 2 for x in lst]
    return sum(squared_diff) / len(lst)

def calculate_std(lst):
    return sqrt(calculate_variance(lst))

# Testing the functions
print(evens_and_odds(100))
# Output: The number of odds are 50.
#         The number of evens are 51.

print(calculate_factorial(5))
# Output: 120 (5!)

print(is_empty([]))
# Output: True

data_list = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9]
print(calculate_mean(data_list))
# Output: 5.090909090909091

print(calculate_median(data_list))
# Output: 6

print(calculate_mode(data_list))
# Output: 5 (it can be a list if there are multiple modes)

print(calculate_range(data_list))
# Output: 8 (max - min)

print(calculate_variance(data_list))
# Output: 6.363636363636363

print(calculate_std(data_list))
# Output: 2.5238858928247927


# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Write a functions which checks if all items are unique in the list.
def are_all_unique(lst):
    return len(lst) == len(set(lst))

# Write a function which checks if all the items of the list are of the same data type.
def are_all_same_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)

# Write a function which check if provided variable is a valid python variable
def is_valid_variable(variable):
    try:
        exec(f"{variable} = 1")
        del locals()[variable]
        return True
    except:
        return False
print(is_valid_variable("Paarthav"))
# Go to the data folder and access the countries-data.py file.
countries_data = [
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Antigua and Barbuda",
        "capital": "Saint John's",
        "languages": [
            "English"
        ],
        "population": 86295,
        "flag": "https://restcountries.eu/data/atg.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Argentina",
        "capital": "Buenos Aires",
        "languages": [
            "Spanish",
            "Guaraní"
        ],
        "population": 43590400,
        "flag": "https://restcountries.eu/data/arg.svg",
        "currency": "Argentine peso"
    },
    {
        "name": "Armenia",
        "capital": "Yerevan",
        "languages": [
            "Armenian",
            "Russian"
        ],
        "population": 2994400,
        "flag": "https://restcountries.eu/data/arm.svg",
        "currency": "Armenian dram"
    },
    {
        "name": "Aruba",
        "capital": "Oranjestad",
        "languages": [
            "Dutch",
            "(Eastern) Punjabi"
        ],
        "population": 107394,
        "flag": "https://restcountries.eu/data/abw.svg",
        "currency": "Aruban florin"
    },
    {
        "name": "Australia",
        "capital": "Canberra",
        "languages": [
            "English"
        ],
        "population": 24117360,
        "flag": "https://restcountries.eu/data/aus.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Austria",
        "capital": "Vienna",
        "languages": [
            "German"
        ],
        "population": 8725931,
        "flag": "https://restcountries.eu/data/aut.svg",
        "currency": "Euro"
    },
    {
        "name": "Azerbaijan",
        "capital": "Baku",
        "languages": [
            "Azerbaijani"
        ],
        "population": 9730500,
        "flag": "https://restcountries.eu/data/aze.svg",
        "currency": "Azerbaijani manat"
    },
    {
        "name": "Bahamas",
        "capital": "Nassau",
        "languages": [
            "English"
        ],
        "population": 378040,
        "flag": "https://restcountries.eu/data/bhs.svg",
        "currency": "Bahamian dollar"
    },
 
    {
        "name": "Bermuda",
        "capital": "Hamilton",
        "languages": [
            "English"
        ],
        "population": 61954,
        "flag": "https://restcountries.eu/data/bmu.svg",
        "currency": "Bermudian dollar"
    },
    {
        "name": "Bhutan",
        "capital": "Thimphu",
        "languages": [
            "Dzongkha"
        ],
        "population": 775620,
        "flag": "https://restcountries.eu/data/btn.svg",
        "currency": "Bhutanese ngultrum"
    },
   
    {
        "name": "Korea (Republic of)",
        "capital": "Seoul",
        "languages": [
            "Korean"
        ],
        "population": 50801405,
        "flag": "https://restcountries.eu/data/kor.svg",
        "currency": "South Korean won"
    },
    {
        "name": "South Sudan",
        "capital": "Juba",
        "languages": [
            "English"
        ],
        "population": 12131000,
        "flag": "https://restcountries.eu/data/ssd.svg",
        "currency": "South Sudanese pound"
    },
    
    
]
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Assuming the file structure is like: project_folder/data/countries-data.py
def most_spoken_languages():
    all_languages = [language for country in countries_data for language in country["languages"]]
    language_counts = {language: all_languages.count(language) for language in set(all_languages)}
    sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:10]  # Change 10 to 20 if needed

# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
# Function to get the most populated countries
def most_populated_countries():
    sorted_countries = sorted(countries_data, key=lambda x: x["population"], reverse=True)
    return sorted_countries[:10]  # Change 10 to 20 if needed

# Example usage
most_spoken = most_spoken_languages()
print("Most Spoken Languages:", most_spoken)

most_populated = most_populated_countries()
print("Most Populated Countries:", most_populated)

