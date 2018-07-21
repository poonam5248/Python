# Ques 6. Sort the dictionary created in previous question according to marks. 

d={}
x=input("Enter name of Ist Student: ")
y=int(input("Enter marks of Ist Student: "))
d[y]=x
x=input("Enter name of 2nd Student: ")
y=int(input("Enter marks of 2nd Student: "))
d[y]=x
x=input("Enter name of 3rd Student: ")
y=int(input("Enter marks of 3rd Student: "))
d[y]=x
x=input("Enter name of 4th Student: ")
y=int(input("Enter marks of 4th Student: "))
d[y]=x
x=input("Enter name of 5th Student: ")
y=int(input("Enter marks of 5th Student: "))
d[y]=x
x=input("Enter name of 6th Student: ")
y=int(input("Enter marks of 6th Student: "))
d[y]=x
x=input("Enter name of 7th Student: ")
y=int(input("Enter marks of 7th Student: "))
d[y]=x
x=input("Enter name of 8th Student: ")
y=int(input("Enter marks of 8th Student: "))
d[y]=x
x=input("Enter name of 9th Student: ")
y=int(input("Enter marks of 9th Student: "))
d[y]=x
x=input("Enter name of 10th Student: ")
y=int(input("Enter marks of 10th Student: "))
d[y]=x
print("\n")
print(d)
values=list(d.values())
print(values)
values.sort()
print(values)
