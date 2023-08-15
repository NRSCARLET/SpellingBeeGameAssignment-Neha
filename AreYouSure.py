from tkinter import *
import tkinter as tk
import sys
def difficultystage():
    login.destroy()
    import Difficulty
    Difficulty

def menu():
    login.destroy()
    import MenuWindow
    MenuWindow
    
def register():
    import UserReg
    UserReg
    
rusure = Tk()
rusure.geometry('200x200')
rusure.configure (bg = '#6693F5')
rusure.title("Spelling Bee's Seplling Game")
makesure = tk.Label(rusure, text="Are you sure you want this username?")
makesure.pack()
yesb1 = tk.Button(text="Yes", command = difficultystage)
yesb1.pack()
nob1 = tk.Button(text="No", command = register)
nob1.pack()
menub3 = tk.Button(text="Menu", command = menu)
menub3.pack()


