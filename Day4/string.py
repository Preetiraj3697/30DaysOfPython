
# Single line comment
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# Multiline String
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String Concatenation
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 15

#### Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2] # 
print(pto) # pto

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

## String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`

# endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# format()	formats string into nicer output    
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0

# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Checks Decimal Characters

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True


# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

# strip(): Removes both leading and trailing characters

challenge = ' thirty days of python '
print(challenge.strip('y')) # 5

# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split():Splits String from Left

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']

# title(): Returns a Title Cased String

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase(): Checks if String Starts with the Specified String
  
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False

# Exercise
# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# Strings to be concatenated
string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
# Concatenating the strings
result_string = string1 + ' ' + string2 + ' ' + string3 + ' ' + string4
# Displaying the result
# print(result_string)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str1,str2,str3 = "Coding","For","All"
res = str1 + " " + str2 + " " + str3
print(res);

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
# 4. Print the variable company using print().
print(company);

# 5. Print the length of the company string using len() method and print().
length = len(company);
print(length);

# 6. Change all the characters to uppercase letters using upper() method.
capital = company.upper();
print(capital);

# 7. Change all the characters to lowercase letters using lower() method.
CharLower = company.lower();
print(CharLower);
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
string = "Hello friend in pythod WORLD"
capitalStr = string.capitalize();
titleStr = string.title();
swapStr = string.swapcase();
print(capitalStr)
print(titleStr)
print(swapStr)
# 9. Cut(slice) out the first word of Coding For All string.
first_word = company.split()[0]
print("First Word:", first_word)
# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
contains_coding_index = company.index('Coding') if 'Coding' in company else -1
contains_coding_find = company.find('Coding') if 'Coding' in company else -1
contains_coding_other = 'Coding' in company
# Display the results
print("Index of 'Coding':", contains_coding_index)
print("Find 'Coding':", contains_coding_find)
print("Contains 'Coding':", contains_coding_other)
# 11. Replace the word coding in the string 'Coding For All' to Python.
ReplaceWord = company.replace("Coding","Python")
print(ReplaceWord);
# 12. Change Python for Everyone to Python for All using the replace method or other methods.
# Original string
original_string = "Python for Everyone"
# Replace 'Everyone' with 'All'
new_string = original_string.replace('Everyone', 'All')
# Display the result
print("Original String:", original_string)
print("Updated String:", new_string)

# 13. Split the string 'Coding For All' using space as the separator (split()) .
split_res = company.split()
print(split_res);

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
it_company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_it_res = it_company.split(",")
print(split_it_res);

# 15. What is the character at index 0 in the string _Coding For All_.
# Original string
text = "_Coding For All_"
# Get the character at index 0
character_at_index_0 = text[0]
# Display the result
print("Character at index 0:", character_at_index_0)

# 16. What is the last index of the string _Coding For All_.
# Original string
text = "_Coding For All_"
# Get the character at index 0
character_at_index_last = text[len(text)-1]
# Display the result
print("Character at index last:", character_at_index_last)
# 17. What character is at index 10 in "Coding For All" string.
company = "Coding For All"
index_10 = company[10];
print("Character at index 10:", index_10)
# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
PFE = "Python For Everyone"
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
CFA = "Coding For All"
# 20. Use index to determine the position of the first occurrence of C in Coding For All.
# Original string
text = "Coding For All"
# Find the position of the first occurrence of 'C'
position_of_C = text.index('C')
# Display the result
print("Position of the first occurrence of 'C':", position_of_C)

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
# Original string
text = "Coding For All"
# Find the position of the first occurrence of 'C'
position_of_F = text.index('F')
# Display the result
print("Position of the first occurrence of 'F':", position_of_F)

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
# Original string
text = "Coding For All People"
# Find the position of the last occurrence of 'l'
position_of_last_l = text.rfind('l')
# Display the result
print("Position of the last occurrence of 'l':", position_of_last_l)


# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
# Using index
position_of_because = sentence.index('because')
# Or using find
# position_of_because = sentence.find('because')
print("Position of the first occurrence of 'because':", position_of_because)


# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
position_of_last_because = sentence.rindex('because')
print("Position of the last occurrence of 'because':", position_of_last_because)

# 25. Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase_sliced = sentence[sentence.find('because'):sentence.rfind('because') + len('because')]
print("Sliced phrase:", phrase_sliced)

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
position_of_first_because = sentence.find('because')
print("Position of the first occurrence of 'because':", position_of_first_because)


# 27. Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase_sliced_again = sentence[position_of_first_because:position_of_last_because + len('because')]
print("Sliced phrase again:", phrase_sliced_again)

# 28. Does '\'Coding For All' start with a substring _Coding_?
string_with_backslash = '\Coding For All'
starts_with_Coding = string_with_backslash.startswith('Coding')
print("Starts with 'Coding':", starts_with_Coding)

# 29. Does 'Coding For All' end with a substring _coding_?
string_to_check = 'Coding For All'
ends_with_coding = string_to_check.endswith('coding')
print("Ends with 'coding':", ends_with_coding)

# 30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
string_with_spaces = '  Coding For All    '
trimmed_string = string_with_spaces.strip()
print("Trimmed String:", trimmed_string)

# 31. Which one of the following variables return True when we use the method isidentifier():
#     - 30DaysOfPython
#     - thirty_days_of_python
# Testing isidentifier() method
variable1 = '30DaysOfPython'
variable2 = 'thirty_days_of_python'
is_identifier_variable1 = variable1.isidentifier()
is_identifier_variable2 = variable2.isidentifier()
print("Variable1 is identifier:", is_identifier_variable1)
print("Variable2 is identifier:", is_identifier_variable2)


# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(python_libraries)

print("Joined list with hash and space: #", joined_libraries)

# 33. Use the new line escape sequence to separate the following sentences.
#     I am enjoying this challenge.
#     I just wonder what is next.
sentence1 = "I am enjoying this challenge."
sentence2 = "I just wonder what is next."
separated_sentences = f"{sentence1}\n{sentence2}"
print("Separated sentences with new line:")
print(separated_sentences)

# 34. Use a tab escape sequence to write the following lines.
#     Name      Age     Country   City
#     Asabeneh  250     Finland   Helsinki
header = "Name\tAge\tCountry\tCity"
data = "Asabeneh\t250\tFinland\tHelsinki"
print("Formatted lines with tab:")
print(header)
print(data)

# 35. Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
formatted_text = f"The area of a circle with radius {radius} is {area} meters square."
print(formatted_text)


# 36. Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6

addition = f"{a} + {b} = {a + b}"
subtraction = f"{a} - {b} = {a - b}"
multiplication = f"{a} * {b} = {a * b}"
division = f"{a} / {b} = {a / b:.2f}"
remainder = f"{a} % {b} = {a % b}"
floor_division = f"{a} // {b} = {a // b}"
exponentiation = f"{a} ** {b} = {a ** b}"

print(addition)
print(subtraction)
print(multiplication)
print(division)
print(remainder)
print(floor_division)
print(exponentiation)
