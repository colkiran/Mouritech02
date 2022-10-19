
l = ['a', 'b', 'c', 'd', 'e']
print(f"l :{l}")
print(type(l))
# print(dir(l))


iterObj = l.__iter__()
# print(dir(iterObj))
# __iter__() and __next__() are the protocols of iteration

print("-" * 40)
e1 = iterObj.__next__()
print(f"element1 :{e1}")

print("-" * 40)
e2 = iterObj.__next__()
print(f"element1 :{e2}")

print("-" * 40)
e3 = iterObj.__next__()
print(f"element1 :{e3}")

print("-" * 40)
e4 = iterObj.__next__()
print(f"element1 :{e4}")

print("-" * 40)
e5 = iterObj.__next__()
print(f"element1 :{e5}")

# print("-" * 40)
# e6 = iterObj.__next__()
# print(f"element1 :{e6}")

