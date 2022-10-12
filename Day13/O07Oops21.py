# Duck Types

class Manager():

    def doJob(self):
        print("Manager's job.....")

class Developer():

    def doJob(self):
        print("Developers job......")

Mike = Manager()
Dave = Developer()

def BankJob(emps):
    print("Bank job started......")
    for emp in emps:
        emp.doJob()
    print("Bank job ended......")
    print("-" * 40)

BankJob([Mike, Dave])
