#Ques 4. Write a python program using tkinter interface to take an input in the GUI program and print it.

import tkinter
from tkinter import *

root=Tk()

def show():
    print(entry.get())
def terminate():
    exit(0)

root.geometry('400x400')

entry=Entry(root,width=40)
entry.pack()

a=Button(root,width=30,text='Click',command=show)
a.pack()

b=Button(root,width=30,text='Exit',command=terminate)
b.pack()

root.mainloop()