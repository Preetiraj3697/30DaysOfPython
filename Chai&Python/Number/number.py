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



