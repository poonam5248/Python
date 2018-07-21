# Ques 1. Create a function to calculate the area of a circle by taking radius from user.


r = int(input("Enter the radius of circle: "))


def area():
    a = r * r * 3.14
    print("\nArea of circle is : ",a)

area()