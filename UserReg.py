import sys 
from tkinter import *
import tkinter as tk
def difficultystage():
    reg.destroy()
    E2.destroy()
    okb2.destroy()
    backb2.destroy()
    Userregister.destroy()
    import Difficulty
    Difficulty

def menu():
    reg.destroy()
    E2.destroy()
    okb2.destroy()
    backb2.destroy()
    Userregister.destroy()
    import MenuWindow
    MenuWindow
reg = Tk()
reg.geometry("330x130")
reg.configure (bg = '#6693F5')
reg.title("Spelling Bee's Spelling Game!")

Userregister = Label(reg, text="Please enter a username for your account").pack()
E2 = Entry(reg, bd =5).pack()
okb2 = tk.Button(text="Enter", command = difficultystage).pack()
backb2 = tk.Button(text="Back", command = menu).pack()
reg.mainloop()