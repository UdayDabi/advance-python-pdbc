from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


s= Shape()



class Rectangle(Shape):
    # yaha area() implement hi nahi kiya
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        rectangle_area = self.length * self.width
        print("Rectangle  area :", rectangle_area)
        return rectangle_area

# object banane ki koshish
r = Rectangle(5, 10)
r.area()