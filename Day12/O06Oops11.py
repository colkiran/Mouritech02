
class Employee:

    def __init__(self, name):
        self.__name = name          # private variable
        self.tech = ['C++', 'C#', 'ASP.net', 'VB.net', 'Sql Server', 'SSIS', 'SSRS', 'SSAS', 'ReactJS']

    def __str__(self):
        return self.__name + " - " + ", ".join([t for t in self.tech])

emp1 = Employee("Stewart")
print(emp1)
print("-" * 40)

# print(emp1.__name)
print(emp1.__dict__)

print("-" * 40)
print(f"emp_name :{emp1._Employee__name}")

print("-" * 40)
emp1._Employee__name = "Kennedy"
print(emp1.__dict__)