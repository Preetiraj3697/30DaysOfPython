import mymodule
print(mymodule.generate_full_name('Paarthav','Shah'))

# Import Functions from a Module
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Paarthav','Shah'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(f'{int(weight)} N')
print(person['firstname'])

# Import Functions from a Module and Renaming
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Paarthav','Shah'))
print(total(1,9))
mass = 100
weight = mass * g
print(f'{int(weight)} N')
# print(p)
print(p['firstname'])

# import built-in module
import os
#Print current working directory
print("Current directory:" , os.getcwd())
# Creating a directory
# os.mkdir('Paarthav')
# Changing the current directory
# os.chdir('Paarthav')
#Print current working directory
# print("Current directory now:" , os.getcwd())
# Removing directory
# os.rmdir('Paarthav')

# import built-ni sys module
import sys
print(sys.version)
# for line in sys.stdin: 
#     if 'q' == line.rstrip(): 
#         break
#     print(f'Input : {line}') 
 
# print("Exit") 
# sys.stdout.write('Geeks')

# def print_to_stderr(*a): 
#     print(*a, file = sys.stderr) 
 
# print_to_stderr("Hello World") 
# to exit sys
# sys.exit()
# To know the largest integer variable it takes
# print(sys.maxsize)
# To know environment path
# print(sys.path)
# To know the version of python you are using
# print(sys.version)


# Statistics Module
from statistics import * # Importing all the statistics modules
ages = [20,20,4,24,25,22,26,20,23,22,26]
print(mean(ages))
print(median(ages))
print(mode(ages))       # 20
print(stdev(ages))

# Math module
import math
print(math.pi)
print(math.sqrt(2))
print(math.pow(2,3))
print(math.floor(9.81))
print(math.ceil(9.81))
print(math.log10(100))


from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

# Exercise level 1
# 1. Write a function which generates a six digit/character random_user_id.
#   print(random_user_id());
#   '1ee33d'
import random
def random_user_id():
    return "".join(random.choice('0123456789abcdef') for _ in range(6))

print(random_user_id())


# 2. Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is 
# the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr
def user_id_gen_by_user():
    char_count = int(input("Enter the number of charcters: "))
    id_count = int(input("Enter the number of IDs: "))
    user_ids = []
    for _ in range(id_count):
        user_id = "".join(random.choice('0123456789abcdef') for _ in range(char_count))
        user_ids.append(user_id)
    return user_ids

print(user_id_gen_by_user())
# 3. Write a function named rgb_color_gen. It will generate rgb colors
# (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form
def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())

# Exercises: Level 2
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num_colors):
    return ["#"+ "".join(random.choice('0123456789abcdef') for _ in range(6)) for _ in range(num_colors)]
# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_colors):
    return [rgb_color_gen() for _ in range(num_colors)]
# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
def generate_colors(color_type,num_colors):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))

# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it
# returns a shuffled list
def shuffle_list(input_list):
    shuffle_list = input_list.copy()
    random.shuffle(shuffle_list)
    return shuffle_list

# Write a function which returns an array of seven random numbers in a 
# range of 0-9. All the numbers must be unique.
def seven_unique_numbers():
    return random.sample(range(10),7)

# Example usage:
my_list = [1, 2, 3, 4, 5]
shuffled_result = shuffle_list(my_list)
print("Shuffled List:", shuffled_result)

seven_numbers_result = seven_unique_numbers()
print("Seven Unique Numbers:", seven_numbers_result)

