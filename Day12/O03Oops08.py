
from functools import total_ordering

@total_ordering                 # mandatory to overload __eq__ and any one cmp operator
class Employee:

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):            # works for not equal to also
        return self.age == other.age

emp1 = Employee("Peter", 55000, 32)
print(emp1)

print("-" * 40)
emp2 = Employee("Richard", 45000, 35)
print(emp2)

print("-" * 40)
# print(emp1 == emp2)              # compares the adresses, __eq__

if emp1 != emp2:
    print("{}'s salary of {} is NOT equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 40)
if emp1 > emp2:
    print("{}'s salary of {} is Greater Than {}'s salary of {}".format(emp1.name, emp1.age, emp2.name, emp2.age))
else:
    print("{}'s salary of {} is Not Greater Than {}'s salary of {}".format(emp1.name, emp1.age, emp2.name, emp2.age))

print("-" * 40)
print(emp1 >= emp2)

print("-" * 40)
print(emp1 <= emp2)
