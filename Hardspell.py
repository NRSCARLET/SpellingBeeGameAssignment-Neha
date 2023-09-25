import sys 
from tkinter import *
import tkinter as tk
import random
from UserRegandLog import playing_user
hard_spell_words_dict={"ytabeu" : "beauty", "bafcir" : "fabric", "shabti" : "habits", "afcdea" : "facade", "kachre" : "hacker", "oachns" : "nachos", "yfacip" : "pacify", "biabtr" : "rabbit", "umacuv" : "vacuum", "ddwlae" : "waddle", "chstay" : "yachts", "gzigde" : "zigged", "baroda" : "abroad", "auslac" : "casual", "eimdum" : "medium", "balces" : "cables", "efaetd" : "defeat", "ibehdn" : "behind", "mereeg" : "emerge", "dibger" : "bridge", "pwrapde" : "wrapped", "balyiti" : "ability", "cpaniat" : "captain", "heantbe" : "beneath", "turceny" : "century", "xniauso" : "anxious", "viddied" : "divided", "conemyo" : "economy", "eadises" : "disease", "awytage" : "gateway", "laehtyh" : "healthy", "leilagl" : "illagal", "tiyjusf" : "justify", "xamiumm" : "maximum", "lqicuky" : "quickly", "siaspve" : "passive", "rmovdee" : "removed", "loevint" : "violent", "tisfasy" : "satisfy", "liyqauf" : "qualify"}

jumbled_word = ""
correct_answer = ""
printed_key = ""
AnswerEntryhard = None
enterbutton = None
wordbutton = None
points = None
userpoints = 0
level = 0
#words for hints (in order): beauty, fabric, habits, facade, hacker, nachos, pacify, rabbit, vacuum, waddle, yachts, zigged, abroad, casual, medium, cables, defeat, behind, emerge, bridge, wrapped, ability, captain, beneath, century, anxious, divided, economy, disease, gateway, healthy, illegal, justify, maximum, quickly, passive, removed, violent, satisfy, qualify.
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
def end():
    hard.destroy()
    import EndScreen
    EndScreen


def checkanswer():
    global userpoints
    user_answer = AnswerEntryhard.get().lower()
    AnswerEntryhard.delete(0, END)
    AnswerEntryhard.config(state = "disabled")
    enterbutton.config(state = "disabled")
    wordbutton.config(state = "active")
    if user_answer == correct_answer:
        answerlabel.config(text=f"CORRECT! The answer is {correct_answer}!")
        userpoints += 1
        points.config(text=f"Points: {userpoints}")
    else:
        answerlabel.config(text=f"INCORRECT! The answer was {correct_answer}!")

    
def actualgame():
    global AnswerEntryhard, printed_key, correct_answer, level, enterbutton, wordbutton, points
    level +=1
    answerlabel.config(text="")
    points.config(text=f"Points: {userpoints}")
    if level <= 10:
        AnswerEntryhard.grid(row=2, column=0, padx=5, pady=5)
        AnswerEntryhard.config(state = "normal")
        printed_key = random.choice(list(hard_spell_words_dict))
        correct_answer = hard_spell_words_dict.pop(printed_key)
        jumblelabel.config(text=f"Write the correct word!: {printed_key}")
        enterbutton.config(text="Enter!", command=checkanswer)
        enterbutton.grid(row=4, column=0, padx=3, pady=3)
        enterbutton.config(state = "active")
        wordbutton.config(text="Print (new) word!", state = "disabled")
    else:
        Gamestartlabel.config(text="Please press the 'End game' button to continue to the end screen")
        AnswerEntryhard.destroy()
        enterbutton.destroy()
        points.destroy()
        with open('hardscore.txt', 'a') as pointopen:
            pointopen.write(f"{playing_user}, {userpoints}" + "\n")
            pointopen.close()
        with open('hardscore.txt', 'r') as pointopen:
            scores = pointopen.read().splitlines()
            for i, score in enumerate(scores):
                name, points = score.split(', ')
                points = int(points)
                if points < 5:
                    jumblelabel.config(text=f"Better luck next time {name}!")
                elif points == 10:
                    jumblelabel.config(text=f"WOAH a perfect score!! Amazing job {name}!")
    
                else:
                    jumblelabel.config(text=f"Great job {name}!")
                pointlabel = Labels(text=f"You scored {points} out of 10!")
                pointlabel.grid(row=2, column=0, padx=5, pady=5)
                wordbutton.config(text="End game!", command = end)
        



def difficultywindow():
    hard.destroy()
    import Difficulty
    Difficulty

        
def menu():
    hard.destroy()
    import MenuWindow
    MenuWindow


def easygamestart():
    global wordbutton
    Gamestartlabel.config(text="Unscramble the words and write the correct spelling!")
    Gamestartlabel.grid(row=0, column=0, padx=5, pady=5)

    wordbutton = Buttons(text="Okay!", command = actualgame)
    wordbutton.grid(row=3, column=0, padx=3, pady=3)
    
    h.destroy()
    conbutton.destroy()
    backb3.destroy()
    menub6.destroy()

    
hard = Tk()
hard.geometry('200x200')
hard.configure(bg = '#6693F5')
hard.title("Spelling Bee's Spelling Game!")
h = Labels(text="You've picked hard mode")
h.grid(row=0, column=0, padx=5, pady=5)

conbutton = Buttons(text="Continue", command = easygamestart)
conbutton.grid(row=2, column=0, padx=3, pady=3)

backb3 = Buttons(text="Back", command = difficultywindow)
backb3.grid(row=3, column=0, padx=3, pady=3)

menub6 = Buttons(text="Menu", command = menu)
menub6.grid(row=4, column=0, padx=3, pady=3)

Gamestartlabel = Labels(hard, text="")
Gamestartlabel.grid(row=1, column=0, padx=5, pady=5)

jumblelabel = Labels(hard, text="")
jumblelabel.grid(row=1, column=0, padx=5, pady=5)

answerlabel = Labels(hard, text="")
answerlabel.grid(row=5, column=0, padx=5, pady=5)

points = Labels(hard, text="")
points.grid(row=0, column=1, padx=5, pady=5)

AnswerEntryhard = tk.Entry(hard, bd =5)
AnswerEntryhard.grid()
AnswerEntryhard.grid_forget()

enterbutton = Buttons(text="")
enterbutton.grid()
enterbutton.grid_forget()
"""label_answer_test = Labels(hard, text="")
label_answer_test.grid(row=1, column=0, padx=5, pady=5)"""
