#not using, will put an end screen at the end of each game in the same file.
import sys 
from tkinter import *
import tkinter as tk
import random
from 
"""def menu():
    import exitscreen
    Exitscreen
"""
def playagain():
    end.destroy()
    import Difficulty
    Difficulty
    
with open('easyscore.txt', 'r') as pointopen:
    scores = pointopen.read().splitlines()
    for i, score in enumerate(scores):
        name, points = score.split(', ')
end = Tk()
end.geometry('200x200')
end.configure(bg = '#6693F5')
end.title("Spelling Bee's Spelling Game!")
endlabel = Labels(text="You've completed the Spelling Bee Spelling Game!")
endlabel.grid(row=0, column=0, padx=5, pady=5)
menub = Buttons(text="End game")
menub.grid(row=3, column=0, padx=3, pady=3)
difficultyb = Buttons(text="Play Again", command=playagain)
difficultyb.grid(row=4, column=0, padx=3, pady=3)

