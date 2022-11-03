
class Singleton:

    __instance = None

    @staticmethod
    def get_intance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Single instance already exists...")
        else:
            Singleton.__instance = self


s1 = Singleton.get_intance()
print(s1)
s1.prod = "Car - Hyundai Tucson"
s1.color = "Red"


s2 = Singleton.get_intance()
print(s2)
print(s2.color)
print(s2.__dict__)


# s3 = Singleton()
# print(s3)