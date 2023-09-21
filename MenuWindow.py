from tkinter import *
import tkinter as tk
from os import system, name
from time import sleep
window = tk.Tk()
window.configure (bg = '#6693F5')
window.title("Spelling Bee's Spelling Game!")
window.geometry("300x300")
def clear():
    """This definition is to add a mechanism to clear the screan."""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def register():
    window.destroy()
    import UserRegandLog
    UserRegandLog.regwindow()
    
def login():
    window.destroy()
    import UserRegandLog
    UserRegandLog.logwindow()
    
def exit():
    b1.destroy()
    b2.destroy()
    b3.destroy()
    hello.destroy()
    goodbye = tk.Label(text="Thank you for playing!").pack()
    
hello = tk.Label(text="Welcome to Spelling Bee's Spelling Game!", fg = 'white', bg = '#6693F5', font = 'helvetica 12 bold')
hello.pack()
b1 = tk.Button(text="Register (new user)", fg = 'white', bg = '#DA70D6', font = 'helvetica 9 bold', command=register)
b1.pack()
b2 = tk.Button(text="Login (old user)", fg = 'white', bg = '#DA70D6', font = 'helvetica 9 bold', command=login)
b2.pack()
b3 = tk.Button(text="Exit Game", fg = 'white', bg = '#DA70D6', font = 'helvetica 9 bold', command=exit)
b3.pack()
tk.mainloop()