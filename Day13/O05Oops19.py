
from abc import ABC, abstractmethod

class Accounts(ABC):

    @abstractmethod
    def get_balance(self):
        pass


class Savings(Accounts):

    def deposit(self, a):
        print(f"Amount {a} debited into the account")

    def get_balance(self):
        print("The balance in the account is #####.##")


class Current(Accounts):

    def deposit(self, a):
        print(f"Amount {a} credited into the account")

    def get_balance(self):
        print("The balance in the account is #####.##")


cur = Current()
cur.deposit(10000)
