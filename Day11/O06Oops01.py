
class Player:

    def get_runs(self):
        print(self.__class__)
        print("runs scored......")

sachin = Player()
sachin.get_runs()
print("-" * 40)

print(type(sachin))
print(sachin.__class__)
