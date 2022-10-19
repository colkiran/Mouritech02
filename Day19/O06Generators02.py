
def fun():
    x = 1
    print("Apples from Ooty......")
    yield x
    x += 9
    print("Oranges from Kanpur.......")
    yield x
    x += 10
    print("Grapes from hubli...........")
    yield x

res = fun()
print(f"res :{res}")

print("-" * 40)
print(res.__next__())

print("-" * 40)
print(res.__next__())

print("-" * 40)
print(res.__next__())

# print("-" * 40)
# print(res.__next__())

def fun():
    for i in range(1, 11):
        yield i

print("-" * 40)
gObj = fun()
print(gObj.__next__())

print(gObj.__next__())

print(gObj.__next__())

print("-" * 40)

for x in fun():
    print(x, end=" ")
print()
