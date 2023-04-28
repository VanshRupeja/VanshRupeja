import tkinter as tk
from tkinter import *

m=Tk()
m.geometry("400x275")
m.title("Home Page")

frame=tk.Frame(m,bg="snow")

home=tk.Label(frame,text=" Home Page ",bg="snow",font=("bold",20))

heading=tk.Label(frame,text=" SBI BANK",bg="cyan",font=("bold",40))

def open():
    import registertkinter.py

def lo():
    import login.py


rButton=tk.Button(frame,text=" Register ",width="50",height="2",bg="cyan",command=lambda:open())
lButton=tk.Button(frame,text=" Login ", width="50", height="2",bg="sky blue",command=lambda:lo())

#positing

heading.grid(row=0, column=400)
home.grid(row=20, column=400)

rButton.grid(row=700,column=400,padx=30,pady=10)
lButton.grid(row=370,column=400,padx=30,pady=10)


frame.grid(row=100,column=100,)

m.mainloop()
