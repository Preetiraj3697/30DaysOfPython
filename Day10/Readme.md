# Loops
Lige is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming language use loops. Python programming language also provides the following type of two loops:
1. while loop
2. for loop
   
## While Loop
We use the reserved word while to make a while loop. It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.
#### Example:
```py
count = 0
while count < 5:
    print(count)
    count += 1
```
In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use else.
```py
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(count)
```
The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. As a result 5 will be printed.

### Break and Continue - Part 1
- Break: we use break when we like to get out of or stop the loop.
#### Example:
```py
count = 0
while count < 5:
  print(count)
  count = count + 1
   if count == 3:
        break
```
The above while loop only print 0, 1, 2 but when it reaches 3 it stops.
- Continue: With the continue statement we can skip the current iteration, and continue with the next.
```py
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

```
The above while loop only print 0, 1, 2, and 4 (skips 3).

### For Loop
A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#### Example in List:
```py
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
```
#### Example in String:
```py
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
```
#### Example in Tuple
```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
```
#### Example in dictionary
```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
```

#### Example in Set
```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

## Break and Continue - Part 2
short reminder: Break: we use break when we like to stop our loop before it is completed.
Example:
```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```
In the above example, the loop stops when it reaches 3.

Continue: We use continue when we like to skip some of the steps in the iteration of the loop.
```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
```
In the example above, if the number equals 3, the step after the condition (but inside the loop) is skipped and the execution of the loop continues if there are any iterations left.

## The Range Function
the range() function is used list of numbers. The range(start,end,step) takes three parameters: starting, ending and increment. by default it start from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequence using range.
```py
lst = list(range(11))
print(lst) # [0,1,2,3,4,5,6,7,8,9,10]
st = set(range(1,11))
print(st) # {1,2,3,4,5,6,7,8,9,10}
lst = list(range(0,11,2))
print(lst) # [0,2,4,6,8,10]
st = setst = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
```
```py
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
```

### Nested For Loop
we can write loops inside a loop.
```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

### For Else
if we want to execute some message when the loop ends, we use else.
```py
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
```

### Pass
in python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.

```py
for number in range(6):
    pass
```