# Exception Handling
python uses try and except to handle errors gracefully. A graceful exit (or graceful handling) of errors is a simple programming idiom - a program detects a serious error condition and 'exist gracefully', in a controlled manner as a result. Often the program prints a descriptive error message to a terminal or log as part of the graceful exit, this makes our application more robust. The cause of an exception is often external to the program itself. An example of exceptions could be an incorrect input, wrong file name, unable to find a file, a malfunctioning IO device. Graceful handling of errors prevents our applications from crashing.
We have covered the different Python error types in the previous section. If we use try and except in our program, then it will not raise errors in those blocks.
<img src="https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/images/try_except.png" alt="error" />

```py
try:
   code in this block if things go well
except:
   code in this block run if things go wrong
```
Example:
```py
try:
    print(10+'5')
except:
    print('Something went wrong')
```
In the example above the second operand is a string. We could change it to float or int to add it with the number to make it work. But without any changes, the second block, except, will be executed.
```py
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
```
```sh
Something went wrong
```
In the above example, teh exception block will run and we do not know exactly the problem. To analyze the problem, we can use the different error types with except.
In the following example, it will handle the error and will also tell use the kind of error raised.
```py
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
```
```sh
Enter your name:Paarthav
Year you born:2001
Type error occured
```
In the code above the output is going to be TypeError. Now, let's add an additional block:
```py
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')
```
```sh
Enter your name:Paarthav
Year you born:2001
You are Paarthav. And your age is 18.
I usually run with the try block
I alway run.
```
it is also shorten the above code as follows:
```py
try:
    name = input('Enter your name: ')
    year_born = input('Year you born: ')
    age = 2024 - int(year_born)
    print(f'You are {name}. And your age is {age}')
except Exception as e:
    print(e)
```
# Packing and Unpacking Arguments in Python
We use two operators:
- * for tuples
- ** for dictionaires
Let us takes as an example below. It takes only arguments but we have list. We can unpack the list and changes to argument.
### Unpacking
Unpacking List
```py
def sum_of_five_nums(a,b,c,d,e):
    return a+b+c+d+e
lst = [1,2,3,4,5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```
When we run the this code, it raises an error, because this function takes numbers (not a list) as arguments. Let us unpack/destructure the list.
```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```
We can also use unpacking in the range built-in function that expects a start and an end.
```py
numbers = range(2,7) # normal call with separate arguments
print(list(numbers)) # [2,3,4,5,6]
args = [2,7]
numbers = range(*args) # call with arguments unpacked from a list
print(numbers) # range(2,7)

```
A list or a tuple can also be unpacked like this:
```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```
Unpacking Dictionaries
```py
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
```
# Packing
Sometimes we never know how many arguments need to be passed to a python function. We can use the packing method to allow our function to take unlimited number or arbitrary number of arguments.
### Packing Lists
```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```
Packing Dictionaries
```py
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Paarthav",
      country="India", city="Faridabad", age=22))
```
```sh
name = Paarthav
country = India
city = Faridabad
age = 22
{'name': 'Paarthav', 'country': 'India', 'city': 'Faridabad', 'age': 22}
```
# Spreading in Python
Like in Javascript, spreading is possible in python. Let us check it in an example below:
```py
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```
# Enumerate
if we are interested in an index of list, we use enumerate built-in function to get the index of each item in the list.
```py
for index, item in enumerate([20,30,40]):
    print(index,item)
# output
# 0 20
# 1 30
# 2 40
```
```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')
```
```sh
# output
hi
The country Finland has been found at index 0
hi
hi
hi
hi
```
# Zip
Sometimes we would like to combine lists when looping through them. See the example below:
```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```
```sh
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
```




