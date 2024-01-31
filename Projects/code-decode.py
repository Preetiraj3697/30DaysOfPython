# Beginner Project

'''
you type a word 'preeti' you program check this secure key this secure key a certain rule:
1. if user type code more than and equal to 3 word that 1 word and append in last
2. put random 3 word in start and end of code
Example:
user_type = 'Paarthav'
program first check it more than 3 words => yes
than take 1 letter P put in last => aarthavP
append 3 random letter in code start and end => efgaarthavPqrs
else reverse it words 
example => of => fo
'''
import random

user_type = input('Enter your code name: ')
def generate_secure_key(user_type):
  length = len(user_type)
  if length >= 3 :
    first_letter = user_type[0]
    modified_code = user_type[1:] + first_letter
    random_prefix = ''.join(random.choices('abcedfghijkl', k=3))
    random_suffix = ''.join(random.choices('abcedfghijkl', k=3))
    security_key = random_prefix + modified_code + random_suffix
    print(f'Your secure key is {security_key}')
    return security_key
  elif length < 3:
    print(user_type[::-1])
  else:
    print('Something went wrong! :-<')
    
security_key = generate_secure_key(user_type)

# Decode the secure key
def decode_secure_key(security_key):
  length = len(security_key)
  if length >= 3 :
      # Remove start and end 3 random letter
      modified_code = security_key[3:-3]
      last_letter = modified_code[-1]
      decoded_user_type = last_letter + modified_code[:-1]
      print(f'your decode key is {decoded_user_type}')
  elif length < 3:
      print(security_key[::-1])
  else:
      print('Something Went Wrong!')

decode_secure_key(security_key)

