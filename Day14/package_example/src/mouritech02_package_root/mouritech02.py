
gstname = "Rahul Dravid"

sports = ['cricket', 'football', 'hockey', 'snooker', 'swimming']

runs = {'test': 18500, 'odi': 14200, 't20': 1200}

def greet(gnm):
    print(f"Greetings Mr.{gnm}, Welcome to the event.......")

def sum(x, y):
    return x + y

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


    def get_details(self):
        print(f"Product name is {self.name}\nPrice is {self.price}")
