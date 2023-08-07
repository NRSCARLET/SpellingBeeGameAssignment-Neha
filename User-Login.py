import sys 
from tkinter import *
import sys 
import tkinter as tk 
#PrintLogger code from Quora
class PrintLogger: 
    def __init__(self, textbox): 
        self.textbox = textbox 
 
    def write(self, text): 
        self.textbox.insert(tk.END, text) 
 
root = tk.Tk() 
 
textbox = tk.Text(root) 
textbox.pack() 
 
printlogger = PrintLogger(textbox) 
sys.stdout = printlogger 
class Userlogin:
    def __init__(self, name, highscore):
        self.name = name
        self.highscore = highscore


hello = tk.Label(text="Welcome to the spelling game!")
hello.pack()

def login():
    print("Please input a username")
    E1 = Entry(root, width = 50)
    E1.pack(side = RIGHT)

.TK
userbutton = tk.Button(text="User Login", 
                   command=login)
userbutton.pack()
 
tk.mainloop()

    