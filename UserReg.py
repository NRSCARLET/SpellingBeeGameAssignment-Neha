import sys 
from tkinter import *
import tkinter as tk
        
def difficultystage():
    Userregister.destroy()
    E2.destroy()
    okb2.destroy()
    backb2.destroy()
    reg.destroy()
    import Difficulty
    Difficulty
    
def sure():
    reg.destroy()
    rusure = Tk()
    rusure.geometry('200x200')
    rusure.configure (bg = '#6693F5')
    rusure.title("Spelling Bee's Seplling Game")
    user = E2.get()
    words = tk.Label(text="Are you sure you want your username to be:")
    words.pack()
    entget = tk.Label(text=user)
    entget.pack()
    yesb1 = tk.Button(text="Yes", command = difficultystage)
    yesb1.pack()
    nob1 = tk.Button(text="No")
    nob1.pack()
    backb3 = tk.Button(text="Menu")
    backb3.pack()
    
    
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
Userregister = Label(reg, text="Please enter a username for your account")
Userregister.pack()
E2 = Entry(reg, bd =5)
E2.pack()
okb2 = tk.Button(text="Enter", command = sure)
okb2.pack()
backb2 = tk.Button(text="Back", command = menu)
backb2.pack()
reg.mainloop()