from tkinter import *
import tkinter as tk
from os import system, name
from time import sleep
from UserRegandLog import Labels, Buttons
from PIL import Image, ImageTk
window = tk.Tk()
window.configure (bg = '#6693F5')
window.title("Spelling Bee's Spelling Game!")
window.geometry("360x300")
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
    window.destroy()
    import EndScreen
    EndScreen.endgame()
    
hello = Labels(text="Welcome to Spelling Bee's Spelling Game!")
hello.grid(row=0, column=0, padx=5, pady=5)
b1 = Buttons(text="Register (new user)", command=register)
b1.grid(row=2, column=0, padx=3, pady=3)
b2 = Buttons(text="Login (old user)", command=login)
b2.grid(row=3, column=0, padx=3, pady=3)
b3 = Buttons(text="Exit Game", command=exit)
b3.grid(row=4, column=0, padx=3, pady=3)
tk.mainloop()
#got this image code from a tkinter test replit
"""image = Image.open("beeidlegif.gif")
photo = ImageTk.PhotoImage(image)
label = Label(window, image=photo)
label.grid(row=5, column=0, padx=3, pady=3)""" #FIX!!!