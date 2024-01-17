
# Install
1. Go to [Website](https://www.python.org)
 <img src="https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/images/installing_on_macOS.png" alt="python website">

 - # Some time you facing this issue
  ### python was not found; run without arguments to install from the microsoft store, or disable this shortcut from settings > manage app execution aliases.

For most people, the simple fix is to install Python from the official Python website and check the "Add Python to environment variables" option during installation.

Step 1: Locate Your Python Installation Paths

First, you need to find the paths where your Python interpreter is installed. The paths are usually one of the below:
%AppData%\Programs\Python\Python311
%AppData%\Programs\Python\Python311\Scripts

Step 2: Access and set the path Environment Variables
 
 search for "Environment Variables" in Windows search as shown below:
 <img src="https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/blogpost/solving-python-not-found/step-1-search-for-environment-variables.png" alt="environment">

 Navigate to the System Properties, and then click on the "Environment Variables" button.

<img src="https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/blogpost/solving-python-not-found/step2-system-properties.png" alt="environment">

Step 3: Modify the System Variables

Click on the "System variables" and then click "Path" as shown below

<img src="https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/blogpost/solving-python-not-found/step3-system-variable.png" alt="environment">

After you select the "Path" variable, click "Edit."

<img src="https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/blogpost/solving-python-not-found/step4-edit-system-variable.png" alt="environment">

Click "New" and then Add the previously copied Python paths to the list.

<img src="https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/blogpost/solving-python-not-found/step-5-click-new.png" alt="environment">

This is what it will look like:

<img src="https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/blogpost/solving-python-not-found/edit-environment-variable-dialogue.png" alt="environment">

Note: The key to solving this issue lies in adding the Python paths to the System variables, not the User variables. I initially made the mistake of using the User variables, which led to another error. Hence, I want to make sure you do not repeat the mistake I did!

To check if python is installed write the following command on your device terminal.

```
python --version  
``` 
<img src="https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/images/python_versio.png" alt="cmd">


# Python Shell
Python is an interpreted scripting language, so it does not need to be compiled. It means it executes the code line by line. Python comes with a Python Shell (Python Interactive Shell). It is used to execute a single python command and get the result.

Python Shell waits for the Python code from the user. When you enter the code, it interprets the code and shows the result in the next line. Open your terminal or command prompt(cmd) and write:
```
python
```
<img src="https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/images/adding_on_python_shell.png" alt="shell">

# Data types
In Python there are several types of data types. Let us get started with the most common ones. Different data types will be covered in detail in other sections. For the time being, let us just go through the different data types and get familiar with them. You do not have to have a clear understanding now.

## Number

Integer: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
Complex Example 1 + j, 2 + 4j


## String

A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.

Example:

```python
'Asabeneh'
'Finland'
'Python'
'I love teaching'
```
'I hope you are enjoying the first day of 30DaysOfPython Challenge'
Booleans
A boolean data type is either a True or False value. T and F should be always uppercase.

Example:

    ```python
    True  #  Is the light on? If it is on, then the value is True
    False # Is the light on? If it is off, then the value is False
    ```

## List

Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.

Example:

```python
[0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers
['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits)
['Finland','Estonia', 'Sweden','Norway'] # all the same data types - a list of strings (countries)
['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float
```
## Dictionary

A Python dictionary object is an unordered collection of data in a key value pair format.

Example:

```python
{
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}
```
## Tuple

A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.

Example:

```python
('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # planets
```

## Set

A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.

In later sections, we will go in detail about each and every Python data type.

Example:

```python
{2, 4, 3, 5}
{3.14, 9.81, 2.7} # order is not important in set
```
