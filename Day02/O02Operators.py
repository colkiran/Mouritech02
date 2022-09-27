
"""
1. arithmetic Operators -   +, -, *, /, //, %. **
2. Augmentor Operators  -   =, +=, -=, /=, *=...
3. Relational or Comparison
4. Logical Operators
5. Bitwise Operators
6. Ternary Operators
"""

print("Arithmetic Operators".center(40, "-"))

print(f"10 + 3 = {10 + 3}")
print(f"10 - 3 = {10 - 3}")
print(f"10 * 3 = {10 * 3}")
print(f"10 / 3 = {10 / 3}")
print(f"10 // 3 = {10 // 3}")
print(f"10 % 3 = {10 % 3}")
print(f"10 ** 3 = {10 ** 3}")

print("Augmentor Operator".center(40, "-"))
x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("comparison operator".center(40, "-"))
a = 10
b = 20

print(f"a :{a}")
print(f"b :{b}")
print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a != b :{a != b}")

print("Logical Operators".center(40, "-"))
print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 1)

# or
print("-" * 40)
print(1 == 1 or 2 == 1)
print(1 == 2 or 2 == 1)

# not
print("-" * 40)
print(not(1 == 1 or 2 == 1))
print(not(1 == 2 or 2 == 1))

print("-" * 40)
print(ord("A"))         # integer representation of unicode
print(ord("Z"))
print(ord("a"))
print(ord("z"))

print("Bitwise operators".center(40, "-"))
print(5 | 3)
print(5 & 3)
print(5 ^ 3)
print(5 << 1)
print(8 << 1)
print(5 << 2)
print(16 >> 1)

print(5 >> 1)
print(~0)
print(~5)

print("ternary operator".center(40, "-"))
a = 12
print("Eligible" if a > 18 else "not eligible")
