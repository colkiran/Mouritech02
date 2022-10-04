
# closures
def outerFun(gname):
    gst = f"Mr.{gname}"

    def innerFun():

        print("Hello world")
        print(f"Greetings {gst}")

    return innerFun


outerFun("Rahul")
print("-" * 40)

infun = outerFun("Rahul")
print("After executing few lines of code....")

infun()
print("-" * 40)

print(__name__)         # __main__
print(outerFun.__name__)
print(outerFun("virat").__name__)


