
class Player:

    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name} :{self.age}")

ply1 = Player('Rohit', 34)
ply1.get_details()

ply2 = Player("Virat", 33)
ply2.get_details()

print("-" * 40)

print(f"Player :{Player.team}")
print(f"ply1 :{ply1.team}")
print(f"ply2 :{ply2.team}")

print("-" * 40)
Player.team  = "MI"

print(f"Player :{Player.team}")
print(f"ply1 :{ply1.team}")
print(f"ply2 :{ply2.team}")

print("-" * 40)
ply2.team = "RCB"
print(ply2.team)
print(f"Player :{Player.team}")
print(f"ply1 :{ply1.team}")

print("-" * 40)
print(ply2.__dict__)

print("-" * 40)
print(Player.__dict__)
