from tkinter import *
root=Tk()

e=Entry(root)
e.pack()

#entry1=Entry(root,width=50,bg="yellow").pack()
#entry2=Entry(root,borderwidth=10).pack()

def myClick():
    l1=Label(root,text=e.get())
    l1.pack()
   

mybutton=Button(root,text="click me",command=myClick).pack()





root.mainloop()
