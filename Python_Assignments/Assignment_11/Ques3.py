'''Ques 3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of
multiple of 2 sec between each display. Delay goes like 2sec-4sec-6sec-8sec-10sec.'''


import threading
from threading import Thread
import time

def display(l):
    n=2
    for x in l:
        print(x)
        time.sleep(n)
        n+=2

l=[10,20,30,40]
t=Thread(target=display,args=(l,))
t.start()