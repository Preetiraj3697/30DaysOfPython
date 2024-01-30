# class Person:
#     pass
# print(Person)

# p = Person()
# print(p)

# class Person:
#     def __init__ (self, name):
#         # self allows to attach parameter to the class
#         self.name = name

# p = Person('Paarthav')
# print(p.name)
# print(p)

# class Person:
#       def __init__(self, firstname, lastname, age, country, city):
#           self.firstname = firstname
#           self.lastname = lastname
#           self.age = age
#           self.country = country
#           self.city = city


# p = Person('Paarthav','Shah',22,'India','Faridabad')
# print(p.firstname)
# print(p.lastname)
# print(p.age)
# print(p.country)
# print(p.city)

# class Person:
#       def __init__(self, firstname, lastname, age, country, city):
#           self.firstname = firstname
#           self.lastname = lastname
#           self.age = age
#           self.country = country
#           self.city = city
#       def person_info(self):
#         return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

# p = Person('Paarthav','Shah',22,'India','Faridabad')
# print(p.person_info())

# class Person:
#       def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
#           self.firstname = firstname
#           self.lastname = lastname
#           self.age = age
#           self.country = country
#           self.city = city

#       def person_info(self):
#         return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

# p1 = Person()
# print(p1.person_info())
# p2 = Person('Paarthav','Shah',22,'India','Faridabad')
# print(p2.person_info())

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

# p1 = Person()
# print(p1.person_info())
# p1.add_skill('HTML')
# p1.add_skill('CSS')
# p1.add_skill('JavaScript')
# p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
# print(p2.person_info())
# print(p1.skills)
# print(p2.skills)

# class Student(Person):
#     pass


# s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
# s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
# print(s1.person_info())
# s1.add_skill('JavaScript')
# s1.add_skill('React')
# s1.add_skill('Python')
# print(s1.skills)

# print(s2.person_info())
# s2.add_skill('Organizing')
# s2.add_skill('Marketing')
# s2.add_skill('Digital Marketing')
# print(s2.skills)

class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

# Exercise Level 1
# 1. Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
class Statistics:
    def __init__(self,data):
        self.data = data
    
    def count(self):
        return len(self.data)
    def sum(self):
        return sum(self.data)
    def min(self):
        return min(self.data)
    def max(self):
        return max(self.data)
    def range(self):
        return max(self.data) - min(self.data)
    def mean(self):
        return sum(self.data) / len(self.data)
    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        middle = n//2
        if n % 2 == 0:
            return (sorted_data[middle-1]+sorted_data[middle]) / 2
        else:
            return sorted_data[middle]
    
    def mode(self):
        frequency = {}
        for value in self.data:
            frequency[value] = frequency.get(value, 0) + 1
        
        mode_value = max(frequency, key=frequency.get)
        mode_count = frequency[mode_value]
        
        return {'mode':mode_value, 'count':mode_count}
    
    def std(self):
        import math
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        return math.sqrt(variance)
    
    def var(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        return variance
    
    def freq_dist(self):
        frequency = {}
        for value in self.data:
            frequency[value] = frequency.get(value, 0) + 1
            
        freq_dist_list = [(count,value) for value,count in frequency.items()]
        return sorted(freq_dist_list, reverse=True)
    
    def describe(self):
        result = f"Count: {self.count()}\n"
        result += f"Sum: {self.sum()}\n"
        result += f"Min: {self.min()}\n"
        result += f"Max: {self.max()}\n"
        result += f"Range: {self.range()}\n"
        result += f"Mean: {self.mean()}\n"
        result += f"Median: {self.median()}\n"
        result += f"Mode: {self.mode()}\n"
        result += f"Variance: {self.var()}\n"
        result += f"Standard Deviation: {self.std()}\n"
        result += f"Frequency Distribution: {self.freq_dist()}\n"
        return result

data = Statistics(ages)
print(data.describe())

# 2. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self,firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}
    
    def add_income(self, description, amount):
        if description not in self.incomes:
            self.incomes[description] = 0
        self.incomes[description] += amount
    
    def add_expenses(self, description, amount):
        if description not in self.expenses:
            self.expenses[description] = 0
        self.expenses[description] += amount
    
    def total_income(self):
        return sum(self.incomes.values())
    
    def total_expenses(self):
        return sum(self.expenses.values())
    
    def account_balance(self):
        return self.total_income() - self.total_expenses()
    
    def account_info(self):
        info = f"{self.firstname} {self.lastname}'s Account Information:\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expenses()}\n"
        info += f"Account Balance: {self.account_balance()}\n"
        info += "Incomes:\n"
        for description, amount in self.incomes.items():
            info += f"  {description}: {amount}\n"
        info += "Expenses:\n"
        for description, amount in self.expenses.items():
            info += f"  {description}: {amount}\n"
        return info


# Example usage:
person_account = PersonAccount("John", "Doe")

person_account.add_income("Salary", 5000)
person_account.add_income("Freelance", 1000)

person_account.add_expenses("Rent", 1500)
person_account.add_expenses("Utilities", 200)
person_account.add_expenses("Groceries", 300)

print(person_account.account_info())

# John Doe's Account Information:
# Total Income: 6000
# Total Expense: 2000
# Account Balance: 4000
# Incomes:
#   Salary: 5000
#   Freelance: 1000
# Expenses:
#   Rent: 1500
#   Utilities: 200
#   Groceries: 300
