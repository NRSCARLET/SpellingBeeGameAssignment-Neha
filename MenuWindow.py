from tkinter import *
import tkinter as tk
from os import system, name
from time import sleep
window = tk.Tk()
window.configure (bg = '#6693F5')
window.title("Spelling Bee's Spelling Game!")
window.geometry("400x150")
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
    goodbye = tk.Label(text="Thank you for playing!").grid()
    
hello = tk.Label(text="Welcome to Spelling Bee's Spelling Game!", fg = 'white', bg = '#6693F5', font = 'helvetica 12 bold')
hello.grid(row=0, column=0, padx=5, pady=5)
b1 = tk.Button(text="Register (new user)", fg = 'white', bg = '#DA70D6', font = 'helvetica 9 bold', command=register)
b1.grid(row=2, column=0, padx=3, pady=3)
b2 = tk.Button(text="Login (old user)", fg = 'white', bg = '#DA70D6', font = 'helvetica 9 bold', command=login)
b2.grid(row=3, column=0, padx=3, pady=3)
b3 = tk.Button(text="Exit Game", fg = 'white', bg = '#DA70D6', font = 'helvetica 9 bold', command=exit)
b3.grid(row=4, column=0, padx=3, pady=3)
tk.mainloop()