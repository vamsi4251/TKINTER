from tkinter import *
from tkinter import messagebox

root=Tk()
'''
def popup():
    messagebox.showinfo("popup","hello")
def popup():
    messagebox.showwarning("popup","hello")

def popup():
    messagebox.showerror("popup","hello")

def popup():
    messagebox.askquestion("popup","hello")

def popup():
    messagebox.askokcancel("popup","hello")
'''
def popup():
    r=messagebox.askyesno("popup","hello")
    Label(root,text=r).pack()
    

Button(root,text="click me",command=popup).pack()








root.mainloop()
