# Exercises: Day 6
# Exercises: Level 1
# 1. Create an empty tuple
empty_tuple = ()
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("Alice","Eva","Grace") #Imaginary Sisters
brothers = ("Bob","Charlie","David") #Imaginary brothers
# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
# 4. How many siblings do you have?
num_siblings = len(siblings)
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father = "John"
mother = "Mary"
family_member = (father,mother) + siblings;
# print the results
print("Empty Tuple",empty_tuple);
print("Siblings",siblings)
print("Number of Siblings",num_siblings)
print("Family Members:",family_member)

# Exercise Level 2
# 1. Unpack siblings and parents from family_members
father, mother, *remaining_siblings = family_member
# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Apple","Banana","Orange")
vegetables = ("Carrot","Broccoli","Spinach")
animal_products = ("Chicken","Beef","Eggs")
# Join the three tuples
food_stuff_tp = fruits + vegetables + animal_products
# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2
middle_item_tp = food_stuff_tp[middle_index]
middle_items_It = food_stuff_lt[middle_index-1:middle_index+1]
# 5. Slice out the first three items and the last three items from food_staff_lt list
first_three_items_It = food_stuff_lt[:3]
last_three_items_It = food_stuff_lt[-3:]
# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp
# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# 8. Check if 'Estonia' is a nordic country
estonia_in_nordic = "Estonia" in nordic_countries;
# 9. Check if 'Iceland' is a nordic country
iceland_in_nordic = "Iceland" in nordic_countries;

# Print the results
print("Father:", father)
print("Mother:", mother)
print("Remaining Siblings:", remaining_siblings)
print("Food Stuff List:", food_stuff_lt)
print("Middle Item in List:", middle_item_tp)
print("Middle Items in List:", middle_items_It)
print("First Three Items in List:", first_three_items_It)
print("Last Three Items in List:", last_three_items_It)
print("Estonia in Nordic Countries:", estonia_in_nordic)
print("Iceland in Nordic Countries:", iceland_in_nordic)
