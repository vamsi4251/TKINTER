from tkinter import *
root=Tk()
def myClick():
    label=Label(root,text="i clicked the button")
    label.pack()
    

mybutton=Button(root,text="click me",command=myClick()).pack()
mybutton1=Button(root,text="click me",state=DISABLED).pack()

mybutton1=Button(root,text="click me",padx=50,pady=10,command=myClick).pack()
mybutton1=Button(root,text="click me",fg="red",bg="yellow").pack()




root.mainloop()
