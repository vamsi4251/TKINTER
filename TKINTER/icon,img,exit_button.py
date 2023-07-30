from tkinter import *
from PIL import ImageTk,Image
root=Tk()
#ADDING ICON
#root.iconbitmap("C:/Users/91897/Desktop/TKINTER/v-image.ico")



#ADDING EXIT BUTTON
button_exit=Button(root,text="EXIT",command=root.quit)
button_exit.pack()

#ADDING IMAGE

img=ImageTk.PhotoImage(Image.open("v.png"))
lab=Label(image=img)
lab.pack()


root.mainloop()
