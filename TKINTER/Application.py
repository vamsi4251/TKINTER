
from tkinter import *

window =Tk()
window.geometry("800x500")
window.title("sample")
mylabel=Label(window,text="APPLICATION",font=("bold",20)).grid(row=0,column=3)
name=Label(window,text="NAME : ").grid(row=1,column=0)
name_box=Entry(window,width=30).grid(row=1,column=2)
mailid=Label(window,text="MAILID : ").grid(row=2,column=0)
mailid_box=Entry(window,width=30).grid(row=2,column=2)
gender=Label(window,text="GENDER : ").grid(row=3,column=0)
gendre1=Radiobutton(window,text="male",value=0).grid(row=3,column=2)
gendre2=Radiobutton(window,text="female",value=1).grid(row=4,column=2)
phone=Label(window,text="PHONE : ").grid(row=5,column=0)
phone_box=Entry(window,width=30).grid(row=5,column=2)




window.mainloop()
