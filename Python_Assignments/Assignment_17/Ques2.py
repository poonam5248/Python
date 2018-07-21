'''Ques 2. Write a python program to in the same interface as above and create an
action when the button is click it will display some text.'''

import tkinter
from tkinter import *

root=Tk()

def show():
    var.set("Hey....Welcome to Python")

def terminate():
    exit(0)

var=StringVar()

root.geometry('480x480')
a=Button(root,width=60,text='Click',command=show)
a.pack()

b=Button(root,width=60,text='Exit',command=terminate)
b.pack()

label=Label(root,textvar=var,width=50)
label.pack()

root.mainloop()




#
# import tkinter
# from tkinter import *
#
# def show():
#     print('Hey You Are most Welcome!!')
#
# root= Tk()
# root.geometry("250x250")
# a=Button(root,text="click",bg="cyan",fg="black",command=show)
# a.pack()
#
# root.mainloop()