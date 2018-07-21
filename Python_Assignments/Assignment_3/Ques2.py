#Ques 2. Add the following list to above created list which is in ques1. 
#          ["Google","Apple","Facebook","Microsoft","Tesla"]   


l=[]

num1= int(input("Enter first number= "))
num2= int(input("Enter second number= "))
num3= int(input("Enter third  number= "))
print(l.append(num1))
print(l.append(num2))
print(l.append(num3))
print("List created: then    l = ",l)




l1=["Google","Apple","Facebook","Microsoft","Tesla"]
print(l.extend(l1))
print("After added both lists :  Then     l= ",l)