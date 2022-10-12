
# class Method

class Player:

    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor......")


    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    # @classmethod
    # def ChangeTeam(cls, tm):
    #     cls.team = tm

    @classmethod
    def CreatePlayer(cls, firstnm, lastnm, age):
        print("factory")
        return cls(f"Mr.{firstnm} {lastnm}", age)      # calls the constructor


ply1 = Player("Virat", 34)
ply1.get_details()

print("-" * 40)
ply2 = Player.CreatePlayer("Rohit", "Sharma", 33)
ply2.get_details()

# print("-" * 40)
# Player.ChangeTeam("MI")
# print(Player.team)
# print(ply1.team)
# print(ply2.team)