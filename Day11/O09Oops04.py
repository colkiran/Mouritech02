"""
self will implicitly takes the name of the object that called the method

ply1.get_details => self - ply1


"""
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized.....")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 30)
ply1.get_details()

print("-" * 40)
ply2 = Player("Virat", 28)
ply2.get_details()

print("-" * 40)
print("ply1 :", ply1.__dict__)
print("ply2 :", ply2.__dict__)


print("-" * 40)
ply2.runs = 130
print("ply2 :", ply2.__dict__)
print("ply1 :", ply1.__dict__)
