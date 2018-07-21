'''Ques 1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and
create a scrollbar to scroll the list of keys in the dictionary.'''

import tkinter
from tkinter import *

def show():
    search_name = l.get(ACTIVE)
    print(search_name)
    print(dict[search_name])
    name_var.set(search_name)
    number_var.set(str(dict[search_name]))

dict={}
name=["Nikhil","Poonam","Avleen","Priyank","Akhil","Chiku","Duggu"]
number=[6316048,6316052,6316082,6316054,6316042,6316025,6316028]
for i in range(len(name)):
    dict[name[i]]=number[i]

name_list=list(dict.keys())

root=Tk()
root.geometry('550x200')
root.resizable(FALSE,FALSE)
s=Scrollbar(root)
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)

l=Listbox(root,yscrollcommand=s.set)
for name in name_list:
    l.insert(END,name)
l.pack(side=LEFT,fill=BOTH)

s.config(command=l.yview)

name_var=StringVar()
name_var.set("Name")
name_label=Label(root,width=40,textvariable=name_var)
name_label.pack()

number_var=StringVar()
number_var.set("Number")
number_lable=Label(root,width=40,textvariable=number_var)
number_lable.pack()

button=Button(text="Get Number",width=20,bg='lightpink',fg='black',command=show)
button.pack()

root.mainloop()