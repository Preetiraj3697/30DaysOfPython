# Assignment operators
# x = 5
# x += 3
# x -= 4
# x *= 5
# x /= 4
# x %= 4
# x //= 5
# x **= 5
# x &= 3
# x |= 5
# x ^= 6
# x >>= 5
# x <<= 6


# Arithmetic Operators
# Addition(+): a + b
# Subtraction(-): a - b
# Multiplication(*): a * b
# Division(/): a / b
# Modulus(%): a % b
# Floor division(//): a // b
# Exponentiation(**): a ** b

# Arithmetic Operations in Python
# Integers
print('Addition: ', 1+2);
print('Substraction: ',4-2)
print('Multiplication ',3*6)
print("Division ",4/2)
print("Division Without the remainder: ", 7//2)
print("Modulus ",3%2)
print('Exponentiation ', 2**3)


# Floats
print("Floating Point Number, PI", 3.14)
print("Floating Point Number, gravity", 9.81)

# Complext Number
print('Complex number: ',1+1j)
print('Multiplying complex number: ',(1+1j)*(1-1j));

# Declaring the variable at the top first
a=6
b=2
# Arithmetic operations and assigning the result to a variable
total = a+b
diff = a-b
product = a*b
division = a/b
remainder = a%b
floor_division = a//b
exponential = a**b

print(total);
print('a+b =',total)
print("a-b = ",diff)
print('a*b = ',product)
print('a/b = ',division)
print('a % b = ', remainder)
print('a//b = ',floor_division)
print('a**b = ', exponential)

print("== Addition, Subtraction, Multiplication, Division, Modulus ==")
# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

# CalCulating area of a circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print('Area of a circle: ', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle: ', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity;
print(weight, 'N');

# Calculate the density of a liquid
mass = 75
volume = 0.075
density = mass / volume
print('density: ',density);


# Comparison Operators
# x==y Equal
# x!=y Not equal
# x>y Greater than
# x<y Less than
# x>=y Greater then or equal to
# x<=y Less than or equal to

print(3>2);
print(3>=2)
print(3<2)
print(2<3)
print(3==2)
print(3!=2)
print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print(len('mango') < len('avocado'))
print(len('milk') != len('meat'))
print(len('milk') == len('meat'))
print(len('tomato') == len('potato'))
print(len('python') > len('dragon'))

# comparing something gives either a true or false
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

# In addition to the above comparison operator Python uses:

# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x in y
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# Logical Operators
# operator = and , or ,not 
# Returns True if both statements are true in and
# Returns True if one of the statements is true in or
# Reverse the result, REturn false if the result is true


print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False


# Exercise - Day3
# 1. Declare your age as integer variable
age = 10
# 2. Declare your height as a float variable
height = 5.8
# 3. Declare a variable that store a complex number
complex_number = 1+3j
# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
Base = int(input('Enter Base: '))
Height = int(input("Enter height: "))
area_of_triangle = 0.5 * Base * Height;
print('Area of the Triangle is', int(area_of_triangle))
# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = int(a+b+c);
print("The Perimeter of the triangle is :", perimeter)
# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input('Length of Rectangle: '))
width = int(input('Enter width of rectangle: '))
area_of_rectangle = int(2 * (length+width))
# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
radius = int(input("Enter radius of circle: "))
area_of_circle = int(pi * radius * radius)
circumference_of_circle = int(2 * pi * radius);
print('Area of circle ', area_of_circle);
print('Circumference of circle ', circumference_of_circle);
# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Equation: y = 2x - 2
# Coefficients
slope = 2
# x-intercept: Set y = 0 and solve for x
x_intercept = 0
# y-intercept: Set x = 0 and solve for y
y_intercept = -2
# Print the results
print(f"Slope: {slope}")
print(f"x-intercept: {x_intercept}")
print(f"y-intercept: {y_intercept}")

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Coordinates of the points
x1, y1 = 2, 2
x2, y2 = 6, 10
# Calculate slope
slope = (y2 - y1) / (x2 - x1)
# Calculate Euclidean distance
euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# Print the results
print(f"Slope: {slope}")
print(f"Euclidean Distance: {euclidean_distance}")

# 10. Compare the slopes in tasks 8 and 9.
# Slope of the equation y = 2x - 2
slope_task_8 = 2
# Slope between points (2, 2) and (6, 10)
slope_task_9 = (10 - 2) / (6 - 2)
# Compare slopes
if slope_task_8 == slope_task_9:
    print("The slopes are equal.")
else:
    print("The slopes are not equal.")

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# Coefficients of the quadratic equation
a = 1
b = 6
c = 9
# Calculate the discriminant
discriminant = b**2 - 4*a*c
# Check if the discriminant is non-negative (real roots)
if discriminant >= 0:
    # Calculate the two roots using the quadratic formula
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)

    print("Root 1:", root1)
    print("Root 2:", root2)
else:
    print("No real roots. Discriminant is negative.")

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# Length of the words
length_python = len('python')
length_dragon = len('dragon')
# Falsy comparison statement
falsy_comparison = length_python == length_dragon
# Print the results
print(f"Length of 'python': {length_python}")
print(f"Length of 'dragon': {length_dragon}")
print(f"Falsy Comparison: {falsy_comparison}")

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
# Strings
word_python = 'python'
word_dragon = 'dragon'
# Check if 'on' is found in both words
found_in_python = 'on' in word_python
found_in_dragon = 'on' in word_dragon
# Use 'and' operator for the check
both_contain_on = found_in_python and found_in_dragon
# Print the results
print(f"Is 'on' found in 'python'? {found_in_python}")
print(f"Is 'on' found in 'dragon'? {found_in_dragon}")
print(f"Both words contain 'on': {both_contain_on}")

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon"
containe_jargon = 'jargon' in sentence;
print(f"Does sentence container word of jargon? {containe_jargon}")

# 15. There is no 'on' in both dragon and python
# check if  'on' is not found in both words
not_found_in_python = 'on' not in word_python
not_found_in_dragon = 'on' not in word_dragon
# use and operator for check
both_do_not_contain_on = not_found_in_python and not_found_in_dragon
#Print the results
print(f"Both word don't containe 'on': {both_do_not_contain_on}")


# 16. Find the length of the text python and convert the value to float and convert it to string
length_of_python = len('python');
float_len = float(length_of_python)
string_len = str(float_len)

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

number = int(input('Enter number: '))
if(number % 2 == 0):
    print("This is Even Number")
else:
    print("This is Odd Number")

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# Floor division of 7 by 3
floor_division_result = 7 // 3
# Convert 2.7 to an integer
int_value_of_2_7 = int(2.7)
# Check if the floor division result is equal to the integer-converted value of 2.7
is_equal = floor_division_result == int_value_of_2_7
# Print the results
print(f"Floor division of 7 by 3: {floor_division_result}")
print(f"Integer converted value of 2.7: {int_value_of_2_7}")
print(f"Are they equal? {is_equal}")

# 19. Check if type of '10' is equal to type of 10
if(type('10')==type(10)):
    print("Equal")
else:
    print("Not Equal")
# 20. Check if int('9.8') is equal to 10
result2 = float('9.8') == 10
print(result2)
# 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Prompt user for input
hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
# Calculate pay
pay = hours * rate_per_hour
# Display the result
print(f"The pay is: {pay}")

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Prompt user for input
years = float(input("Enter the number of years: "))
# Calculate the number of seconds in a hundred years
seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
days_per_year = 365
total_seconds_in_a_hundred_years = 100 * days_per_year * hours_per_day * minutes_per_hour * seconds_per_minute
# Calculate the number of seconds a person can live
seconds_lived = years * days_per_year * hours_per_day * minutes_per_hour * seconds_per_minute

# Display the results
print(f"In {years} years, a person can live approximately {seconds_lived:.0f} seconds.")
print(f"If a person lives for a hundred years, they would have lived approximately {total_seconds_in_a_hundred_years:.0f} seconds.")

# 23. Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')
