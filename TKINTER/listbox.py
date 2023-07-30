from tkinter import *
root=Tk()
#Create Frame
my_frame=Frame(root)
my_scrollbar=Scrollbar(my_frame,orient=VERTICAL)

#listbox
#SINGLE,BROWSE,MULTIPLE,EXTENDED
my_listbox=Listbox(my_frame,width=50,yscrollcommand=my_scrollbar.set,selectmode=MULTIPLE)

#config scrollbar
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
my_frame.pack()
my_listbox.pack(pady=15)

#add item to listbox
my_listbox.insert(END,"this is an item")
my_listbox.insert(0,"second item")


#adding list items in listbox

my_list=["one","two","three","four","five","six","seven","eight","nine","ten"]
for i in my_list:
    my_listbox.insert(END,i)
    
#Deleteing item in listbox
def delete():
    my_listbox.delete(ANCHOR)
    my_label.config(text="")
b1=Button(root,text="delete",command=delete).pack()

#Select item in listbox
def select():
    my_label.config(text=my_listbox.get(ANCHOR))
b2=Button(root,text="select",command=select)
b2.pack()
global my_mylabel
my_label=Label(root,text="")
my_label.pack()


root.mainloop()
