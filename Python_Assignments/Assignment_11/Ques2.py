#Ques 2. Make a thread that prints numbers from 1-10, waits for 1 sec between.



import threading
from threading import Thread
import time

def display():
    for x in range(1,11):
        print(x)
        time.sleep(1)
t=Thread(target=display)
t.start()
