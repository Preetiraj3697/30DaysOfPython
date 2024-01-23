# Exercises: Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1.
# 1. Find the length of the set it_companies
it_com_length =  len(it_companies)
print(it_com_length)
# 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update({"LinkedIn","Netflix","Tesla"})
print(it_companies)
# 4. Remove one of the companies from the set it_companies
it_companies.remove("IBM")
print(it_companies)
# 5. What is the difference between remove and discard
# The `remove` method removes the specified element from the set, but if 
# element is not present, it raises a 'keyError'.
# The `discard` method also removes the specified element, but if the
# element is not present, it does nothing (no error is raised).

# Exercises: Level 2
# 1. Join A and B
joined_sets = A.union(B)
print(joined_sets)
# 2. Find A intersection B
intersection_set = A.intersection(B)
print(intersection_set)
# 3. Is A subset of B
is_subset = A.issubset(B)
print(is_subset)
# 4. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print(are_disjoint)
# 5. Join A with B and B with A
# This question is a bit unclear. if you meant to join the sets and keep
# unique elements, you can use `union` as shown in question 6.
# 6. What is the symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B)
print(symmetric_diff)
# 7. Delete the sets completely
del it_companies, A, B
# print(it_companies)
# print(A)
# print(B)

# Exercises: level 3
# 1. Convert the ages to a set and compare the length of the list and 
# the set, which one is bigger?
age_set = set(age)
if len(age_set)>len(age):
    print("The set has more unique elements than the list.")
elif len(age_set)<len(age):
    print("The list has more unique elements than the set.")
else:
    print("Both have the same number of unique elements.")
    
# 2. Explain the difference between the following data types: 
# string, list, tuple and set
# - String : A sequence of characters, immutable.
# - List : An ordered collection of items, mutable.
# - Tuple: An ordered, immutable collection of items.
# - Set: An unordered collection of unique items.

# 3. I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = set(sentence.split())
unique_word_count = len(words)
print(words)
print(unique_word_count)

