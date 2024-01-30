def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print('Seleted option from below: ')
print('A: Add your numbers')
print('B: Minus your numbers')
print('C: Multiply your numbers')
print('D: Divide Your numbers')
choice =  input("Please enter choice (a/ b/ c/ d): ")  
num1 = int(input('Enter you first number: '))
num2 = int(input('Enter you second number: '))


if choice.lower() == 'a':
   print(f'{num1}+{num2} = {plus(num1,num2)}')
elif choice.lower() == 'b':
    print(f'{num1}-{num2} = {minus(num1,num2)}') 
elif choice.lower() == 'c':
    print(f'{num1}X{num2} = {multiply(num1,num2)}') 
elif choice.lower() == 'b':
    print(f'{num1}/{num2} = {divide(num1,num2)}') 
else:
    print('Invalid Input you write!')

