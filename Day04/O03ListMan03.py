
print("append".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
l1.append(9)

print(f"l1 :{l1}")
l1.append([10, 11, 12, 13, 14])

print(f"l1 :{l1}")
print(l1[9][1:4])

print("extend".center(40, "-"))
l1 = list(range(2, 11, 2))
print(f"l1 :{l1}")

l1.extend([12, 14, 16, 18])
print(f"l1 :{l1}")

print("insert".center(40, "-"))
l2 = [1, 2, 3, 4, 5]
print(f"l2 :{l2}")
l2.insert(1, 1.5)
l2.insert(3, 2.5)
l2.insert(5, 3.5)
l2.insert(7, 4.5)

print(f"l2 :{l2}")

print("pop".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")
res = l1.pop(4)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop(1)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

print("remove".center(40, "-"))
l1 = [1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 1, 2]

print(F"l1 :{l1}")
l1.remove(3)
l1.remove(3)
l1.remove(3)
# l1.remove(3)

print(F"l1 :{l1}")

print("-" * 40)
l1 = [1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 1, 2]

print(F"l1 :{l1}")

while l1.count(1):
    l1.remove(1)

# while True:
#     try:
#         l1.remove(1)
#     except ValueError:
#         break

print(l1)
