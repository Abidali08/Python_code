import tkinter as tk
from tkinter import *

a = tk.Tk() #Create window
a.title('First Window')
#this code for button
button = tk.Button(a,text='Stop',width='50',command = a.destroy)
button.pack()

#this code is for Canva
w = Canvas(a,width=40,height=60)
w.pack()
canvas_height=20
canvas_width=2000
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )



a.mainloop() #loop repeat => window


ch = tk.Tk()

m = IntVar()
Checkbutton(ch,text='Male',variable=m).grid(row=0,sticky=W)

f = IntVar()
Checkbutton(ch,text='Female',variable=f).grid(row=1,sticky=W)

o = IntVar()
Checkbutton(ch,text='others',variable=o).grid(row=2,sticky=W)

ch.mainloop()

f = tk.Tk()
frame = Frame(f)
frame.pack()

redbutton = Button(frame, text='Red',fg='red')
redbutton.pack(side = LEFT)

yellowbutton = Button(frame, text='Yellow',fg='yellow')
yellowbutton.pack(side = LEFT)

bluebutton = Button(frame, text='blue',fg='blue')
bluebutton.pack(side = LEFT)

pinkbutton = Button(frame, text='pink',fg='pink')
pinkbutton.pack(side = RIGHT)

f.mainloop()