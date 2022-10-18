
class TooOld(Exception):
    pass

class TooYoung(Exception):
    pass

class TooTiny(Exception):
    pass

try:
    age = int(input("Enter your age :"))

    if age < 10:
        raise TooTiny("Too very young to cast a vote.....")
    elif age < 18:
        raise TooYoung("Young and still not eligible to vote.....")
    elif age > 100:
        raise TooOld("Too old to cast the vote.....")
    else:
        print("please cast your valuable vote.......")

except TooOld as o:
    print(o)
except TooYoung as y:
    print(y)
except TooTiny as o:
    print(o)