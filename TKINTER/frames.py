from tkinter import *
from PIL import ImageTk,Image

root=Tk()

frame=LabelFrame(root,padx=50,pady=50)
frame.pack(padx=10,pady=10)

b1=Button(frame,text="clear")
b2=Button(frame,text="submit")

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)



root.mainloop()
