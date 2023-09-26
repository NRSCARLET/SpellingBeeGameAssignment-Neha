playing_user = ""
E2 = None
import sys 
from tkinter import *
import tkinter as tk

class Buttons(Button):
    def __init__(self,*args, **kwargs):
        Button.__init__(self,*args, **kwargs)
        self['bg'] = '#DA70D6'
        self['fg'] = 'white'
        self['font'] = 'helvetica 9 bold'

class Labels(Label):
    def __init__ (self, *args, **kwargs):
        Label.__init__(self, **kwargs)
        self['bg'] = '#6693F5'
        self['fg'] = 'purple'
        self['font'] = 'helvetica 10 bold'
        
def REGEM():
    regerror = Labels(reg, text="The username you have entered already exists. Please login with the same username or register again with a different username")
    regerror.grid(row=0, column=0, padx=5, pady=5)


def saveuser():
    global playing_user
    checking_preused_name = E2.get()
    with open('username.txt', 'r') as file:
        names = file.read().splitlines()
        if checking_preused_name in names:
            REGEM()
        else:
            with open('username.txt', 'a') as useropen:
                checking_preused_name = playing_user
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
    Userregister = Labels(reg, text="Please create a username for your account")
    Userregister.grid(row=0, column=0, padx=5, pady=5)
    E2 = Entry(reg, bd =5)
    E2.grid(row=1, column=0, padx=5, pady=5)
    okb2 = Buttons(text="Enter", command = saveuser)
    okb2.grid(row=2, column=0, padx=3, pady=3)
    menub2 = Buttons(text="Menu", command = menu)
    menub2.grid(row=3, column=0, padx=3, pady=3)
    reg.mainloop()





#PrintLogger code from Quora
E1 = None
def reg():
    login.destroy()
    import UserRegandLog
    UserRegandLog.regwindow()

def log():
    login.destroy()
    import UserRegandLog
    UserRegandLog.logwindow()
    
def LOGEM():
    Userlogin.destroy()
    E1.destroy()
    okb1.destroy()
    menub1.destroy()
    error = Label(login, text="The Username you entered was not in our database.\nPlease enter a different username OR register as a user.")
    error.grid(row=0, column=0, padx=5, pady=5)
    Regbutton = Buttons(text="Register", command=reg)
    Regbutton.grid(row=1, column=0, padx=3, pady=3)
    Loginbutton = tk.Button(text="Login", command =log)
    Loginbutton.grid(row=2, column=0, padx=3, pady=3)
    menub3 = Buttons(text="Menu", command=menu)
    menub3.grid(row=3, column=0, padx=3, pady=3)

def check():
    global playing_user
    name_check = E1.get()
    with open('username.txt', 'r') as file:
        names = file.read().splitlines()
        if name_check in names:
            playing_user = name_check
            login.destroy()
            import Difficulty
            Difficulty
        else:
            LOGEM()
    

def menu():
    login.destroy()
    import MenuWindow
    MenuWindow

def logwindow():
    global E1, login, Userlogin, okb1, menub1
    login = Tk()
    login.geometry("330x130")
    login.configure (bg = '#6693F5')
    login.title("Spelling Bee's Spelling Game!")
    Userlogin = Labels(login, text="Please enter your Username")
    Userlogin.grid(row=0, column= 0, padx= 5, pady=5)
    E1 = tk.Entry(login, bd =5)
    E1.grid(row=1, column=0, padx= 5, pady=5)
    okb1 = tk.Button(text="Enter", command = check)
    okb1.grid(row=2, column=0, padx= 3, pady=3)
    menub1 = tk.Button(text="Menu", command = menu)
    menub1.grid(row=3, column=0, padx=3, pady=3)
    login.mainloop()
