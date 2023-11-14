import sys 
from tkinter import *
import tkinter as tk
import random
from PIL import Image, ImageTk, ImageSequence
from UserRegandLog import playing_user, Labels, Buttons
med_spell_words_dict={
"rubnt" : "burnt", "intop" : "point", "tiwre" : "write", "tenea" : "eaten", "euqne" : "queen", "uoqet" : "quote", "pleap" : "apple", "elsfe" : "feels", "ovetd" : "voted", "asthe" : "haste", "bazer" : "zebra", "rufry" : "furry", "zifyz" : "fizzy", "iqkcu" : "quick", "foerf" : "offer", "rwory" : "worry", "wetak" : "tweak", "rpnti" : "print", "psrot" : "sport", "aostt" : "toast", "dadre" : "dread", "rtate" : "treat", "ayrcz" : "crazy", "uqkac" : "quack", "onsud" : "sound", "veasw" : "waves", "mujps" : "jumps", "padre" : "drape", "eevah" : "heave", "eaocn" : "ocean", "echba" : "beach", "hiwle" : "while", "airot" : "ratio", "yhvea" : "heavy", "vargy" : "gravy", "zidzy" : "dizzy", "ooakz" : "kazoo", "ratos" : "roast", "kalef" : "flake", "sulfh" : "flush"}


jumbled_word = ""
correct_answer = ""
printed_key = ""
AnswerEntrymed = None
enterbutton = None
wordbutton = None
points = None
username = None
userpoints = 0
level = 0
gamestartpoint = 0
warningwindow_open = False
instructionwindow_open = False


def nox():
    pass


def resetgame():
    global level, gamestartpoint, userpoints
    level = 0
    userpoints = 0
    gamestartpoint = 0
    pass


def update_image():
    global med, gif_frames_iter, gif_frames
    try:
        current_frame = next(gif_frames_iter)
        tk_image = ImageTk.PhotoImage(current_frame)
        label.config(image=tk_image)
        label.image = tk_image
        med.after(50, update_image)
    except StopIteration:
        gif_frames_iter = iter(gif_frames_resized)
        med.after(100, update_image)


def resize_gif(gif_frames, new_width, new_height):
    resized_frames = [frame.resize((new_width, new_height)) for frame in gif_frames]
    return resized_frames


def validate_input(typed_char):
    return typed_char.isalpha() or typed_char == ""


def end():
    med.destroy()
    resetgame()
    playing_user = ""
    import EndScreen
    EndScreen


def checkanswer():
    global userpoints, gif_frames, gif_frames_iter, gif_frames_resized, label
    user_answer = AnswerEntrymed.get().lower()
    AnswerEntrymed.delete(0, END)
    AnswerEntrymed.config(state = "disabled")
    enterbutton.config(state = "disabled")
    wordbutton.config(state = "active")
    if user_answer == correct_answer:
        med.geometry("520x400")
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
        label = tk.Label(med, image=initial_frame_tk)
        label.grid(row=7, column=0, padx=5, pady=5)
        gif_after_id=med.after(80, update_image)
    else:

        med.geometry("520x400")
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
        label = tk.Label(med, image=initial_frame_tk)
        label.grid(row=7, column=0, padx=5, pady=5)
        gif_after_id=med.after(50, update_image)


def closeinstructions():
    global instructionwindow_open
    instructionwindow.destroy()
    instructionwindow_open = False
    pass


def instructions():
    global instructionwindow_open, instructionwindow
    if not instructionwindow_open:
        instructionwindow_open = True
        instructionwindow = tk.Toplevel(med)
        instructionwindow.title("Spelling Bee's Spelling Game!")
        instructionwindow.geometry("600x290")
        instructionwindow.configure(bg ='#b4aaf9')
        instructionwindow.transient(med)
        instructionwindow.protocol("WM_DELETE_WINDOW", nox)
        instructionwindow.overrideredirect(1)
        instructionwindow.grab_set()
        instrctlabel = Label(instructionwindow, text="Game overview:\n>Easy mode: 10 levels, words have 4 letters each\n>Medium mode: 10 levels, words have 5 letters each\nHard mode: 10 levels, words have 6-7 letters each\nHow to play:\n>Register (or log in if you're an existing user)\n>Pick a difficulty (easy, medium, hard)\n>unscramble the word! Based on the letters that appear,\nenter the correct word into the text box!\nGetting the answer correct will reward you with 1 point.\n>Repeat for 10 levels.\n>Once you finish the final level, you will be presented with your score.\n>Play again or exit!\n>Most importantly: HAVE FUN!!", bg='#b4aaf9', fg='#2A0134', font='helvetica 10 bold')
        instrctlabel.grid(row=0, column=0, padx=5, pady=5)
        closebutton = Buttons(instructionwindow, text="Close", command = closeinstructions)
        closebutton.grid(row=1, column=0, padx=3, pady=3)


def actualgame(playing_user):
    med.geometry("520x230")
    global AnswerEntrymed, printed_key, correct_answer, level, enterbutton, wordbutton, points, gamestartpoint, menub4
    level +=1
    gamestartpoint +=1
    answerlabel.config(text="")
    points.config(text=f"Points: {userpoints}")
    levels.config(text=f"Level: {level}")
    if level <= 10:
        instructbutton = Buttons(text="?", command=lambda: instructions())
        instructbutton.grid(row=2, column=1, padx=3, pady=3)
        AnswerEntrymed.grid(row=2, column=0, padx=5, pady=5)
        AnswerEntrymed.config(state = "normal")
        printed_key = random.choice(list(med_spell_words_dict))
        correct_answer = med_spell_words_dict.pop(printed_key)
        jumblelabel.config(text=f"Write the correct word!: {printed_key}")
        enterbutton.config(state="active", text="Enter!", command=checkanswer)
        enterbutton.grid(row=4, column=0, padx=3, pady=3)
        wordbutton.config(text="Print (new) word!", state = "disabled")
        menub4.grid(row=5, column=0, padx=3, pady=3)
        menub4.config(state="active")
        if level == 10:
            wordbutton.config(text="Finish!" , state = "disabled")
    else:
        med.geometry("520x150")
        Gamestartlabel.config(text="Please press the 'End game' button to continue to the end screen")
        AnswerEntrymed.destroy()
        enterbutton.destroy()
        points.destroy()
        levels.destroy()
        menub4.destroy()
        with open('medscore.txt', 'a') as pointopen:
            pointopen.write(f"{playing_user}, {userpoints}" + "\n")
            pointopen.close()
        with open('medscore.txt', 'r') as pointwrite:
            scores = pointwrite.read().splitlines()
            for score in scores:
                parts = score.split(', ')
                if len(parts) == 2:
                    username, points = parts
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
                        wordbutton.config(text="End game!", command=end)
                        break
                        pointwrite.close()

def backtogame():
    global warningwindow_open
    warningwindow.destroy()
    warningwindow_open = False
    pass


def leavemiddlegame():
    global warningwindow_open
    med.destroy()
    resetgame()
    playing_user = ""
    warningwindow_open = False
    import resetprogram
    resetprogram.RP()


def leavewarning():
    global warningwindow_open, warningwindow
    if not warningwindow_open:
        warningwindow_open = True
        warningwindow = tk.Toplevel(med)
        warningwindow.title("Spelling Bee's Spelling Game!")
        warningwindow.geometry("615x170")
        warningwindow.configure(bg ='#F56693')
        warningwindow.transient(med)
        warningwindow.grab_set()
        warningwindow.protocol("WM_DELETE_WINDOW", nox)
        warningwindow.overrideredirect(1)
        warninglabel = Label(warningwindow, text="Are you sure you want to leave?\nNote: Your progress will NOT be saved if you leave in the middle of the game.\n Progress (points) will only be saved once you complete the game.\nClicking 'Yes' will result in being taken back to the menu.\nClicking 'No' will result in the game continuing.", bg='#F56693', fg='#2A0134', font='helvetica 10 bold')
        warninglabel.grid(row=0, column=0, padx=5, pady=5)
        yesmenu = Buttons(warningwindow, text="Yes", command=lambda: leavemiddlegame())
        yesmenu.grid(row=1, column=0, padx=3, pady=3)
        nomenu = Buttons(warningwindow, text="No", command=lambda: backtogame())
        nomenu.grid(row=2, column=0, padx=3, pady=3)

def difficultywindow():
    med.destroy()
    import Difficulty
    Difficulty.difficultywindow()

def menu():
    if gamestartpoint == 0:
        leavemiddlegame()
    else:
        leavewarning()

def medgamestart():
    global wordbutton
    med.geometry("430x100")
    Gamestartlabel.config(text="Unscramble the words and write the correct spelling!")
    Gamestartlabel.grid(row=0, column=0, padx=5, pady=5)
    wordbutton = Buttons(text="Okay!", command=lambda: actualgame(playing_user))
    wordbutton.grid(row=3, column=0, padx=3, pady=3)

    m.destroy()
    conbutton.destroy()
    backb1.destroy()
    menub4.grid_forget()
    """Q1label = tk.Label(text="Please pick the correct spelling of [insert thing here]")
    Q1label.pack()
    Q1CB = Buttons(med, text="paw")
    Q1CB.pack()
    Q1INCB1 = Buttons(text="liw")
    Q1INCB1.pack()
    Q1INCB2 = Buttons(text="pey")
    Q1INCB2.pack()"""


def medwindow():
    global med, m, conbutton, backb1, menub4, Gamestartlabel, jumblelabel, answerlabel, points, levels, AnswerEntrymed, enterbutton
    med = Tk()
    med.geometry('230x200')
    med.configure(bg = '#6693F5')
    med.title("Spelling Bee's Spelling Game!")
    m = Labels(text="You've picked medium mode")
    m.grid(row=0, column=0, padx=5, pady=5)
    validate_cmd = med.register(validate_input)
    med.protocol("WM_DELETE_WINDOW", nox)
    med.overrideredirect(1)
    conbutton = Buttons(text="Continue", command = medgamestart)
    conbutton.grid(row=2, column=0, padx=3, pady=3)
    backb1 = Buttons(text="Back", command = difficultywindow)
    backb1.grid(row=3, column=0, padx=3, pady=3)
    menub4 = Buttons(text="Menu", command = menu)
    menub4.grid(row=4, column=0, padx=3, pady=3)
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