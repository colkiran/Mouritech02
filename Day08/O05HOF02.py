
def bankFlow(fnc):
    print("=" * 40)
    print("Logging into the server......")
    fnc()           # call back
    print("logging out of the server......")
    print("-" * 40)
    

def withdraw():
    print("debited.....")

def deposit():
    print("credited.....")

def gift():
    print("transfered....")

bankFlow(withdraw)
bankFlow(deposit)
bankFlow(gift)

