E2 = None
import sys 
from tkinter import *
import tkinter as tk
#global entry widgets
E1 = None
E2 = None
regi = 0
menulogpoint = 0
playing_user = ""


#points system to help with sharing code between different systems
def reset():
    global regi, menulogpoint
    regi = 0
    menulogpoint = 0
    pass

#Classes for changing colours and fonts of buttons and labels.
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


#Code sharing between the login and register sets of code
def regster():
    if regi >= 1:
        reg.destroy()
        import UserRegandLog
        UserRegandLog.regwindow()
    else:
        login.destroy()
        import UserRegandLog
        UserRegandLog.regwindow()

        
def log():
    if regi >=1:
        reg.destroy()
        import UserRegandLog
        UserRegandLog.logwindow()
    else:
        login.destroy()
        import UserRegandLog
        UserRegandLog.logwindow()

        
def menu():
    if menulogpoint == 0:
        reg.destroy()
        import MenuWindow
        MenuWindow.menu_wind()
    else:
        login.destroy()
        import MenuWindow
        MenuWindow.menu_wind()





#---REGISTER CODE--#
def REGEM():
    global regi
    reg.geometry("430x150")
    E2.destroy()
    okb2.destroy()
    menub2.destroy()
    Userregister.destroy()
    regi += 1
    EMM = Labels(reg, text="The username you have entered already exists.\nPlease login with the same username you've entered\nor register again with a different username.")
    EMM.grid(row=0, column=0, padx=5, pady=5)
    logbutton = Buttons(text="Login", command=log)
    logbutton.grid(row=1, column=0, padx=3, pady=5)
    regbutton = Buttons(text="Register", command=regster)
    regbutton.grid(row=2, column=0, padx=3, pady=3)


def empty():
    global regi
    reg.geometry("360x100")
    E2.destroy()
    okb2.destroy()
    menub2.destroy()
    Userregister.destroy()
    regi += 1
    emptyentry = Labels(reg, text="Please input a username into the entry field.")
    emptyentry.grid(row=0, column= 0, padx=5, pady=5)
    okayb = Buttons(text="Okay", command=regster)
    okayb.grid(row=1, column=0, padx=3, pady=3)


def saveuser():
    global playing_user
    checking_preused_name = E2.get()
    if checking_preused_name == "":
        empty()
    else:
        proper_name = checking_preused_name
        with open('username.txt', 'r') as file:
            names = file.read().splitlines()
            if checking_preused_name in names:
                REGEM()
            else:
                playing_user = proper_name
                with open('username.txt', 'a') as useropen:
                    useropen.write(playing_user + "\n")
                reg.destroy()
                import Difficulty
                Difficulty.difficultywindow()


def validate_input(typed_char):
    return typed_char.isalpha() or typed_char == ""


def regwindow():
    global E2, reg, okb2, menub2, Userregister
    reg = Tk()
    reg.geometry("350x150")
    reg.configure (bg = '#6693F5')
    reg.title("Spelling Bee's Spelling Game!")
    validate_cmd = reg.register(validate_input)
    Userregister = Labels(reg, text="Please create a username for your account")
    Userregister.grid(row=0, column=0, padx=5, pady=5)
    E2 = Entry(reg, bd =5, validate="key", validatecommand=(validate_cmd, "%S"))
    E2.grid(row=1, column=0, padx=5, pady=5)
    okb2 = Buttons(text="Enter", command = saveuser)
    okb2.grid(row=2, column=0, padx=3, pady=3)
    menub2 = Buttons(text="Menu", command = menu)
    menub2.grid(row=3, column=0, padx=3, pady=3)
    reg.mainloop()





#---LOGIN CODE---#
def LOGEM():
    login.geometry("480x140")
    Userlogin.destroy()
    E1.destroy()
    okb1.destroy()
    menub1.destroy()
    error = Labels(login, text="The Username you entered was not in our database.\nPlease enter a different username OR register as a user.")
    error.grid(row=0, column=0, padx=5, pady=5)
    Regbutton = Buttons(text="Register", command=regster)
    Regbutton.grid(row=1, column=0, padx=3, pady=3)
    Loginbutton = Buttons(text="Login", command =log)
    Loginbutton.grid(row=2, column=0, padx=3, pady=3)

def check():
    global playing_user
    name_check = E1.get()
    with open('username.txt', 'r') as file:
        names = file.read().splitlines()
        if name_check in names:
            playing_user = name_check
            login.destroy()
            import Difficulty
            Difficulty.difficultywindow()
        else:
            LOGEM()
    

def validate_input(typed_char):
    return typed_char.isalpha() or typed_char == ""
    

def logwindow():
    global E1, login, Userlogin, okb1, menub1, menulogpoint
    menulogpoint +=1
    login = Tk()
    login.geometry("250x150")
    login.configure (bg = '#6693F5')
    login.title("Spelling Bee's Spelling Game!")
    validate_cmd = login.register(validate_input)
    Userlogin = Labels(login, text="Please enter your Username")
    Userlogin.grid(row=0, column= 0, padx= 5, pady=5)
    E1 = tk.Entry(login, bd =5, validate="key", validatecommand=(validate_cmd, "%S"))
    E1.grid(row=1, column=0, padx= 5, pady=5)
    okb1 = Buttons(text="Enter", command = check)
    okb1.grid(row=2, column=0, padx= 3, pady=3)
    menub1 = Buttons(text="Menu", command = menu)
    menub1.grid(row=3, column=0, padx=3, pady=3)
    login.mainloop()
