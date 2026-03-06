class Shape:
    def area(self):
       return print("Shape Area")


class Rectangle(Shape):

    def area(self):
        return print("Rectangle Area")

r = Rectangle()
r.area()

s = Shape()
s.area()

shape: Shape = Rectangle()
shape.area()
