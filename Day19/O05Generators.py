
l1 = [x ** 2 for x in range(1, 11)]
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l1 = (x ** 2 for x in range(1, 11))
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
s1 = sum([x ** 2 for x in range(1, 11)])
print(f"Sum of squares using compreshension :{s1}")

s2 = sum((x ** 2 for x in range(1, 11)))
print(f"Sum of squares using generator :{s2}")

print("-" * 40)
from sys import getsizeof

t1 = [x ** 2 for x in range(1, 10000)]
print(f"comprehension size of the list :{getsizeof(t1)}")

print("-" * 40)
t2 = (x ** 2 for x in range(1, 10000))
print(f"generator size of the list :{getsizeof(t2)}")

