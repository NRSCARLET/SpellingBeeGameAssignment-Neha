import sys 
from tkinter import *
import tkinter as tk
from tkinter import simpledialog

class EasyButtons(Button):
    def __init__(self,*args, **kwargs):
        Button.__init__(self,*args, **kwargs)
        self['bg'] = '#DA70D6'
        self['fg'] = 'white'
        self['font'] = 'helvetica 9 bold'
        
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
    Q1CB = EasyButtons(ez, text="Correct")
    Q1CB.pack()
    Q1INCB1 = EasyButtons(text="Wrong 1")
    Q1INCB1.pack()
    Q1INCB2 = EasyButtons(text="Wrong 2")
    Q1INCB2.pack()
    
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