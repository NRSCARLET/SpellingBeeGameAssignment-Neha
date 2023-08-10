from tkinter import *
import tkinter as tk
import sys

def register():
    import UserReg
    UserReg
    
rusure = Tk()
rusure.geometry('200x200')
rusure.configure (bg = '#6693F5')
rusure.title("Spelling Bee's Seplling Game")
check = tk.Label(rusure, "Are you sure you want this username?")
check.pack()
yesb1 = tk.Button(text="Yes", command = difficultystage)
yesb1.pack()
nob1 = tk.Button(text="No", command = register)
nob1.pack()


