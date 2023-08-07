from tkinter import *
import tkinter as tk

window = tk.Tk()
window.configure (bg = '#6693F5')
window.title("Spelling Bee's Spelling Game!")
window.geometry("400x400")

hello = tk.Label(text="Welcome to Spelling Bee's Spelling Game!", fg = 'white', bg = '#6693F5', font = 'helvetica 11 bold')
hello.pack()
b1 = tk.Button(text="Register (new user)", fg = 'white', bg = '#DA70D6', font = 'helvetica 9 bold')
b1.pack()
b2 = tk.Button(text="Login (old user)", fg = 'white', bg = '#DA70D6', font = 'helvetica 9 bold')
b2.pack()
tk.mainloop()