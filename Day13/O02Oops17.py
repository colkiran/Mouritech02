
class Animal:

    def eat(self):
        print("Animals eat...")

class Bird(Animal):

    def fly(self):
        print("Birds fly.....")

class Chicken(Bird):

    def disp(self):
        print("Chickens are breeded for consumption.....")

    def fly(self):
        print("Chickens can seldom fly......")

chic = Chicken()
chic.eat()
chic.fly()
chic.disp()
