'''Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
tells them the year that they will turn 100 years old.''' 
 
 
from datetime import datetime 
Name=input("Enter your name : ")
Age=int(input("Enter your age: "))
print("\n")

Hundred= int((100-Age) + datetime.now().year)
print("Hello %s. You are %s years old. You will turn 100 years old in %s\n" % (Name,Age,Hundred))