
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(name):
            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + name)
            print(emojized)

        return innerMostFun
    return innerFun

engGrt = outerFun("Welcome")
engGrtTgr = engGrt("lion")
engGrtTgr("Sheroff")



"""
engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")

engSngArw = engGrt("----->")
engDblArw = engGrt("=====>>")
hndSngArw = hndGrt("----->")
hndDblArw = hndGrt("=====>>")

engSngArw("Sachin")
hndDblArw("Virat")
"""