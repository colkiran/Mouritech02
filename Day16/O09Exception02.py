
try:
    n = input("Enter a numerator :")
    d = input("Enter a denaminator greater than zero(>0) :")
    n = int(n)
    d = int(d)
    print(f"n :{n}")
    print(f"d :{d}")

    q = n / d

except ZeroDivisionError as z:
    print("exception occured......")
    print(z)
except ValueError as v:
    print(v)
except Exception as e:
    print(e)
else:
    print(f"q :{q}")
finally:
    print("completed the division of a number")
