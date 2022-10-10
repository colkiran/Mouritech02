
def foo(i, x=[]):
    x.append(x.append(i))
    return x

for i in range(3):
    y = foo(i)
print(y)
