from tkinter import *
root=Tk()
def click(event):
    mylab=Label(root,text="you click the button")
    mylab.pack()

mybut=Button(root,text="click me")
#bind(event,action)
#Button-1 ------>Left Click
#Button-2 ------>Middle Click
#Button-3 ------>Right Click
#Enter    ------>Mouse Enter
#Leave    ------>Mouse Pointer move outside the button
#FocusIn  ------>
#Return   ------>Entry Button
#Key      ------>Any Key on Keyboard
mybut.bind("<Key>",click)


mybut.pack()





root.mainloop()
