#Ques 4. From a list containing ints, strings and floats, make three lists to store them separately.


		   
		   
l1=[1,2,3,'a','b','c',1.1,2.2,3.3]
lI = []
lS = []
lT = []

print(isinstance(l1[0],int))

for x in l1:
    if type(x) == int:
        lI.append(x)
    elif type(x) == str:
        lS.append(x)
    elif type(x) == float:
        lT.append(x)
    else:
        print("Value is not int,str or float ")
print(lI,lS,lT,sep="\n")