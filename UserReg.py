playing_user = ""
E2 = None
import sys 
from tkinter import *
import tkinter as tk
def saveuser():
    global playing_user
    playing_user = E2.get()
    with open('username.txt', 'a') as useropen:
        useropen.write(playing_user + "\n")
    reg.destroy()
    import Difficulty
    Difficulty

def menu():
    reg.destroy()
    import MenuWindow
    MenuWindow
    
def regwindow():
    global E2, reg
    reg = Tk()
    reg.geometry("330x130")
    reg.configure (bg = '#6693F5')
    reg.title("Spelling Bee's Spelling Game!")
    Userregister = Label(reg, text="Please create a username for your account")
    Userregister.pack()
    E2 = Entry(reg, bd =5)
    E2.pack()
    okb2 = tk.Button(text="Enter", command = saveuser)
    okb2.pack()
    menub2 = tk.Button(text="Menu", command = menu)
    menub2.pack()
    reg.mainloop()