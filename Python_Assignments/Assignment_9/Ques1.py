'''Ques 1 .Create a circle class and initialize it with radius.
 Make two methods getArea and getCircumference inside this class.'''



class Circle:
    radius=10
    def getArea(self):
        c = 3.14 * self.radius * self.radius
        print("Area of Circle is: ",c)
    def getCircumference(self):
        c = self.radius * 2 * 3.14
        print("Circumference of circle is :",c)


c1=Circle()
c1.getArea()
c1.getCircumference()




