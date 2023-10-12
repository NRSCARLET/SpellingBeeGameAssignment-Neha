from tkinter import *
import tkinter as tk
from os import system, name
from time import sleep
from UserRegandLog import Labels, Buttons
from PIL import Image, ImageTk
from tkinter import Label, Tk


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


def animate():
    photo = frames[frame_num]
    label.configure(image=photo)
    label.image = photo  # This line is crucial to prevent garbage collection
    window.after(100, update_frame, (frame_num + 1) % len(frames))


def menu_wind():
    global window
    window = tk.Tk()
    window.configure (bg = '#6693F5')
    window.title("Spelling Bee's Spelling Game!")
    window.geometry("360x300")
    hello = Labels(text="Welcome to Spelling Bee's Spelling Game!")
    hello.grid(row=0, column=0, padx=5, pady=5)
    b1 = Buttons(text="Register (new user)", command=register)
    b1.grid(row=2, column=0, padx=3, pady=3)
    b2 = Buttons(text="Login (old user)", command=login)
    b2.grid(row=3, column=0, padx=3, pady=3)
    b3 = Buttons(text="Exit Game", command=exit)
    b3.grid(row=4, column=0, padx=3, pady=3)
    #got this image code from my tkinter test replit
    gif_file = "beeidlegif.gif"
    gif = Image.open(gif_file)
    frames = [ImageTk.Photoimage(img) for img  in gif]
    resize_gif = image.resize((200, 200))
    label = Label(window)
    label.grid(row=5, column=0, padx=3, pady=3) 
    tk.mainloop()
menu_wind()