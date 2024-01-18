# day2: 30 day of python programming
first_name = "Paarthav";
last_name = "Shah";
full_name = first_name + last_name;
country = "India"
city = "Faridabad"
age = 22;
year = 2024;
is_married = False;
is_true = True;
is_light_On = False;
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
# print(first_name,last_name,full_name);
# print(country,city,age,year);
# print(is_married,is_true,is_light_On);

# Declare multiple variable on one line

name,state,study,year = "Preeti","Haryana","Full-stack","2023";
# print(name,state,study,year);


# check data type
# print(type(first_name));
# print(len(first_name));
# print(type(len(last_name)))

num_one = 5;
num_two = 4;
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one/ num_two
exp = num_one ** num_two;
floor_division = int(num_one/ num_two)
# print(total, diff, product, division, exp , floor_division);

# radius of a circle in 30 meters
r = input("Write you radius of circle: ");
pi = 3.14;
area_of_circle = pi*int(r)**2;
# print(int(area_of_circle));
circum_of_circle = 2* pi *int(r);
# print(int(circum_of_circle));

# Use the built-in input function to get first name, last name,
# country and age from a 
# user and store the value to their corresponding variable names
first_name = input("Enter you first Name: ");
last_name = input("Enter your last name: ");
country = input("Enter your Country name: ");
age = int(input("Enter your age: "));
user = {first_name, last_name,country,age};
# print(user);


# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
# print(type('Asabeneh'))     # str
# print(type(first_name))     # str
# print(type(10))             # int
# print(type(3.14))           # float
# print(type(1 + 1j))         # complex
# print(type(True))           # bool
# print(type([1, 2, 3, 4]))     # list
# print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
# print(type((1,2)))                                              # tuple
# print(type(zip([1,2],[3,4])))                                   # set


# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']