
glbx = "global variable"

def outerFun(gname):
    gst = f"Mr.{gname}"
    print(glbx)


    def innerFun():
        nonlocal gst                # only local variable can become nonlocal
        # nonlocal glbx
        gst = "Mr.Rahul"
        print("Hello World")
        print(gname)
        print(f"Greetings {gst}")

    innerFun()
    print(f"after :{gst}")

outerFun("Sachin")

