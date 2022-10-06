import time


def swap(fnc):

    def helperFun(a, b):
        if  b > a:
            a, b = b, a
        print(f"x :{a}\ty :{b}")
        print(fnc(a, b))
        print("-" * 40)

    return helperFun

@swap
def diff(x, y):
    return x - y

diff(30, 12)
diff(12, 30)

# ----------------------------------------------------------------------------
print("=" * 40)
def timeCalc(fnc):

    def helperFun(n):
        st = time.perf_counter()
        fnc(n)
        et = time.perf_counter()
        print(f"The total time taken by the function {fnc.__name__} to execute is {round(et -st, 2)}")

    return helperFun


@timeCalc
def fun(x):
    l = []
    for i in range(1, x):
        for j in range(1, i + 1):
            l.append(j ** 2)


fun(6000)
