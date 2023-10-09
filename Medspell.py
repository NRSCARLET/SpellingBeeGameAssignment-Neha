import sys 
from tkinter import *
import tkinter as tk
import random
from UserRegandLog import playing_user, Labels, Buttons
med_spell_words_dict={
"rubnt" : "burnt", "intop" : "point", "tiwre" : "write", "tenea" : "eaten", "euqne" : "queen", "uoqet" : "quote", "pleap" : "apple", "elsfe" : "feels", "ovetd" : "voted", "asthe" : "haste", "bazer" : "zebra", "rufry" : "furry", "zifyz" : "fizzy", "iqkcu" : "quick", "foerf" : "offer", "rwory" : "worry", "wetak" : "tweak", "rpnti" : "print", "psrot" : "sport", "aostt" : "toast", "dadre" : "dread", "rtate" : "treat", "ayrcz" : "crazy", "uqkac" : "quack", "onsud" : "sound", "veasw" : "waves", "mujps" : "jumps", "padre" : "drape", "eevah" : "heave", "eaocn" : "ocean", "echba" : "beach", "hiwle" : "while", "airot" : "ratio", "yhvea" : "heavy", "vargy" : "gravy", "zidzy" : "dizzy", "ooakz" : "kazoo", "ratos" : "roast", "kalef" : "flake", "sulfh" : "flush"}

jumbled_word = ""
correct_answer = ""
printed_key = ""
AnswerEntrymed = None
enterbutton = None
wordbutton = None
userpoints = 0
level = 0
points = None
#words for hints (in order): burnt, point, write, eaten, queen, quote, apple, feels, voted, haste, zebra, furry, fizzy, quick, offer, worry, tweak, print, sport, toast, dread, treat, crazy, quack, sound, waves, jumps, drape, heave, ocean, beach, while, ratio, heavy, gravy, dizzy, kazoo, roast, flake, flush


def validate_input(typed_char):
    return typed_char.isalpha() or typed_char == ""


def end():
    med.destroy()
    import EndScreen
    EndScreen


def checkanswer():
    global userpoints
    user_answer = AnswerEntrymed.get().lower()
    AnswerEntrymed.delete(0, END)
    AnswerEntrymed.config(state = "disabled")
    enterbutton.config(state = "disabled")
    wordbutton.config(state = "active")
    if user_answer == correct_answer:
        answerlabel.config(text=f"CORRECT! The answer is {correct_answer}!")
        userpoints += 1
        points.config(text=f"Points: {userpoints}")
    else:
        answerlabel.config(text=f"INCORRECT! The answer was {correct_answer}!")

    
def actualgame():
    global AnswerEntrymed, printed_key, correct_answer, level, enterbutton, wordbutton, points
    level +=1
    answerlabel.config(text="")
    points.config(text=f"Points: {userpoints}")
    levels.config(text=f"Level: {level}")
    med.geometry("520x250")
    if level <= 10:
        AnswerEntrymed.grid(row=2, column=0, padx=5, pady=5)
        AnswerEntrymed.config(state = "normal")
        printed_key = random.choice(list(med_spell_words_dict))
        correct_answer = med_spell_words_dict.pop(printed_key)
        jumblelabel.config(text=f"Write the correct word!: {printed_key}")
        enterbutton.config(state="active", text="Enter!", command=checkanswer)
        enterbutton.grid(row=4, column=0, padx=3, pady=3)
        wordbutton.config(text="Print (new) word!", state = "disabled")
        menub5.config(state="active")
        menub5.grid(row=5, column=0, padx=3, pady=3)
    else:
        Gamestartlabel.config(text="Please press the 'End game' button to continue to the end screen")
        AnswerEntrymed.destroy()
        enterbutton.destroy()
        points.destroy()
        levels.destroy()
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
                wordbutton.config(text="End game!", command = end)
        



def difficultywindow():
    med.destroy()
    import Difficulty
    Difficulty.difficultywindow()

def menu():
    med.destroy()
    import MenuWindow
    MenuWindow.menu_wind()

def easygamestart():
    global wordbutton
    med.geometry("430x100")
    Gamestartlabel.config(text="Unscramble the words and write the correct spelling!")
    Gamestartlabel.grid(row=0, column=0, padx=5, pady=5)

    wordbutton = Buttons(text="Okay!", command = actualgame)
    wordbutton.grid(row=3, column=0, padx=3, pady=3)
    
    m.destroy()
    conbutton.destroy()
    backb2.destroy()
    menub5.grid_forget()


def medwindow():
    global med
    med = Tk()
    med.geometry('240x200')
    med.configure(bg = '#6693F5')
    med.title("Spelling Bee's Spelling Game!")
    m = Labels(text="You've picked medium mode")
    m.grid(row=0, column=0, padx=5, pady=5)
    validate_cmd = med.register(validate_input)
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
    answerlabel.grid(row=6, column=0, padx=5, pady=5)
    points = Labels(med, text="")
    points.grid(row=0, column=1, padx=5, pady=5)
    levels = Labels(med, text="")
    levels.grid(row=1, column=1, padx=5, pady=5)
    AnswerEntrymed = tk.Entry(med, bd =5, validate="key", validatecommand=(validate_cmd, "%S"))
    AnswerEntrymed.grid()
    AnswerEntrymed.grid_forget()
    enterbutton = Buttons(text="")
    enterbutton.grid()
    enterbutton.grid_forget()

"""label_answer_test = Labels(med, text="")
label_answer_test.grid(row=1, column=0, padx=5, pady=5)"""
