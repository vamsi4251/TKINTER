from tkinter import *
root=Tk()
'''
clicked=StringVar()
drop=OptionMenu(root,clicked,"monday","tuesday","wednesday","thursday","friday","saturday","sunday").pack()
'''
option=[
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]
clicked=StringVar()
clicked.set(option[0])

drop=OptionMenu(root,clicked,*option).pack()







root.mainloop()
