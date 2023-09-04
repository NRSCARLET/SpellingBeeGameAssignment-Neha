import sys 
from tkinter import *
import tkinter as tk
import random
"""easy_spell_word_hint = ["btut", "bzzu", "ogod", "tars", "labl", "alfl", "chea", "anme", "ctih", "rogw", "etre", "mila", "wrad", "leyl", "meit", "sahd", "chsa", "eadd", "nabg", "urde", "siks", "ribd", "avse", "orpe", "uleg", "uphs", "ulpl", "stre", "yter", "ewts", "stea", "ongs", "sevt", "kics", "eken", "ttse", "darh", "ysea", "rohn"]"""

easy_spell_words={
"tebn":"bent","bzzu":"buzz","ogod":"good","tars":"star","labl":"ball","alfl":"fall","chea":"ache","anme":"name",
"ctih":"itch","rogw":"grow","etre":"tree","sneo":"nose",      "mila":"mail","wrad":"draw","leyl":"yell","meit":"time",      "sahd":"dash","chsa":"cash","eadd":"dead","nabg":"bang",      "urde":"rude","siks":"kiss","ribd":"bird","avse":"vase",      "orpe":"rope","uleg":"glue","uphs":"push","ulpl":"pull",      "stre":"rest","yter":"tyre","ewts":"west","stea":"east",      "ongs":"song","sevt":"vest","kics":"sick","eken":"knee",
"ttse":"test","darh":"hard","ysea":"easy","rohn":"horn"}

used_hints = []
jumbled_word = ""
correct_answer = ""
#words for hints (in order): butt, buzz, good, star, ball, fall, ache, name, itch, grow, tree, nose, mail, draw, yell, time, dash, cash, dead, bang, rude, kiss, bird, vase, rope, glue, push, pull, rest, tyre, west, east, song, vest, sick, knee, test, hard, easy, horn - 40 words (unjumbled words)
class EasyButtons(Button):
    def __init__(self,*args, **kwargs):
        Button.__init__(self,*args, **kwargs)
        self['bg'] = '#DA70D6'
        self['fg'] = 'white'
        self['font'] = 'helvetica 9 bold'

class EasyLabels(Label):
    def __init__ (self, *args, **kwargs):
        Label.__init__(self, **kwargs)
        self['bg'] = '#6693F5'
        self['fg'] = 'purple'
        self['font'] = 'helvetica 10 bold'
        
"""def change_label():
    question_count = 0
    while question_count < 10:
        if easy_spell_words:
            choose_word = random.choice(list(easy_spell_words.keys()))
            used_hints.append(choose_word)
            print(choose_word)
            question_count +1
            if choose_word in used_hints:
                print("REPEAT")
                
            else:
                change_label()
        if question_count == 10:
            quit()"""
def checkanswer():
    user_answer = AnswerEntry.get().lower()
    if AnswerEntry == correct_answer:
        correctlabel.config(text="Correct! Good job!")
    else:
        incorrectlabel.config(text="Incorrect")

    
def easygame():
    def actualgame():
        global AnswerEntry
        global correct_answer
        global jumbled_word
        key = random.choice(list(easy_spell_words))
        """jumblelabel.config(text=f"Write the correct word!: {key}")"""
        """jumbled_word = easy_spell_words[key]
        correct_answer = jumbled_word
        AnswerEntry = tk.Entry(ez, bd =5)
        AnswerEntry.grid(row=2, column=0, padx=5, pady=5)"""
        enterbutton = EasyButtons(text="Enter!", command=checkanswer)
        enterbutton.grid(row=4, column=0, padx=3, pady=3)
    actualgame()
    wordbutton.config(text="Print (new) word!", command=next_word)

def next_word():
    global current_word, scrambled_word, correct_word
    scrambled_word = actualgame(easy_spell_words)
    current_word = easy_spell_words[scrambled_word]
    correct_word = current_word
    label.config(text=scrambled_word)
    entry.delete(0, tk.END)

def difficultywindow():
    ez.destroy()
    import Difficulty
    Difficulty

def menu():
    ez.destroy()
    import MenuWindow
    MenuWindow

def easygamestart():
    global wordbutton
    Gamestartlabel.config(text="Unscramble the words and pick the correct spelling!")
    Gamestartlabel.grid(row=0, column=0, padx=5, pady=5)
    
    wordbutton = EasyButtons(text="Okay!", command = easygame)
    wordbutton.grid(row=3, column=0, padx=3, pady=3)
    
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
e = EasyLabels(text="You've picked easy mode")
e.grid(row=0, column=0, padx=5, pady=5)

conbutton = EasyButtons(text="Continue", command = easygamestart)
conbutton.grid(row=2, column=0, padx=3, pady=3)

backb1 = EasyButtons(text="Back", command = difficultywindow)
backb1.grid(row=3, column=0, padx=3, pady=3)

menub4 = EasyButtons(text="Menu", command = menu)
menub4.grid(row=4, column=0, padx=3, pady=3)

Gamestartlabel = EasyLabels(ez, text="")
Gamestartlabel.grid(row=1, column=0, padx=5, pady=5)

jumblelabel = EasyLabels(ez, text="")
jumblelabel.grid(row=1, column=0, padx=5, pady=5)

correctlabel = EasyLabels(ez, text="")
correctlabel.grid(row=5, column=0, padx=5, pady=5)

incorrectlabel = EasyLabels(ez, text="")
incorrectlabel.grid(row=5, column=0, padx=5, pady=5)

"""label_answer_test = EasyLabels(ez, text="")
label_answer_test.grid(row=1, column=0, padx=5, pady=5)"""
