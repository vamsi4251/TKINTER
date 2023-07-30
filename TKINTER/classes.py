from tkinter import *
root=Tk()


class elder:
    def __init__(s,master):
        myFrame=Frame(master)
        myFrame.pack()

        s.but=Button(master,text="click me",command=s.click)
        s.but.pack()
    def click(s):
        print("you click the button")
e=elder(root)





root.mainloop()
