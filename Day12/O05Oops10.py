
class Employee:

    def __init__(self, name):
        self.name = name
        self.tech = ['C++', 'C#', 'ASP.net', 'VB.net', 'Sql Server', 'SSIS', 'SSRS', 'SSAS', 'ReactJS']


    def __str__(self):
        return f"Name is {self.name}"

    def __iter__(self):
        return iter(self.tech)

    def __getitem__(self, idx):
        return self.tech[idx]

    def __setitem__(self, idx, val):
        self.tech[idx] = val

    def append(self, val):
        self.tech.append(val)


emp1 = Employee("Mike")
print(emp1)
print("-" * 40)

print([t for t in emp1])                # list comprehension
print("-" * 40)

tech = emp1[4]
print(tech)
print("-" * 40)

emp1[3] = 'Entity Frame Work'
print([t for t in emp1])

print("-" * 40)
emp1.append("Python")
print([t for t in emp1])
