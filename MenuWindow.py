from tkinter import *
import tkinter as tk
from os import system, name
from time import sleep
"""window = tk.Tk()"""
def clear():
    """This definition is to add a mechanism to clear the screan."""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def register():
    b1.destroy()
    b2.destroy()
    hello.destroy()
    window.destroy()
    import UserReg
    UserReg
def login():
    b1.destroy()
    b2.destroy()
    hello.destroy()
    window.destroy()
    import UserLogin
    UserLogin
    
def exit():
    b1.destroy()
    b2.destroy()
    b3.destroy()
    hello.destroy()
    goodbye = tk.Label(text="Thank you for playing!").pack()
class Menuscreen(tk):
    def __init__(self):
        tk.__init__(self)
        self.configure (bg = '#6693F5')
        self.title("Spelling Bee's Spelling Game!")
        self.geometry("300x300")
    

hello = tk.Label(text="Welcome to Spelling Bee's Spelling Game!", fg = 'white', bg = '#6693F5', font = 'helvetica 12 bold')
hello.pack()
b1 = tk.Button(text="Register (new user)", fg = 'white', bg = '#DA70D6', font = 'helvetica 9 bold', command=register)
b1.pack()
b2 = tk.Button(text="Login (old user)", fg = 'white', bg = '#DA70D6', font = 'helvetica 9 bold', command=login)
b2.pack()
b3 = tk.Button(text="Exit Game", fg = 'white', bg = '#DA70D6', font = 'helvetica 9 bold', command=exit)
b3.pack()
tk.mainloop()