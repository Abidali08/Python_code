from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

master = Tk()
master.title("Master Window")
master.geometry('800x400')


def createwin():
    c = Toplevel()
    c.title("Create")
    c.geometry('400x200')
    cl = Label(c,text="Welcome To Create Window").pack(padx=5,pady=5)
    
def updatewin():
    u = Toplevel()
    u.title("Create")
    u.geometry('400x200')
    ul = Label(u,text="Welcome To Update Window").pack(padx=5,pady=5)

def deletewin():
    d = Toplevel()
    d.title("Create")
    d.geometry('400x200')
    dl = Label(d,text="Welcome To Delete Window").pack(padx=5,pady=5)

Create = Button(
    master,text='Create',width=8,command=createwin
)
Create.grid(row=5,column=4,padx=10,pady=10)

Update = Button(
    master,text='Update',width=8,command=updatewin
)
Update.grid(row=5,column=6,padx=20,pady=10)


Delete = Button(
    master,text='Delete',width=8,command=deletewin
)
Delete.grid(row=5,column=8,padx=30,pady=10)

master.mainloop()