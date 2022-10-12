
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's job.....")

class Developer(Employee):

    def doJob(self):
        print("Developers job......")

Mike = Manager()
Dave = Developer()

def BankJob(emp):
    print("Bank job started......")
    emp.doJob()
    print("Bank job ended......")
    print("-" * 40)

BankJob(Mike)
BankJob(Dave)
