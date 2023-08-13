import sys 
from tkinter import *
import tkinter as tk
from tkinter import simpledialog

def Easymode():
    diff.destroy()
    import easyspell
    easyspell

def Medmode():
    diff.destroy()
    import medspell
    medspell

def Hardmode():
    diff.destroy()
    import hardspell
    hardspell

diff = Tk()
diff.geometry("200x130")
diff.configure (bg = '#6693F5')
diff.title("Spelling Bee's Spelling Game!")
dif = tk.Label(text="Choose a difficulty")
dif.pack()

easybut = tk.Button(text="Easy", command = Easymode)
easybut.pack()
medbut = tk.Button(text="Medium", command = Medmode)
medbut.pack()
hardbut = tk.Button(text="Hard", command = Hardmode)
hardbut.pack()