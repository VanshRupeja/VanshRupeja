
import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import messagebox
m=Tk()

m.title(" Main Page ")

frame=tk.Frame(m)
#m.geometry("400x400")

wel=tk.Label(frame,text="Welcome to Main Page",font=("Berlin Sans FB",15))
s=tk.Label(frame,text="SBI BANK",font=("Algerian",14))

def dep():
    import addamount.py
def r():
    import login.py

def wid():
    import withdraw.py
    
def balan():
    import checkbalance.py


def close():
    m.destroy()
    
rButton=tk.Button(frame,text=" Deposit Cash ",width="50",height="2",bg="cyan",command=lambda:dep())
lButton=tk.Button(frame,text=" Withdraw Cash", width="50", height="2",bg="sky blue",command=lambda:wid())
balButton=tk.Button(frame,text=" Balance", width="50", height="2",bg="snow",command=lambda:[balan()])
returnlogin=tk.Button(frame,text="Return to Login", width="50", height="2",bg="yellow",command=lambda:r())

cl=tk.Button(frame,text=" Close ",command=lambda:close())

rButton.grid(row=10,column=2,padx=10,pady=10)
lButton.grid(row=10,column=5,padx=10,pady=10)
balButton.grid(row=20,column=2,padx=10,pady=10)
returnlogin.grid(row=20,column=5,padx=10,pady=10)
wel.grid(row=0,column=3,padx=10,pady=10)
s.grid(row=1,column=3,padx=10,pady=10)
cl.grid(row=40,column=0)
frame.grid(row=0,column=0)

m.mainloop()
