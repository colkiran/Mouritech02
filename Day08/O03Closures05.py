
def sum(x, y):
    print(f"sum of {x} and {y}")
    return x + y

def diff(x, y):
    print(f"diff of {x} and {y}")
    return x - y

def logdetails(fnc):            # HOF
    loginfo = "Logging into the service......"

    def innerFun(*args):
        print(loginfo)
        print(fnc(*args))               # call back
        print("-" * 40)

    return innerFun

sumlogger = logdetails(sum)
difflogger = logdetails(diff)

sumlogger(35, 45)
difflogger(70, 25)

