
from datetime import datetime
import dateutils

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreateEmployee(cls, name, dob):
        actdt = datetime.strptime(dob, "%d/%m/%Y")
        ag = round(dateutils.years(datetime.now(), actdt), 0)
        return cls(name, int(ag))                # calls the constructor

    @staticmethod
    def CheckEligibility(age):
        return "Eligible" if age >= 35 else "Not Eligible"


emp1 = Employee("Jack", 35)
emp1.get_details()
print(f"{emp1.name} is {Employee.CheckEligibility(emp1.age)} to enroll for the course")
print("-" * 40)

emp2 = Employee.CreateEmployee("Jill", "12/10/1987")
emp2.get_details()
print(f"{emp2.name} is {Employee.CheckEligibility(emp2.age)} to enroll for the course")
