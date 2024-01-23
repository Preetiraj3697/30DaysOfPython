# Sets

Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

### Creating a Set
we use the set() built-in function.
- Creating an empty set
  ```py
  # syntax
  st = set()
  ```
- Creating a set with initial items
  ```py
  # syntax
  st = {'item1','item2','item3','item4'}
  ```
Example:
```py
# syntax
fruits = {'banana','orange','mango','lemon'}
```

### Getting Set's Length
We use len() method to find the length of a set.
```py
#syntax
st = {'item1','item2','item3','item4'}
len(st)
```

### Accessing Items in Set
we use loops to access items. we will see this in loop section

### Checking an item
To check if an item exist in a list we use in membership operator.
```py
# syntax
st = {'item1','item2','item3','item4'}
print("Does set st contain item3?", 'item3' in st) # Does set st contain item3? True
```
### Adding Items to a set
Once a set is created we cannot change any items and we can also add additional items.
- Add one item using add()
```py
# syntax
st = {'item1','item2','item3','item4'}
st.add('item5')
```
- Add multiple items using update(). The update() allows to add multiple items to a set. The update() takes a list argunment.
```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])

```
### Removing Items from a set
We can remove an item from a set using remove() method. If the item is not found remove() method wil raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
```py
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```
The pop() methods remove a random item from a list and it returns the removed item.
### Example:

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
```
If we are interested in the removed item.
```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 
```

### Clearing Items in Set
if we want to clear or empty the set we use clear method.
```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear() # set()
```

### Deleting a set
if we want to delete the set itself we use del operator.
```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

### Converting List to set
we can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.
```py
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

```
#### Examples:
```py
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```

### Joining Sets
we can join two sets using the union() or update() method.
- Union This method returns a new set.
```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
```
Example:
```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

```
- update This method inserts a set into a given set
```py
# syntax
st1 = {'item1','item2','item3','item4'}
st2 = {'item5','item6','item7','item8'}
st1.update(st2) # st2 contents are added to st1
```
### Finding Intersection Items
Intersection returns a set of items which are in both the sets. See the example
```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
```
Example:
```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
```
### Checking Subset and Super set
A set can be a subset or super set of other sets:
- Subset: issubset()
- Super set: issuperset
```py
  # syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```
#### Example:
```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
```
### Checking the Difference Between Two Sets
it returns the difference between two sets.
```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
```
#### Example:
```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
```
### Finding Symmetric Difference Between Two Sets
It returns the symmetric difference between two sets. it means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) U (B\A)

#### Example:
```py
whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
some_numbers = {1,2,3,4,5}
whole_numbers.symmetric_difference(some_number) #{0,6,7,8,9,10}
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

```

### Joining Sets
if two sets do not have a common item or items or items we call them disjoint sets. we can check if two sets are joint or disjoint using isdisjoint() method.
```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```
#### Example:
```py
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}

```