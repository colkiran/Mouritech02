
class Player:                               # pascal casing

    def __init__(self):                     # constructor
        self.name = "Sachin"                # attributes or instance var
        self.age = 34
        print("Player Initialized......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")


    def __del__(self):
        print("-" * 40)
        print(self.name + " detroyed....")


ply1 = Player()
ply1.get_details()

print("-" * 40)
del ply1

ply2 = Player()
ply2.name = "Rahul"
ply2.age = 32
ply2.get_details()
