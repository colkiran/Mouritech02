
def doubleMesh(fnc):
    def helper(*args):
        print("=" * 40)
        fnc(*args)
        print("#" * 40)
    return helper


def singleMesh(fnc):
    def helper(*args):
        print("*" * 40)
        fnc(*args)
        print("-" * 40)
    return helper

@singleMesh
@doubleMesh
def fun():
    print(f"Function fun called.....")


fun()
