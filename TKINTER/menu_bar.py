from tkinter import *
root=Tk()

my_menu=Menu(root)
root.config(menu=my_menu)

#create menu items
def our_command():
    mylab=Label(root,text="you click dropdown").pack()
file_menu=Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New..",command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

#Create an Edit menu

edit_menu=Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=our_command)
edit_menu.add_command(label="Copy",command=root.quit)
#Create options menu
option_menu=Menu(my_menu)
my_menu.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="Find",command=our_command)
option_menu.add_command(label="Fin Next",command=root.quit)



root.mainloop()
