
"""
1. int
2. float
3. complex
4. bool
"""
a = 10
b = -10
print(f"a :{a}")                # f string - interpolation
print(type(a))                  # RTTI - runtime type indentification
print(f"b :{b}")
print(type(b))

print("-" * 40)
c = 10.3
d = -10.5
print(f"c :{c}")
print(type(c))
print(f'd :{d}')
print(type(d))

print("-" * 40)
e = 2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 40)
g = 10 + 2j
h = 10 - 2j

print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 40)
x = 2 + 3.5
print(type(x))

x = 2
y = 3.5
z = x + y

print("x =", type(x))
print('y =', type(y))
print('z =', type(z))

print("conversions".center(40, "-"))
a = 10
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(40, "-"))
print(11)                   # decimal number
print(f"0b11 :{0b11}")      # binary
print(f"0b101 :{0b101}")    # binary
print(f"0o11 :{0o11}")      # octal
print(f"0o101 :{0o101}")    # octal
print(f"0xe :{0xe}")        # hexa
print(f"0xa :{0xa}")        # hexa

print("Number system conversion".center(40, "-"))
a = 100
print(f"a :{a}")
print(f"bin(a) :{bin(a)}")
print(f"hex(a) :{hex(a)}")
print(f"oct(a) :{oct(a)}")
