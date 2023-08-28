import sys 
from tkinter import *
import tkinter as tk
from tkinter import simpledialog
easy_spell_word_hint = ["an animals body part", "the sound that bees make", "the opposite of bad", "something thats in space and the ocean", "something you can kick", "the opposite of rise", "when something hurts", "something you have", "something you can scratch", "" ]
#words for hints (in order): butt, buzz, good, star, ball, fall, ache, name, itch, grow, tree, nose, mail, draw, yell, time, dash, cash, dead, bang, rude, kiss, bird, vase, 
class EasyButtons(Button):
    def __init__(self,*args, **kwargs):
        Button.__init__(self,*args, **kwargs)
        self['bg'] = '#DA70D6'
        self['fg'] = 'white'
        self['font'] = 'helvetica 9 bold'
        
def difficultywindow():
    ez.destroy()
    import Difficulty
    Difficulty

def menu():
    ez.destroy()
    import MenuWindow
    MenuWindow

def easygame():
    e.destroy()
    conbutton.destroy()
    backb1.destroy()
    menub4.destroy()
    
    """Q1label = tk.Label(text="Please pick the correct spelling of [insert thing here]")
    Q1label.pack()
    Q1CB = EasyButtons(ez, text="paw")
    Q1CB.pack()
    Q1INCB1 = EasyButtons(text="liw")
    Q1INCB1.pack()
    Q1INCB2 = EasyButtons(text="pey")
    Q1INCB2.pack()"""
    
    
ez = Tk()
ez.geometry('200x200')
ez.configure(bg = '#6693F5')
ez.title("Spelling Bee's Spelling Game!")
e = tk.Label(text="You've picked easy mode")
e.pack()
conbutton = tk.Button(text="Continue", command = easygame)
conbutton.pack()
backb1 = tk.Button(text="Back", command = difficultywindow)
backb1.pack()
menub4 = tk.Button(text="Menu", command = menu)
menub4.pack()