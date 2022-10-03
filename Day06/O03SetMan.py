
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 40)
s2 = {1, 2, 3, 4, 'five', 'six', 'seven', 'eight', 'nine', 10.5, 11.2, 12.5, 13.1, True, False, 15 + 6j, 19 - 4j}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 40)
s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))

# add, update
print("-" * 40)
s4 = {1, 2, 3}
print(f"s4 :{s4}")

s4.add(1)
s4.add(3)
s4.add(4)
s4.add(5)
s4.add(6)
print(f"s4 :{s4}")

# update
print("-" * 40)
s4.update([1, 2, 4])
s4.update([5, 6, 7])
s4.update([2, 5, 4])
s4.update([7, 8, 9])
print(f"s4 :{s4}")

# pop, remove, discard
print("-" * 40)
print(f"s4 :{s4}")

res = s4.pop()
print(f"res :{res}")

res = s4.pop()
print(f"res :{res}")
print(f"s4 :{s4}")

print("-" * 40)
# remove
s4.remove(8)
s4.remove(4)

# s4.remove(1)
print(f's4 :{s4}')
print("-" * 40)
# discard

s4.discard(5)
s4.discard(1)           # does not throw error
print(f"s4 :{s4}")

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")
print("-" * 40)

print("A union B :", A | B)
print("B union A :", B.union(A))

print("-" * 40)
print("A intersection B :", A & B)
print("B intersection A :", B.intersection(A))

print("-" * 40)
print("A difference B :", A - B)
print("B difference A :", B.difference(A))

print("-" * 40)
print("A symmetric difference B :", A ^ B)
print("B symmetric difference A :", B.symmetric_difference(A))

print("-" * 40)
# frozen set - immutable
f1 = frozenset([1, 2, 3, 4, 5])
print(f"f1 :{f1}")
print(type(f1))
