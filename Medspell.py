import sys 
from tkinter import *
import tkinter as tk
import random

med_spell_words_dict={
"rubnt" : "burnt", "intop" : "point", "tiwre" : "write", "tenea" : "eaten", "euqne" : "queen", "uoqet" : "quote", "pleap" : "apple", "elsfe" : "feels", "ovetd" : "voted", "asthe" : "haste", "bazer" : "zebra", "rufry" : "furry", "zifyz" : "fizzy", "iqkcu" : "quick", "foerf" : "offer", "rwory" : "worry", "wetak" : "tweak", "rpnit" : "print", "psrot", "sport", "aostt", "toast", "dadre" : "dread", "rtate" : "treat", "ayrcz" : "crazy", "uqkac" : "quack", "onsud" : "sound", "veasw" : "waves", "mujps" : "jumps", "padre" : "drape", "eevah" : "heave", "eaocn" : "ocean", "echba" : "beach", "hiwle" : "while", "airot" : "ratio", "yhvea" : "heavy", "vargy" : "gravy", "zidzy" : "dizzy", "ooakz" : "kazoo", "ratos" : "roast", "kalef" : "flake", "sulfh" : "flush"}

jumbled_word = ""
correct_answer = ""
printed_key = ""
AnswerEntry = None
enterbutton = None
wordbutton = None
userpoints = 0
level = 0
#words for hints (in order): burnt, point, write, eaten, queen, quote, apple, feels, voted, haste, zebra, furry, fizzy, quick, offer, worry, tweak, print, sport, toast, dread, treat, crazy, quack, sound, waves, jumps, drape, heave, ocean, beach, while, ratio, heavy, gravy, dizzy, kazoo, roast, flake, flush
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

def checkanswer():
    global userpoints
    user_answer = AnswerEntry.get().lower()
    AnswerEntry.config(state = "disabled")
    enterbutton.config(state = "disabled")
    wordbutton.config(state = "active")
    if user_answer == correct_answer:
        answerlabel.config(text=f"CORRECT! The answer is {correct_answer}!")
        userpoints += 1
        print(userpoints)
    else:
        answerlabel.config(text=f"INCORRECT! The answer was {correct_answer}!")

def actualgame():
    global AnswerEntry, printed_key, correct_answer, level, enterbutton, wordbutton
    level +=1
    answerlabel.config(text="")
    AnswerEntry = tk.Entry(med, bd =5)
    AnswerEntry.grid(row=2, column=0, padx=5, pady=5)
    if level <= 10:
        printed_key = random.choice(list(med_spell_words_dict))
        correct_answer = med_spell_words_dict.pop(printed_key)
        jumblelabel.config(text=f"Write the correct word!: {printed_key}")
        enterbutton = Buttons(text="Enter!", command=checkanswer)
        wordbutton.config(text="Print (new) word!", state = "disabled")
        enterbutton.grid(row=4, column=0, padx=3, pady=3)
    else:
        points_str = str(userpoints)
        with open('mediumscore.txt', 'a') as pointopen:
            pointopen.write(f"{playing_user}, {userpoints}" + "\n")
            pointopen.close()
        with open('mediumscore.txt', 'r') as pointopen:
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
                AnswerEntry.destroy()
        



def difficultywindow():
    med.destroy()
    import Difficulty
    Difficulty

def menu():
    med.destroy()
    import MenuWindow
    MenuWindow

def easygamestart():
    global wordbutton
    Gamestartlabel.config(text="Unscramble the words and pick the correct spelling!")
    Gamestartlabel.grid(row=0, column=0, padx=5, pady=5)

    wordbutton = Buttons(text="Okay!", command = actualgame)
    wordbutton.grid(row=3, column=0, padx=3, pady=3)
    
    e.destroy()
    conbutton.destroy()
    backb1.destroy()
    menub4.destroy()

    
med = Tk()
med.geometry('200x200')
med.configure(bg = '#6693F5')
med.title("Spelling Bee's Spelling Game!")
m = Labels(text="You've picked medium mode")
m.grid(row=0, column=0, padx=5, pady=5)

conbutton = Buttons(text="Continue", command = easygamestart)
conbutton.grid(row=2, column=0, padx=3, pady=3)

backb2 = Buttons(text="Back", command = difficultywindow)
backb2.grid(row=3, column=0, padx=3, pady=3)

menub5 = Buttons(text="Menu", command = menu)
menub5.grid(row=4, column=0, padx=3, pady=3)

Gamestartlabel = Labels(med, text="")
Gamestartlabel.grid(row=1, column=0, padx=5, pady=5)

jumblelabel = Labels(med, text="")
jumblelabel.grid(row=1, column=0, padx=5, pady=5)

answerlabel = Labels(med, text="")
answerlabel.grid(row=5, column=0, padx=5, pady=5)


"""label_answer_test = Labels(med, text="")
label_answer_test.grid(row=1, column=0, padx=5, pady=5)"""
