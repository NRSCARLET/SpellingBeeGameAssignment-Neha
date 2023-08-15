import sys 
from tkinter import *
import tkinter as tk
from tkinter import simpledialog

def difficultywindow():
    ez.destroy()
    import Difficulty
    Difficulty

def menu():
    ez.destroy()
    import MenuWindow
    MenuWindow

def easygame():
    print("wow")
ez = Tk()
ez.geometry('200x200')
ez.configure(bg = '#6693F5')
ez.title("Spelling Bee's Spelling Game!")
e = tk.Label(text="You've picked easy mode")
e.pack()

conbutton = tk.Button(text="Continue", command = easygame)
conbutton.pack()
backb1 = tk.Button(text="Back", command = difficultywindow)
backb1.pack()
menub4 = tk.Button(text="Menu", command = menu)
menub4.pack()