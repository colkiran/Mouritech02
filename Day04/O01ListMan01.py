
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print('-' * 40)
l2 = [1, 2, 3, 4, 5.2, 6.4, 7.1, 'eight', 'nine', 'ten', True, False, 14+2j, 15-3j]
print(f"l2 :{l2}")
print(type(l2))

print('-' * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

# read the values in the list
print('-' * 40)
l4 = [1, 2, 3, 4, 5.2, 6.4, 7.1, 'eight', 'nine', 'ten', True, False, 14+2j, 15-3j]

print(f"l4[2]  :{l4[2]}")
print(f"l4[7]  :{l4[7]}")
print(f"l4[-1] :{l4[-1]}")

# iterate through the list
for i in l4:
    print(i, end=" ")
print()

for i in range(0, len(l4)):
    print(l4[i], end=" ")
print()

# modify -> update the values, add new elements
print('-' * 40)
print(f"l4 :{l4}")
print(f"l4[5] :{l4[5]}")
l4[5] = 64
l4[9] = l4[9].upper()

l4[8] = 8.5                   # want to insert this value
print(f"l4 :{l4}")

del l4[10]
del l4[4]
print(f"l4 :{l4}")

print('-' * 40)
l4 = [1, 2, 3, 4, 5.2, 6.4, 7.1, 'eight', 'nine', 'ten', True, False, 14+2j, 15-3j]

print(type(l4))
print(f"{l4[0]} :{id(l4[0])}")
print(f"{l4[1]} :{id(l4[1])}")
print(f"{l4[2]} :{id(l4[2])}")
print(f"{l4[3]} :{id(l4[3])}")
print(f"{l4[4]} :{id(l4[4])}")


print('-' * 40)
# unpack a list
values = list(range(10, 40, 10))
print(f"values :{values}")

a, b, c = values
print(f"a :{a}, b :{b} , c :{c}")

print('-' * 40)
values = list(range(10, 101, 10))
print(f"values :{values}")
a, b, *c = values              # *c can accept more than one value
print(f"a :{a}, b :{b} , c :{c}")

print(f"values :{values}")
a, *b, c = values              # *c can accept more than one value
print(f"a :{a}, b :{b} , c :{c}")

print(f"values :{values}")
*a, b, c = values              # *c can accept more than one value
print(f"a :{a}, b :{b} , c :{c}")


# print('-' * 40)
# print(f"values :{values}")
# x = values
# print(x)
print('-' * 40)

lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

lst3 = [lst1, lst2]
print(f"lst3 :{lst3}")
print(len(lst3))

print('-' * 40)
lst4 = [*lst1, *lst2]               # unpack
print(f"lst4 :{lst4}")
print(len(lst4))
