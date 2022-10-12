
class Animal:

    def __init__(self):
        print("Animal Ctor....")
        self.a = 10

    def eat(self):
        print("Animals eat.....")

# inheritance

class Bird(Animal):

    def fly(self):
        print("birds fly.......")

class Fish(Animal):

    def swim(self):
        print("Fishes Swim.......")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 40)
dolphin = Fish()
dolphin.eat()
dolphin.swim()

print("-" * 40)
print(cuckoo.__dict__)
print(dolphin.__dict__)

print("-" * 40)
print(f"isinstance(cuckoo, Animal): {isinstance(cuckoo, Animal)}")
print(f"isinstance(cuckoo, Bird): {isinstance(cuckoo, Bird)}")
print(f"isinstance(dolphin, Animal): {isinstance(dolphin, Animal)}")
print(f"isinstance(dolphin, Fish): {isinstance(dolphin, Fish)}")
print("-" * 40)

print(f"isinstance(cuckoo, Fish): {isinstance(cuckoo, Fish)}")
print(f"isinstance(dolphin, Bird): {isinstance(dolphin, Bird)}")
