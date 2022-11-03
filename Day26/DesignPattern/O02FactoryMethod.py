
class Shape(object):
    pass

def factory(type):

    class Circle(Shape):
        def draw(self): print ('Circle.draw')

        def erase(self): print('Circle.erase.....')


    class Square(Shape):
        def draw(self): print("Square.draw")

        def erase(self): print("Square.erase.......")

    class rectangle(Shape):
        def draw(self): print("Rectangle.draw")

        def erase(self): print("Rectang;.erase.......")

    if type == 10:
        return Circle()
    if type == 20:
        return Square()


shape = factory(20)
if (shape != None):
    shape.draw()
    shape.erase()
else:
    print("Wrong type passed")

