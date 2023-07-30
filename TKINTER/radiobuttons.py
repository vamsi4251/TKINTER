from tkinter import *


root=Tk()
'''
r=IntVar()
r.set("1")
def clicked(value):
    lab=Label(root,text=value)
    lab.pack()    
Radiobutton(root,text="option 1",variable=r,value=1,command=lambda:clicked(r.get())).pack()
Radiobutton(root,text="option 2",variable=r,value=2,command=lambda:clicked(r.get())).pack()
mylab=Label(root,text=r.get())
mylab.pack()
'''
modes=[
    ("apple","apple"),
    ("banana","banana"),
    ("orange","orange"),
    ("grapes","grapes"),
    ]
fruit=StringVar()
fruit.set("apple")
for text,mode in modes:
    Radiobutton(root,text=text,variable=fruit,value=mode).pack(anchor=W)

root.mainloop()
