from tkinter import *

root=Tk()
def something():
    lab1.config(text="new text")
    root.config(bg="yellow")
    b1.config(text="this is configed",state=DISABLED,pady=20)
global lab1
global b1
lab1=Label(root,text="this is a text")
lab1.pack()

b1=Button(root,text="click me",command=something)
b1.pack()









root.mainloop()
