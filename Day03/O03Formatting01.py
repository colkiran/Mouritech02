
# emulate C style using printf

format = "Hello Mr.%s what a %s player"
print(f"format :{format}")
values = ("Sachin", 'superb')                   # tuples
print(f"values :{values}")
print(format % values)
print("Hello Mr.%s what a %s player at the age %d" % ("Sachin", "superb", 32))

print("-" * 40)
format = "Welcome %s, your rating of %.3f, what a player"
print(format % ("Sachin", 4))
print(format % ("Sachin", 4.78999))
print(format % ("Sachin", 4.79999))
print("Welcome %s, your rating of %.3f, what a player" % ("Sachin", 4.8000))


print("-" * 40)
# emulate unix shell syntax
from string import Template
temp = Template("Welcome $name, what a $adj player")
print(f"temp :{temp}")
print(temp.substitute(name = "Sachin", adj="class"))


# format of string from python
print("-" * 40)
# *args
print("Welcome {}, what a {} player for {}".format("Sachin", 'class', "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", 'class', "India"))
print("Welcome {1}, what a {2} player for {0}".format("India", "Sachin", 'class'))

print("-" * 40)
# **kwargs  => name="sachin"
print("Welcome {name}, what a {adj} player for {ctr}".format(ctr = "India", name ="Sachin",  adj='class'))

print("Welcome {name}, your rating of {rating} what a {adj} player".format(name= "Sachin", rating=4, adj="class"))

print("Welcome {name}, your rating of {rating:.3f} what a {adj} player".format(name= "Sachin", rating=4.8923, adj="class"))

#interpolation
from math import pi, e
print(f"PI = {pi} and Eulers constant e = {e}")

print("PI = {} and Eulers constant e = {}".format(pi, e))
print("PI = {0} and Eulers constant = {1} and magic number = {magic}".format(pi, e, magic=40585))

print("-" * 40)
fullname = ["Sachin", "Tendulkar"]
print("Mr. {name}".format(name = fullname))
print("Mr. {name[0]} {name[1]}".format(name = fullname))
# print("MR. {name}".format(name = fullname[0] + fullname[1]))

print("Conversions".center(40, "-"))
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("-" * 40)
print("The number {num} {num} {num}".format(num = 36))
print("The number {num} {num:f} {num:b}".format(num = 36))
print("The number {num:10} {num:f} {num:b}".format(num = 36))
print("The number {num:5} {num:f} {num:b}".format(num = 36))
print("The number {num:5} {num:f} {num:b}".format(num = 366788999))

print("alignment".center(40, "-"))
print("{num:15} Sachin".format(num=36))
print("{num:15} Tendulkar".format(num="Sachin"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("-" * 40)
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("-" * 40)
print("{pi:010.2}".format(pi=pi))
print("{pi:010.3}".format(pi=pi))

print("-" * 40)
print("{label:40}".format(label="Python"))
print("{label:*<40}".format(label="Python"))            # left align
print("{label:*^40}".format(label="Python"))            # center align
print("{label:*>40}".format(label="Python"))            # right align

print("\n")
print("{label:<40}".format(label="Python"))            # left align
print("{label:^40}".format(label="Python"))            # center align
print("{label:>40}".format(label="Python"))            # right align

print("-" * 40)
print("{0:<20} {1} {2:>20}".format("hello", "world", "hello"))
