import sys 
from tkinter import *
import tkinter as tk
import UserReg
#PrintLogger code from Quora

def EM():
    Userlogin.destroy()
    E1.destroy()
    okb1.destroy()
    menub1.destroy()
    error = Label(login, text="The Username you entered was not in our database.\nPlease enter a different username OR register as a user.")
    error.pack()
    Regbutton = tk.Button(text="Register")
    Regbutton.pack()
    Loginbutton = tk.Button(text="Login")
    Loginbutton.pack()
    menub3 = tk.Button(text="Menu")
    menub3.pack()

def check():
    name_check = E1.get()
    with open('username.txt', 'r') as file:
        names = file.read().splitlines()
        if name_check in names:
            login.destroy()
            import Difficulty
            Difficulty
        else:
            EM()
    

def menu():
    login.destroy()
    import MenuWindow
    MenuWindow


login = Tk()
login.geometry("330x130")
login.configure (bg = '#6693F5')
login.title("Spelling Bee's Spelling Game!")
Userlogin = Label(login, text="Please enter your Username")
Userlogin.pack()
E1 = tk.Entry(login, bd =5)
E1.pack()
okb1 = tk.Button(text="Enter", command = check)
okb1.pack()
menub1 = tk.Button(text="Menu", command = menu)
menub1.pack()
login.mainloop()
