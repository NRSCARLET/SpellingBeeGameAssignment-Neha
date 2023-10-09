import sys 
from tkinter import *
import tkinter as tk
from UserRegandLog import Labels, Buttons

def Easymode():
    diff.destroy()
    import Easyspell
    Easyspell.easywindow()

def Medmode():
    diff.destroy()
    import Medspell
    Medspell.medwindow()

def Hardmode():
    diff.destroy()
    import Hardspell
    Hardspell.hardwindow()

def difficultywindow():
    global diff
    diff = Tk()
    diff.geometry("170x150")
    diff.configure (bg = '#6693F5')
    diff.title("Spelling Bee's Spelling Game!")
    dif = Labels(text="Choose a difficulty")
    dif.grid(row=0, column=0, padx=5, pady=5)
    easybut = Buttons(text="Easy", command = Easymode)
    easybut.grid(row=1, column=0, padx=3, pady=3)
    medbut = Buttons(text="Medium", command = Medmode)
    medbut.grid(row=2, column=0, padx=3, pady=3)
    hardbut = Buttons(text="Hard", command = Hardmode)
    hardbut.grid(row=3, column=0, padx=3, pady=3)