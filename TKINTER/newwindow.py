from tkinter import *
root=Tk()
root.title("first")

def open():
    top=Toplevel()
    top.title("second window")
    lab=Label(top,text="hello").pack()
    btn2=Button(top,text="close",command=top.destroy).pack()

btn=Button(root,text="open second window",command=open).pack()











root.mainloop()
