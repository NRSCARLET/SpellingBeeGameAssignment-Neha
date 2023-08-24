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
    e.destroy()
    conbutton.destroy()
    backb1.destroy()
    testb1 = tk.Button(text="Test1")
    testb1.grid(row=1, column=3)
    testb2 = tk.Button(text="Test2")
    testb2.grid(row=2, column=4)
    testb3 = tk.Button(text="Test3")
    testb3.grid(row=3, column=5)
    
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