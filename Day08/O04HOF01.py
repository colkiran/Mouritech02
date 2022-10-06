
def callMe():
    print("apples from Ooty......")

def fun(fnc):
    print("Hello.....")
    fnc()                           # call back
    print("Hi.......")
    print("-" * 40)

    def defineMe():
        print("Oranged from Kanpur")

    return defineMe

def funCallBack(fnc):
    print("Mera Bharath Mahan.......")
    fnc()
    print("India is Great.......")

funCallBack(fun(callMe))

