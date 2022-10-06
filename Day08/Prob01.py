
def outerFun(fnc):

    def innerFun(*args):
        fnc(*args)
        print("-" * 40)

    return innerFun

def fun():
    print("Function fun called.....")

def fun1(x):
    print(f"Function fun called.....{x}")

def fun2(x, y):
    print(f"Function fun called.....{x}, {y}")

def fun3(x, y, z):
    print(f"Function fun called.....{x}, {y}, {z}")

def fun4(x, y, z, n):
    print(f"Function fun called.....{x}, {y}, {z}, {n}")

f = outerFun(fun)
f1 = outerFun(fun1)
f2 = outerFun(fun2)
f3 = outerFun(fun3)
f4 = outerFun(fun4)

f()
f1(10)
f2(5, 10)
f3(3, 6, 9)
f4(11, 22, 33, 44)

