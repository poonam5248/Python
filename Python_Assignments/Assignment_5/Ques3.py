#Ques 3. Take the input age of 3 people and determine oldest and youngest among them.
print("\n")
Person1=int(input("Enter the age of Ist person= "))
Person2=int(input("Enter the age of 2nd person= "))
Person3=int(input("Enter the age of 3rd person= "))
print("\n")
print("Age of Ist Person is= ",Person1)
print("Age of 2nd Person is= ",Person2)
print("Age of 3rd Person is= ",Person3)
print("\n")

if Person1>Person2 and Person1>Person3:
 print("Ist person is Oldest ")
elif Person2>Person1 and Person2>Person3:
 print("2nd Person is Oldest ")
elif Person1==Person2==Person3:
 print("All Person are of Same age") 
else  :
 print("3rd Person is oldest")
 