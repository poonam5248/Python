'''Ques 4. Create a class Shape.Initialize it with length and breadth Create the method Area.
Create class rectangle and square which inherits shape and access the method Area.'''



class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        self.area = self.length * self.breadth


class Rectangle(Shape):
    def area_rectangle(self):
        print("Area of Rectangle is :", self.area)


class Square(Shape):
    def area_square(self):
        print("Area of Square is :", self.area)


length = int(input("Enter the Length:"))
breadth = int(input("Enter the Breadth:"))


a = Rectangle(length,breadth)
b = Square(length,breadth)


if length == breadth:
    b.area()
    b.area_square()
else:
    a.area()
    a.area_rectangle()
