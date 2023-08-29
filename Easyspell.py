import sys 
from tkinter import *
import tkinter as tk
import random
easy_spell_word_hint = ["btut", "bzzu", "ogod", "tars", "labl", "alfl", "chea", "anme", "ctih", "rogw", "etre", "mila", "wrad", "leyl", "meit", "sahd", "chsa", "eadd", "nabg", "urde", "siks", "ribd", "avse", "orpe", "uleg", "uphs", "ulpl", "stre", "yter", "ewts", "stea", "ongs", "sevt", "kics", "eken", "ttse", "darh", "ysea", "rohn"]
used_hints = []
#words for hints (in order): butt, buzz, good, star, ball, fall, ache, name, itch, grow, tree, nose, mail, draw, yell, time, dash, cash, dead, bang, rude, kiss, bird, vase, rope, glue, push, pull, rest, tyre, west, east, song, vest, sick, knee, test, hard, easy, horn - 40 words (might get rid of some if I can't describe them properly)
class EasyButtons(Button):
    def __init__(self,*args, **kwargs):
        Button.__init__(self,*args, **kwargs)
        self['bg'] = '#DA70D6'
        self['fg'] = 'white'
        self['font'] = 'helvetica 9 bold'

def easygame():
    def change_label():
        if easy_spell_word_hint:
            choose_word = random.choice(easy_spell_word_hint)
            used_hints.append(choose_word)
            easy_spell_word_hint.remove(choose_word)
            label["text"] = choose_word
            if label
def difficultywindow():
    ez.destroy()
    import Difficulty
    Difficulty

def menu():
    ez.destroy()
    import MenuWindow
    MenuWindow

def easygamestart():
    Q1label = tk.Label(text="Unscramble the words and pick the correct spelling!")
    Q1label.pack()
    easyokbutton = tk.Button(text="Okay!", command = easygame)
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
conbutton = tk.Button(text="Continue", command = easygamestart)
conbutton.pack()
backb1 = tk.Button(text="Back", command = difficultywindow)
backb1.pack()
menub4 = tk.Button(text="Menu", command = menu)
menub4.pack()