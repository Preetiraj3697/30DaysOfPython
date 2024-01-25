# Modules
### What is a module
A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.

### Creating a Module
To create a module we write our codes in a python script and we save it as a .py file. Create a file named mymodule.py inside your project folder. Let us write some code in this file.
```py
# mymodule.py file
def generate_full_name(firstname,lastname):
    return firstname+' '+lastname

```
create main.py file in your project directory and import the mymodule.py file.
### Importing a Module
To import the file we use the import keyword and the name of the file only.

```py
# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```
### Import Functions from a Module
We can have many functions in a file and we can import all the functions differently.
```py
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname'])
```