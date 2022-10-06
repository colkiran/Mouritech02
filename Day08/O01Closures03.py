
def outerFun(greet):

    def innerFun(gname):
        print(greet, gname)

    return innerFun

# curry
engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")
tmlGrt = outerFun("Vanakam")

# simple currywa
engGrt("Virat")
hndGrt("Axar")
tmlGrt("Natraj")
