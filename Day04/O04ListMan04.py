
print("{:-^40}".format("clear"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

print("count".center(40, "-"))
l1 = [1, 2, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 2, 2, 1, 2, 3]
print(f'1 :{l1.count(1)}')
print(f'2 :{l1.count(2)}')
print(f'3 :{l1.count(3)}')
print(f'4 :{l1.count(4)}')

print("index".center(40, "-"))
l1 = [1, 2, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 2, 2, 1, 2, 3]

print(l1.index(3))

print(l1.index(3, l1.index(3) + 1))

print(l1.index(3, l1.index(3, l1.index(3) + 1) + 1))

l1 = list(set(l1))
print(f"l1 :{l1}")

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")
l2 = l1                 # shallow copy - data and address is shared

print(l1 is l2)
print(l1 == l2)
print(f"l2 before :{l2}")

l2.extend([6, 7, 8, 9])
print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 40)
l3 = [6, 7, 8, 9, 10]
print(f"l3 before :{l3}")
l4 = l3.copy()
print(f"l4 before :{l4}")

print(l3 is l4)             # compares the address
print(l3 == l4)             # compares the values
l4.append(11)
l4.append(12)
l4.append(13)

print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 40)

l5 = [1, 2, 3, [11, 22, 33, 44, 55], 4, 5]
print(f"l5 before :{l5}")

l6 = l5.copy()
print(f"l6 before :{l6}")

l5[3].extend([66, 77, 88])
print(f"l5 after :{l5}")
print(f"l6 after :{l6}")

print("=" * 40)
l7 = [11, 22, 33, [1, 2, 3, 4, 5], 44, 55]
print(f"l7 before :{l7}")
from copy import deepcopy
l8 = deepcopy(l7)
print(f"l8 before :{l8}")

l8[3].insert(1, 1.5)
l8[3].insert(3, 2.5)
l8[3].insert(5, 3.5)

print(f"l8 after :{l8}")
print(f"l7 after :{l7}")