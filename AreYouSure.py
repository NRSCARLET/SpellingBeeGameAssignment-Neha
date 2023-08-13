from tkinter import *
from UserReg import *
import tkinter as tk
import sys

def difficultystage():
    rusure.destroy()
    import Difficulty
    Difficulty

def menu():
    rusure.destroy()
    import MenuWindow
    MenuWindow
    
def register():
    import UserReg
    UserReg
    
rusure = Tk()
rusure.geometry('200x200')
rusure.configure (bg = '#6693F5')
rusure.title("Spelling Bee's Seplling Game")
check = tk.Label(rusure, text=f"Are you sure you want {user} as your username?")
check.pack()
yesb1 = tk.Button(text="Yes", command = difficultystage)
yesb1.pack()
nob1 = tk.Button(text="No", command = register)
nob1.pack()
backb3 = tk.Button(text="Menu")
backb3.pack()


