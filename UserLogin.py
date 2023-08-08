import sys 
from tkinter import *
import tkinter as tk
from tkinter import simpledialog
#PrintLogger code from Quora
def difficultystage():
    login.destroy()
    E1.destroy()
    okb1.destroy()
    backb2.destroy()
    Userlogin.destroy()
    import Difficulty
    Difficulty

def menu():
    login.destroy()
    E1.destroy()
    okb1.destroy()
    backb2.destroy()
    Userlogin.destroy()
    import MenuWindow
    MenuWindow
login = Tk()
login.geometry("330x130")
login.configure (bg = '#6693F5')
login.title("Spelling Bee's Spelling Game!")
Userlogin = Label(login, text="Please enter your Username")
Userlogin.pack()
E1 = Entry(login, bd =5)
E1.pack()
okb1 = tk.Button(text="Enter", command = difficultystage)
okb1.pack()
backb2 = tk.Button(text="Back", command = menu)
backb2.pack()
login.mainloop()

"""username = simpledialog.askstring("Login", "Please input your Username!")
tk.mainloop()"""