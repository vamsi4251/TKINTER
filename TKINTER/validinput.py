from tkinter import *
root=Tk()



def number():
    try:
        int(my_box.get())
        ans.config(text="valid")
    except ValueError:
        ans.config(text="invalid")
my_lab=Label(root,text="enter a number").pack()
my_box=Entry(root)
my_box.pack()
my_button=Button(root,text="click me",command=number).pack()
ans=Label(root,text="")
ans.pack()

root.mainloop()
