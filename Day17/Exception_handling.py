# try:
#     print(10+'5')
# except:
#     print('something went wrong')
# # Examples:
# try:
#     name = input('Enter Your name: ')
#     year_born = input('Year you were born: ')
#     age = 2024 - year_born
#     print(f'You are {name}. And your age is {age}')
# except:
#     print('Something went wrong')

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occured')
# except ValueError:
#     print('Value error occured')
# except ZeroDivisionError:
#     print('zero division error occured')

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occur')
# except ValueError:
#     print('Value error occur')
# except ZeroDivisionError:
#     print('zero division error occur')
# else:
#     print('I usually run with the try block')
# finally:
#     print('I alway run.')
    
# try:
#     name = input('Enter your name: ')
#     year_born = input('Year you born: ')
#     age = 2024 - int(year_born)
#     print(f'You are {name}. And your age is {age}')
# except Exception as e:
#     print(e)

# def sum_of_five_nums(a,b,c,d,e):
#     return a+b+c+d+e
# lst = [1,2,3,4,5]
# print(sum_of_five_nums(lst))

# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(*lst))  # 15

# numbers = range(2,7)
# print(list(numbers))
# args = [2,7]
# numbers = range(*args)
# print(numbers)
# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
# numbers = [1, 2, 3, 4, 5, 6, 7]
# one, *middle, last = numbers
# print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

# def unpacking_person_info(name, country, city, age):
#     return f'{name} lives in {country}, {city}. He is {age} year old.'
# dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
# print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

# def sum_all(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(sum_all(1, 2, 3))             # 6
# print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Paarthav",
      country="India", city="Faridabad", age=22))

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, item in enumerate([20,30,40]):
    print(index,item)
    
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

# Exercises : Day17
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
# Unpack the first five countries and store them in a variable 
# nordic_countries, store Estonia 
# and Russia in es, and ru respectively.
*nordic_countries , es, ru = names

print("Nordic countries:", nordic_countries)
print("Estonia:", es)
print("Russia:", ru)
# Output
# Nordic countries: ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# Estonia: Estonia
# Russia: Russia