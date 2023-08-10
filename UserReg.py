import sys 
from tkinter import *
import tkinter as tk
def difficultystage():
    login.destroy()
    E1.destroy()
    okb1.destroy()
    backb2.destroy()
    Userlogin.destroy()
    import Difficulty
    Difficulty
    
def sure():
    Userregister.destroy()
    E2.destroy()
    okb2.destroy()
    backb2.destroy()
    reg.destroy()
    rusure = Tk()
    rusure.geometry('100x100')
    rusure.configure (bg = '#6693F5')
    rusure.title("Spelling Bee's Seplling Game")
    check = Label("Are you sure you want this username?")
    check.pack()
    yesb1 = tk.Button(text="Yes", command = difficultystage)
    nob1 = tk.Button(text="No", command = )
    
def menu():
    login.destroy()
    E1.destroy()
    okb1.destroy()
    backb2.destroy()
    Userlogin.destroy()
    import MenuWindow
    MenuWindow

reg = Tk()
reg.geometry("330x130")
reg.configure (bg = '#6693F5')
reg.title("Spelling Bee's Spelling Game!")
Userregister = Label(reg, text="Please enter a username for your account").pack()
E2 = Entry(reg, bd =5).pack()
okb2 = tk.Button(text="Enter", command = sure).pack()
backb2 = tk.Button(text="Back", command = menu).pack()
reg.mainloop()


Register()