'''Ques 1. Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is
inheriting Animal and access the base class method.'''


class Animal:
    def animal_attribute(self):
        print("This is an Animal Class")
class Tiger(Animal):
    def display(self):
        print("This is the Tiger Class")

a=Tiger()
a.animal_attribute()
a.display()














