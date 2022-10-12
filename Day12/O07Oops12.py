
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, val):
        if val < 0:
            raise ValueError('Price cannot be less than zero(0)')
        else:
            self.__price = val

    def del_price(self):
        self.__price = 0

import sys
try:
    pepsi = Product(40)
    print(f"Price :{pepsi.get_price()}")

    print("-" * 40)
    pepsi.set_price(65)
    print(f"Price :{pepsi.get_price()}")

    print("-" * 40)
    pepsi.set_price(50)
    print(f"Price :{pepsi.get_price()}")

    print("-" * 40)
    pepsi.del_price()
    print(f"Price :{pepsi.get_price()}")

except:
    print("Exception Occured......")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
