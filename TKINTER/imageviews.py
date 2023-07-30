from tkinter import *
from PIL import ImageTk,Image
root=Tk()

img1=ImageTk.PhotoImage(Image.open("C:/Users/91897/Desktop/TKINTER/images/1.jpg"))
img2=ImageTk.PhotoImage(Image.open("C:/Users/91897/Desktop/TKINTER/images/2.jpg"))
img3=ImageTk.PhotoImage(Image.open("C:/Users/91897/Desktop/TKINTER/images/3.jpg"))

img_list=[img1,img2,img3]

lab=Label(image=img1)
lab.grid(row=0,column=0,columnspan=3)

def forward():
    return

def backword():
    return

button_back=Button(root,text="<<",command=backward)
button_front=Button(root,text=">>",command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_front.grid(row=1,column=2)
root.mainloop()
