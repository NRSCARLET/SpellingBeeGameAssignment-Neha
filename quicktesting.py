import sys 
from tkinter import *
import tkinter as tk
import random
def actualgame():
    global AnswerEntry, printed_key, correct_answer, level, enterbutton, wordbutton
    level +=1
    answerlabel.config(text="")
    MAX_CHRCTRS = 3
    if level <= 10:
        printed_key = random.choice(list(easy_spell_words_dict))
        correct_answer = easy_spell_words_dict.pop(printed_key)
        jumblelabel.config(text=f"Write the correct word!: {printed_key}")
        enterbutton = Buttons(text="Enter!", command=checkanswer)
        wordbutton.config(text="Print (new) word!", state = "disabled")
        enterbutton.grid(row=4, column=0, padx=3, pady=3)
        AnswerEntry = tk.Entry(ez, bd =5)
        AnswerEntry.grid(row=2, column=0, padx=5, pady=5)
        AnswerEntry.delete(0, tk.END)
    else:
        wordbutton.config(text="End Game!", state = "disabled")
        points = userpoints
        leaderboard = Label(text="Please enter a 3 character name for the leaderboard!")
        leaderboard.grid(row=4, column=0, padx=3, pady=3)
        leaderboardEntry = tk.Entry(ez, bd=5)
        leaderboardEntry.grid(row=5, column=0, padx=5, pady=5)
        LBENT = leaderboardEntry.get()
        if len(LBENT) == 3:
            wordbutton.config(state = "active")
        else:
            leaderboardEntry.delete(MAX_CHRCTRS, tk.END)
        with open('easyscore.txt', 'a') as pointopen:
            pointopen.write(str(points) + "\n")
        ez.destroy()
        import EndScreen
        EndScreen