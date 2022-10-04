
# closures
def outerFun(gname):
    gst = f"Mr.{gname}"

    def innerFun():

        print("Hello world")
        print(f"Greetings {gst}")

    innerFun()


outerFun("Rahul")
