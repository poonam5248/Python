'''Ques 1. Write a python program using tkinter interface to write Hello World and
a exit button that closes the interface. '''

# import tkinter
# from tkinter import *
#
# root=Tk()
#
# def show():
#     print("Hello World",Tk)
# def terminate():
#     exit(0)
# root.geometry('480x480')
# a=Button(root,width=52,text='Click',command=show)
# a.pack()
#
# b=Button(root,width=52,text='Exit',command=terminate)
# b.pack()
#
# root.mainloop()


import tkinter
from tkinter import *

root=Tk()
label=Label(root)
label.pack()

print("Hello World",Tk)
exit(0)
root.geometry('480x480')
a=Button(root,width=52,text='Click')
a.pack()

b=Button(root,width=52,text='Exit')
b.pack()

root.mainloop()











