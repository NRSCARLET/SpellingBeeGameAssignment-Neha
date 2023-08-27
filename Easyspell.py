import sys 
from tkinter import *
import tkinter as tk
from tkinter import simpledialog

class CorrectButton(button):
    def __init__(self):
        correct = tk.Button()
        
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
    inc1 = tk.Button(text="Test2")
    inc1.grid(row=2, column=4)
    inc2 = tk.Button(text="Test3")
    inc2.grid(row=3, column=5)
    
ez = Tk()
ez.geometry('200x200')
ez.configure(bg = '#6693F5')
ez.title("Spelling Bee's Spelling Game!")
e = tk.Label(text="You've picked easy mode")
e.grid(row=1, column=3)
conbutton = tk.Button(text="Continue", command = easygame)
conbutton.grid(row=2, column=3)
backb1 = tk.Button(text="Back", command = difficultywindow)
backb1.grid(row=3, column=3)
menub4 = tk.Button(text="Menu", command = menu)
menub4.grid(row=4, column=3)