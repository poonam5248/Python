#               Sets

# Ques 4. Create two set using user defined values. 

#1. Calculate difference between two sets.
#2. Compare two sets.
#3. Print the result of intersection of two sets.

print("Creation of First Set....")
num1=int(input("Enter Ist Number: "))
num2=int(input("Enter 2nd Number: "))
num3=int(input("Enter 3rd Number: "))
num4=int(input("Enter 4th Number: "))
S1=set([num1,num2,num3,num4])
print("\n")
print("Ist set is : ",S1)

print("\n")
print("Creation of Second set....")
num1=int(input("Enter Ist Number: "))
num2=int(input("Enter 2nd Number: "))
num3=int(input("Enter 3rd Number: "))
num4=int(input("Enter 4th Number: "))
S2=set([num1,num2,num3,num4])
print("\n")
print("2nd set is : ",S2)
print("\n")

 #1.Calculate difference between two sets.

print("Calculation of difference between two sets....")
print("\'Difference of two sets are\': ",S1-S2)

# 2. Compare two sets
print("\n")
print("Comparison of Two sets....")
if S1==S2:
 print("\'Sets are Equal\'")
else:
 print("\'Sets are unequal\'")
 

# 3. Intersection of two sets
print("\n")
print("Intersecting Two sets....  ")
print("\'Intersection of two sets are\': ",S1&S2) 
 