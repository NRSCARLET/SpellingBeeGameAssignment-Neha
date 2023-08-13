import sys 
from tkinter import *
import tkinter as tk
from tkinter import simpledialog


diff = Tk()
diff.geometry("200x130")
diff.configure (bg = '#6693F5')
diff.title("Spelling Bee's Spelling Game!")

dif = tk.Label(text="Choose a difficulty")
dif.pack()

easybut = tk.Button(text="Easy")
easybut.pack()
medbut = tk.Button(text="Medium")
medbut.pack()
hardbut = tk.Button(text="Hard")
hardbut.pack()