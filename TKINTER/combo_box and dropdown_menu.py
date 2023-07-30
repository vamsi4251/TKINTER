from tkinter import *
from tkinter import ttk


root=Tk()
def select(event):
    mylab=Label(root,text=click.get())
    mylab.pack()

def combo1(event):
     mylab=Label(root,text=mycombo.get()).pack()
option=[
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday"


    ]
click=StringVar()
click.set(option[0])
drop=OptionMenu(root,click,*option,command=select)
drop.pack()


mycombo=ttk.Combobox(root,value=option)
mycombo.current(0)
mycombo.bind("<<ComboboxSelected>>",combo1)
mycombo.pack()
#mybut=Button(root,text="selected",command=select).pack()


root.mainloop()
