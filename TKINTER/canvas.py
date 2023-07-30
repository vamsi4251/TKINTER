from tkinter import *
root=Tk()

my_canvas=Canvas(root,width=300,height=200,bg="white")
my_canvas.pack(padx=10,pady=20)

#draw lines
#my_canvas.create_line(x1,y1,x2,y2,fill="color")

my_canvas.create_line(0,100,300,100,fill="red")
my_canvas.create_line(150,0,150,200,fill="red")
my_canvas.create_rectangle(50,150,250,50,fill="red")
my_canvas.create_oval(50,150,250,50,fill="yellow")







root.mainloop()
