import sys 
from tkinter import *
import tkinter as tk
def difficultystage():
    Userregister.destroy()
    E2.destroy()
    okb2.destroy()
    menub2.destroy()
    reg.destroy()
    import Difficulty
    Difficulty
    
def sure():
    reg.destroy()
    import AreYouSure
    AreYouSure
    
    
def menu():
    reg.destroy()
    E2.destroy()
    okb2.destroy()
    menub2.destroy()
    Userregister.destroy()
    import MenuWindow
    MenuWindow

reg = Tk()
reg.geometry("330x130")
reg.configure (bg = '#6693F5')
reg.title("Spelling Bee's Spelling Game!")
Userregister = Label(reg, text="Please enter a username for your account")
Userregister.pack()
E2 = Entry(reg, bd =5)
E2.pack()
okb2 = tk.Button(text="Enter", command = sure)
okb2.pack()
menub2 = tk.Button(text="Menu", command = menu)
menub2.pack()
reg.mainloop()