
#Ques 4. Call factorial function using thread.




import threading
from threading import Thread
import time
import math

def factorial(n):
    fact=1
    for x in range(1,n+1):
        fact=fact*x
    print("Factorial of Number is : ",fact)

n=int(input("Enter any number :"))
t=Thread(target=factorial,args=(n,))
t.start()
