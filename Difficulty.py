import sys 
from tkinter import *
import tkinter as tk
from tkinter import simpledialog

def Easymode():
    diff.destroy()
    import Easyspell
    Easyspell

def Medmode():
    diff.destroy()
    import Medspell
    Medspell

def Hardmode():
    diff.destroy()
    import Hardspell
    Hardspell

diff = Tk()
diff.geometry("200x130")
diff.configure (bg = '#6693F5')
diff.title("Spelling Bee's Spelling Game!")
dif = tk.Label(text="Choose a difficulty")
dif.grid()

easybut = tk.Button(text="Easy", command = Easymode)
easybut.grid()
medbut = tk.Button(text="Medium", command = Medmode)
medbut.grid()
hardbut = tk.Button(text="Hard", command = Hardmode)
hardbut.grid()