'''Ques 3. Create a frame using tkinter with any label text and two buttons.
One to exit and other to change the label to some other text.'''

import tkinter
from tkinter import *

root=Tk()

def show():
    var.set("Hello Python")

def terminate():
    exit(0)

var=StringVar()

root.geometry('400x400')
a=Button(root,width=40,text='Click',command=show)
a.pack()

b=Button(root,width=40,text='Exit',command=terminate)
b.pack()

var.set("Hello World")
label=Label(root,textvar=var,width=20)
label.pack()

root.mainloop()







