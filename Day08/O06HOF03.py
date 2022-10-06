
def bankFlow(fnc):

    def helperFun(*args):
        print("=" * 40)
        print("Logging into the server......")
        fnc(*args)           # call back
        print("logging out of the server......")
        print("-" * 40)

    return helperFun

@bankFlow                   # withdraw = bankFlow(withdraw)
def withdraw(amt):
    print(f"debited {amt}.....")


@bankFlow
def deposit(amt):
    print(f"credited {amt}.....")


@bankFlow
def gift(amt):
    print(f"transfered {amt}....")

deposit(50000)
withdraw(10000)
gift(5000)

