import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
m=Tk()
m.geometry("500x400")

frame=tk.Frame(m)

m.title(" Check Balance")

heading=tk.Label(frame,text="Check Balance",font=("bold"))
heading.grid(row=0,column=3)

lbalance=tk.Label(frame,fg="green")

lpas=tk.Label(frame,text="Password:")
pas=tk.Entry(frame)

def bal():
    connection= mysql.connector.connect(host='localhost', user='root',password='',port='3306',database='sbi_bank')
    c=connection.cursor()
    password=pas.get()

    balance="select Balance from customerinfo where Password= %s"
    
    c.execute(balance,[(password)])
    result=c.fetchall()
    if result:
        
        messagebox.showinfo("Message","Available Balance in Your Account : %s"%(result))
        
    else:
        messagebox.showerror("Error","Wrong Input")




bButton=tk.Button(frame,text="Check Balance",command=lambda:[bal()])
bButton.grid(row=5, column=3,padx=10,pady=10)


lpas.grid(row=3,column=2,padx=10,pady=10)
pas.grid(row=3,column=8,padx=10,pady=10)

lbalance.grid(row=8,column= 6,padx=10,pady=10)
frame.grid(row=0,column=0)
m.mainloop()
