import tkinter
from tkinter import *

def show():
    search_name = l.get(ACTIVE)
    print(search_name)
    print(dict[search_name])
    name_var.set(search_name)
    number_var.set(str(dict[search_name]))
def add():
    dict[str(entry1.get())]=str(entry2.get())
    l.insert(END,entry1.get())
    print(dict)

dict={}
name=["Poonam","Nikhil","Nick","Punno","Avleen","Priyank","Avu","Kiyara"]
number=[5248,4852,4258,8524,4528,8254,8452,2548,]
for i in range(len(name)):
    dict[name[i]]=number[i]

name_list=list(dict.keys())

root=Tk()
root.geometry('500x150')
root.resizable(FALSE,FALSE)
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)

l=Listbox(root,yscrollcommand=s.set)
for name in name_list:
    l.insert(END,name)
l.pack(side=LEFT,fill=BOTH)

s.config(command=l.yview)

name_var=StringVar()
name_var.set("name")
name_label=Label(root,width=40,textvariable=name_var)
name_label.pack()

number_var=StringVar()
number_var.set("number")
number_lable=Label(root,width=40,textvariable=number_var)
number_lable.pack()

button=Button(text="Get Number",width=20,bg='lightpink',fg='black',command=show)
button.pack()

entry1=Entry(root,width=30)
entry1.pack()
entry2=Entry(root,width=30)
entry2.pack()
button2=Button(root,width=20,bg='lightgreen',fg='black',text="add entry",command=add)
button2.pack()

root.mainloop()