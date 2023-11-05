import sys 
from tkinter import *
import tkinter as tk
import random
from PIL import Image, ImageTk, ImageSequence
from UserRegandLog import playing_user, Labels, Buttons
hard_spell_words_dict={"ytabeu" : "beauty", "bafcir" : "fabric", "shabti" : "habits", "afcdea" : "facade", "kachre" : "hacker", "oachns" : "nachos", "yfacip" : "pacify", "biabtr" : "rabbit", "umacuv" : "vacuum", "ddwlae" : "waddle", "chstay" : "yachts", "gzigde" : "zigged", "baroda" : "abroad", "auslac" : "casual", "eimdum" : "medium", "balces" : "cables", "efaetd" : "defeat", "ibehdn" : "behind", "mereeg" : "emerge", "dibger" : "bridge", "pwrapde" : "wrapped", "balyiti" : "ability", "cpaniat" : "captain", "heantbe" : "beneath", "turceny" : "century", "xniauso" : "anxious", "viddied" : "divided", "conemyo" : "economy", "eadises" : "disease", "awytage" : "gateway", "laehtyh" : "healthy", "leilagl" : "illegal", "tiyjusf" : "justify", "xamiumm" : "maximum", "lqicuky" : "quickly", "siaspve" : "passive", "rmovdee" : "removed", "loevint" : "violent", "tisfasy" : "satisfy", "liyqauf" : "qualify"}

jumbled_word = ""
correct_answer = ""
printed_key = ""
AnswerEntryhard = None
enterbutton = None
wordbutton = None
points = None
username = None
userpoints = 0
level = 0
gamestartpoint = 0
warningwindow_open = False
#words for hints (in order): beauty, fabric, habits, facade, hacker, nachos, pacify, rabbit, vacuum, waddle, yachts, zigged, abroad, casual, hardium, cables, defeat, behind, emerge, bridge, wrapped, ability, captain, beneath, century, anxious, divided, economy, disease, gateway, healthy, illegal, justify, maximum, quickly, passive, removed, violent, satisfy, qualify.


def nox():
    pass


def resetgame():
    global level, gamestartpoint, userpoints, current_user, playing_user
    level = 0
    userpoints = 0
    gamestartpoint = 0
    playing_user = ""
    pass


def update_image():
    global hard, gif_frames_iter, gif_frames
    try:
        current_frame = next(gif_frames_iter)
        tk_image = ImageTk.PhotoImage(current_frame)
        label.config(image=tk_image)
        label.image = tk_image
        hard.after(50, update_image)
    except StopIteration:
        gif_frames_iter = iter(gif_frames_resized)
        hard.after(100, update_image)


def resize_gif(gif_frames, new_width, new_height):
    resized_frames = [frame.resize((new_width, new_height)) for frame in gif_frames]
    return resized_frames


def validate_input(typed_char):
    return typed_char.isalpha() or typed_char == ""


def end():
    hard.destroy()
    resetgame()
    import EndScreen
    EndScreen


def checkanswer():
    global userpoints, gif_frames, gif_frames_iter, gif_frames_resized, label
    user_answer = AnswerEntryhard.get().lower()
    AnswerEntryhard.delete(0, END)
    AnswerEntryhard.config(state = "disabled")
    enterbutton.config(state = "disabled")
    wordbutton.config(state = "active")
    if user_answer == correct_answer:
        hard.geometry("520x400")
        answerlabel.config(text=f"CORRECT! The answer is {correct_answer}!")
        userpoints += 1
        points.config(text=f"Points: {userpoints}")
        gif_path = "beegoodjobyes.png"
        gif = Image.open(gif_path)
        gif_frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]
        new_width = 200
        new_height = 150
        gif_frames_resized = resize_gif(gif_frames, new_width, new_height)
        gif_frames_iter = iter(gif_frames_resized)
        initial_frame = next(gif_frames_iter)
        initial_frame_tk = ImageTk.PhotoImage(initial_frame)
        label = tk.Label(hard, image=initial_frame_tk)
        label.grid(row=7, column=0, padx=5, pady=5)
        gif_after_id=hard.after(80, update_image)
    else:

        hard.geometry("520x400")
        answerlabel.config(text=f"INCORRECT! The answer was {correct_answer}!")
        gif_path = "beenophoto.png"
        gif = Image.open(gif_path)
        gif_frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]
        new_width = 200
        new_height = 150
        gif_frames_resized = resize_gif(gif_frames, new_width, new_height)
        gif_frames_iter = iter(gif_frames_resized)
        initial_frame = next(gif_frames_iter)
        initial_frame_tk = ImageTk.PhotoImage(initial_frame)
        label = tk.Label(hard, image=initial_frame_tk)
        label.grid(row=7, column=0, padx=5, pady=5)
        gif_after_id=hard.after(50, update_image)



def actualgame(playing_user):
    hard.geometry("520x230")
    global AnswerEntryhard, printed_key, correct_answer, level, enterbutton, wordbutton, points, gamestartpoint, menub4
    level +=1
    gamestartpoint +=1
    answerlabel.config(text="")
    points.config(text=f"Points: {userpoints}")
    levels.config(text=f"Level: {level}")
    if level <= 10:
        AnswerEntryhard.grid(row=2, column=0, padx=5, pady=5)
        AnswerEntryhard.config(state = "normal")
        printed_key = random.choice(list(hard_spell_words_dict))
        correct_answer = hard_spell_words_dict.pop(printed_key)
        jumblelabel.config(text=f"Write the correct word!: {printed_key}")
        enterbutton.config(state="active", text="Enter!", command=checkanswer)
        enterbutton.grid(row=4, column=0, padx=3, pady=3)
        wordbutton.config(text="Print (new) word!", state = "disabled")
        menub4.grid(row=5, column=0, padx=3, pady=3)
        menub4.config(state="active")
    else:
        hard.geometry("520x150")
        Gamestartlabel.config(text="Please press the 'End game' button to continue to the end screen")
        AnswerEntryhard.destroy()
        enterbutton.destroy()
        points.destroy()
        levels.destroy()
        menub4.destroy()
        with open('hardscore.txt', 'a') as pointopen:
            pointopen.write(f"{playing_user}, {userpoints}" + "\n")
            pointopen.close()
        with open('hardscore.txt', 'r') as pointopen:
            scores = pointopen.read().splitlines()
            for score in scores:
                username, points = score.split(', ')
                points = int(points)
                if username == playing_user:
                    if points < 5:
                        jumblelabel.config(text=f"Better luck next time {playing_user}!")
                    elif points == 10:
                        jumblelabel.config(text=f"WOAH a perfect score!! Amazing job {playing_user}!")
    
                    else:
                        jumblelabel.config(text=f"Great job {playing_user}!")
                    pointlabel = Labels(text=f"You scored {points} out of 10!")
                    pointlabel.grid(row=2, column=0, padx=5, pady=5)
                    wordbutton.config(text="End game!", command = end)
                    break

def backtogame():
    global warningwindow_open
    warningwindow.destroy()
    warningwindow_open = False
    pass


def leavemiddlegame():
    global warningwindow_open
    hard.destroy()
    resetgame()
    warningwindow_open = False
    import MenuWindow
    MenuWindow.menu_wind()


def leavewarning():
    global warningwindow_open, warningwindow
    if not warningwindow_open:
        warningwindow_open = True
        warningwindow = tk.Toplevel(hard)
        warningwindow.title("Spelling Bee's Spelling Game!")
        warningwindow.geometry("615x170")
        warningwindow.configure(bg ='#F56693')
        warningwindow.transient(hard)
        warningwindow.grab_set()
        warningwindow.protocol("WM_DELETE_WINDOW", nox)
        warninglabel = Label(warningwindow, text="Are you sure you want to leave?\nNote: Your progress will NOT be saved if you leave in the middle of the game.\n Progress (points) will only be saved once you complete the game.\nClicking 'Yes' will result in being taken back to the menu.\nClicking 'No' will result in the game continuing.", bg='#F56693', fg='#2A0134', font='helvetica 10 bold')
        warninglabel.grid(row=0, column=0, padx=5, pady=5)
        yesmenu = Buttons(warningwindow, text="Yes", command=lambda: leavemiddlegame())
        yesmenu.grid(row=1, column=0, padx=3, pady=3)
        nomenu = Buttons(warningwindow, text="No", command=lambda: backtogame())
        nomenu.grid(row=2, column=0, padx=3, pady=3)

def difficultywindow():
    hard.destroy()
    import Difficulty
    Difficulty.difficultywindow()

def menu():
    if gamestartpoint == 0:
        leavemiddlegame()
    else:
        leavewarning()

def hardgamestart():
    global wordbutton
    hard.geometry("430x100")
    Gamestartlabel.config(text="Unscramble the words and write the correct spelling!")
    Gamestartlabel.grid(row=0, column=0, padx=5, pady=5)
    wordbutton = Buttons(text="Okay!", command=lambda: actualgame(playing_user))
    wordbutton.grid(row=3, column=0, padx=3, pady=3)

    h.destroy()
    conbutton.destroy()
    backb1.destroy()
    menub4.grid_forget()
    """Q1label = tk.Label(text="Please pick the correct spelling of [insert thing here]")
    Q1label.pack()
    Q1CB = Buttons(hard, text="paw")
    Q1CB.pack()
    Q1INCB1 = Buttons(text="liw")
    Q1INCB1.pack()
    Q1INCB2 = Buttons(text="pey")
    Q1INCB2.pack()"""
    

def hardwindow():
    global hard, h, conbutton, backb1, menub4, Gamestartlabel, jumblelabel, answerlabel, points, levels, AnswerEntryhard, enterbutton
    hard = Tk()
    hard.geometry('210x200')
    hard.configure(bg = '#6693F5')
    hard.title("Spelling Bee's Spelling Game!")
    h = Labels(text="You've picked hard mode")
    h.grid(row=0, column=0, padx=5, pady=5)
    validate_cmd = hard.register(validate_input)
    hard.protocol("WM_DELETE_WINDOW", nox)
    conbutton = Buttons(text="Continue", command = hardgamestart)
    conbutton.grid(row=2, column=0, padx=3, pady=3)
    backb1 = Buttons(text="Back", command = difficultywindow)
    backb1.grid(row=3, column=0, padx=3, pady=3)
    menub4 = Buttons(text="Menu", command = menu)
    menub4.grid(row=4, column=0, padx=3, pady=3)
    Gamestartlabel = Labels(hard, text="")
    Gamestartlabel.grid(row=1, column=0, padx=5, pady=5)
    jumblelabel = Labels(hard, text="")
    jumblelabel.grid(row=1, column=0, padx=5, pady=5)
    answerlabel = Labels(hard, text="")
    answerlabel.grid(row=6, column=0, padx=5, pady=5)
    points = Labels(hard, text="")
    points.grid(row=0, column=1, padx=5, pady=5)
    levels = Labels(hard, text="")
    levels.grid(row=1, column=1, padx=5, pady=5)
    AnswerEntryhard = tk.Entry(hard, bd =5, validate="key", validatecommand=(validate_cmd, "%S"))
    AnswerEntryhard.grid()
    AnswerEntryhard.grid_forget()
    enterbutton = Buttons(text="")
    enterbutton.grid()
    enterbutton.grid_forget()