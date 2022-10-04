
glbX = 100

def fun(a):
    global glbX
    print(f"a :{a}")            # local variables
    b = "hello world"
    print(f"b :{b}")            # local variables
    glbX = 500
    print(f"inside {glbX}")


print(f"before :{glbX}")

fun(25)

print(f"after :{glbX}")

