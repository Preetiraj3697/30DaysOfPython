# Higher Order Functions



import functools


def sum_numbers(nums): # normal Function
    return sum(nums) # a sad function abusing the built-in sum function

def higher_order_function(f,lst): # function as a parameter
    summation = f(lst)
    return summation

res = higher_order_function(sum_numbers,[1,2,3,4,5])
print(res) # 15

# Function as a Return Value
def square(x):
    return x**2

def cube(x):
    return x**3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    
res = higher_order_function('square')
print(res(3)) # 9
res = higher_order_function('cube')
print(res(3)) # 27
res = higher_order_function('absolute')
print(res(-3)) # 3


# Python Closure
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_res = add_ten()
print(closure_res(5)) # 15
print(closure_res(10)) # 20

# Python Decorators
# Creating Decorators
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON


'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
        
# Accepting Parameters in Decorator Functions
def decortor_with_parameters(function):
    def wrapper_accepting_parameter(para1,para2,para3):
        function(para1,para2,para3)
        print('I live in {}'.format(para3))
    return wrapper_accepting_parameter

@decortor_with_parameters
def print_full_name(first_name,last_name,country):
    print('I am {} {}. I love to teach.'.format(first_name,last_name,country))
    
print_full_name('Paarthav','Shah','Finland')

# Built-in Higher order functions
# Map function
numbers = [1,2,3,4,5]
def square(x):
    return x**2
numbers_squared = map(square, numbers)
print(list(numbers_squared)) # [1,4,9,16,25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x:x**2, numbers)
print(list(numbers_squared)) # [1,4,9,16,25]

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Filter Function
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']

# Reduce Function
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = functools.reduce(add_two_nums, numbers_str)
print(total)    # 15

# Exercises Day14
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises Level 1
# 1. Explain the difference between map, filter, and reduce.

# Map, Filter, and Reduce:
# Map:
# Purpose: Applies a given function to all the items in an iterable (e.g., a list) and returns an iterator that produces the results.
# Syntax: map(function, iterable)
# Example:
# python
# Copy code
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
# Filter:
# Purpose: Filters elements from an iterable based on a given function, and returns an iterator with only the elements that satisfy the condition.
# Syntax: filter(function, iterable)
# Example:
# python
# Copy code
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]
# Reduce:
# Purpose: Applies a rolling computation to sequential pairs of values in an iterable, reducing them to a single accumulated result.
# Syntax: functools.reduce(function, iterable[, initializer])
# Example:
# python
# Copy code
# from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_all = functools.reduce(lambda x, y: x + y, numbers)
print(sum_all)  # Output: 15

# 2. Explain the difference between higher order function, closure and decorator
# Higher-Order Function, Closure, and Decorator:
# Higher-Order Function:
# A function that takes one or more functions as arguments or returns a function as its result.
# Closure:
# A closure is a nested function that captures and remembers the values in the enclosing function's local scope, even if the outer function has finished executing.
# Decorator:
# A decorator is a function that takes another function and extends or modifies its behavior without explicitly modifying the original function's code.

# 3. Define a call function before map, filter or reduce, see examples.
# Define a call function before map, filter, or reduce:

def call(func, *args, **kwargs):
    return func(*args, **kwargs)

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(call, [lambda x: x**2] * len(numbers), numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# 4. Use for loop to print each country in the countries list.
countries = ["USA", "Canada", "UK", "Germany"]

for country in countries:
    print(country)

# 5. Use for to print each name in the names list.
names = ["Alice", "Bob", "Charlie", "David"]

for name in names:
    print(name)

# 6. Use for to print each number in the numbers list.
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


