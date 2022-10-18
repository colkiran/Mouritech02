
import sys

n = input("Enter a numerator :")
d = input("Enter a denaminator greater than zero(>0) :")
n = int(n)
d = int(d)
print(f"n :{n}")
print(f"d :{d}")

try:
    q = n / d
    print(f"q :{q}")
except:
    print("exception occured......")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
