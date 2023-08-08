from tkinter import *
import tkinter as tk

window = tk.Tk()
window.configure (bg = '#6693F5')
window.title("Spelling Bee's Spelling Game!")
window.geometry("300x300")

def login():
    b1.destroy()
    b2.destroy()
    hello.destroy()
    import UserLogin
    UserLogin
    
hello = tk.Label(text="Welcome to Spelling Bee's Spelling Game!", fg = 'white', bg = '#6693F5', font = 'helvetica 12 bold')
hello.pack()
b1 = tk.Button(text="Register (new user)", fg = 'white', bg = '#DA70D6', font = 'helvetica 9 bold')
b1.pack()
b2 = tk.Button(text="Login (old user)", fg = 'white', bg = '#DA70D6', font = 'helvetica 9 bold', command=login)
b2.pack()
tk.mainloop()