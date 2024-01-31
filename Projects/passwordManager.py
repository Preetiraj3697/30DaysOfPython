# Beginner Project

from cryptography.fernet import Fernet

# key + password + text to encrypt = random text
# random text + key + password = text to encrypt
"""def write_key():
    key = Fernet.generate_key()
    with open('./Projects/key.key', 'wb') as key_file:
        key_file.write(key)"""

def load_key():
    file =  open('./Projects/key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('./Projects/password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f'Account: {user} and Password: {fer.decrypt(passw.encode()).decode()}')
        

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('./Projects/password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
   mode = input('Would you like to add a new password or view existing ones (view, add), press q to quit? ').lower() 
   if mode == 'q':
       break

   if mode == 'view':
       view()
   elif mode == 'add':
        add()
   else:
      print('Invalid mode.')
      continue
  
  
