# Ques 5.Using range(1,101), make a list containing even and odd numbers.



l1=[]
l2=[]
for n in range(1,101) :
    if n%2 ==0:
        l1.append(n)
    else :
        l2.append(n)
print("even number :-",l1)
print("\n\n")
print("odd number:-",l2)