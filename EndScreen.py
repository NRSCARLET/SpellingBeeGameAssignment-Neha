#not using, will put an end screen at the end of each game in the same file.
import sys 
from tkinter import *
import tkinter as tk
import random
from UserRegandLog import Labels, Buttons
"""def menu():
    import exitscreen
    Exitscreen
"""
def playagain():
    end.destroy()
    import Difficulty
    Difficulty


def endgame():
    end.geometry("500x50")
    endlabel.destroy()
    notelabel.destroy()
    menub.destroy()
    difficultyb.destroy()
    ty = Labels(end, text="Thank you for playing! See you later!\nPlease press the 'x' at the top right of the window to close it.")
    ty.grid(row=0, column=0, padx=5, pady=5)


end = Tk()
end.geometry('640x200')
end.configure(bg = '#6693F5')
end.title("Spelling Bee's Spelling Game!")
endlabel = Labels(text="You've completed the Spelling Bee Spelling Game!")
endlabel.grid(row=0, column=0, padx=5, pady=5)
notelabel = Labels(end, text="Note: Pressing the 'Play Again' button will take you back to the difficulty screen.\nPressing the 'End Game' button will end the game.")
notelabel.grid(row=1, column=0, padx=5, pady=5)
menub = Buttons(text="End Game", command=endgame)
menub.grid(row=3, column=0, padx=3, pady=3)
difficultyb = Buttons(text="Play Again", command=playagain)
difficultyb.grid(row=4, column=0, padx=3, pady=3)

