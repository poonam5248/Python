'''Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. 
    Iterate over list using for loop.'''
               
			   
			   

x= int(input("Enter the key x:-"))
y=int(input("Enter the key y:-"))
z= int(input("Enter the key z:-"))
l=[x,y,z]
k= int(input("Enter the search key:-"))
for n in range(3):
    if (l[n]==k):
        print("Value found",n)
        del l[n]
        break
print(l)
