import sys 
from tkinter import *
import tkinter as tk
import random
from PIL import Image, ImageTk, ImageSequence
from UserRegandLog import playing_user, Labels, Buttons
easy_spell_words_dict={
"tebn":"bent","bzzu":"buzz","ogod":"good","tars":"star","labl":"ball","alfl":"fall","chea":"ache","anme":"name",
"ctih":"itch","rogw":"grow","etre":"tree","sneo":"nose",      "mila":"mail","wrad":"draw","leyl":"yell","meit":"time",      "sahd":"dash","chsa":"cash","eadd":"dead","nabg":"bang",      "urde":"rude","eahv":"have","ribd":"bird","avse":"vase",      "orpe":"rope","uleg":"glue","uphs":"push","ulpl":"pull",      "stre":"rest","yter":"tyre","ewts":"west","stea":"east",      "ongs":"song","sevt":"vest","kics":"sick","eken":"knee",
"ttse":"test","darh":"hard","ysea":"easy","rohn":"horn"}


jumbled_word = ""
correct_answer = ""
printed_key = ""
AnswerEntryeasy = None
enterbutton = None
wordbutton = None
points = None
username = None
userpoints = 0
level = 0
gamestartpoint = 0
warningwindow_open = False


def nox():
    pass


def resetgame():
    global level, gamestartpoint, userpoints
    level = 0
    userpoints = 0
    gamestartpoint = 0
    pass


def update_image():
    global easy, gif_frames_iter, gif_frames
    try:
        current_frame = next(gif_frames_iter)
        tk_image = ImageTk.PhotoImage(current_frame)
        label.config(image=tk_image)
        label.image = tk_image
        easy.after(50, update_image)
    except StopIteration:
        gif_frames_iter = iter(gif_frames_resized)
        easy.after(100, update_image)


def resize_gif(gif_frames, new_width, new_height):
    resized_frames = [frame.resize((new_width, new_height)) for frame in gif_frames]
    return resized_frames


def validate_input(typed_char):
    return typed_char.isalpha() or typed_char == ""


def end():
    easy.destroy()
    resetgame()
    playing_user = ""
    import EndScreen
    EndScreen


def checkanswer():
    global userpoints, gif_frames, gif_frames_iter, gif_frames_resized, label
    user_answer = AnswerEntryeasy.get().lower()
    AnswerEntryeasy.delete(0, END)
    AnswerEntryeasy.config(state = "disabled")
    enterbutton.config(state = "disabled")
    wordbutton.config(state = "active")
    if user_answer == correct_answer:
        easy.geometry("520x400")
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
        label = tk.Label(easy, image=initial_frame_tk)
        label.grid(row=7, column=0, padx=5, pady=5)
        gif_after_id=easy.after(80, update_image)
    else:

        easy.geometry("520x400")
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
        label = tk.Label(easy, image=initial_frame_tk)
        label.grid(row=7, column=0, padx=5, pady=5)
        gif_after_id=easy.after(50, update_image)



def actualgame(playing_user):
    easy.geometry("520x230")
    global AnswerEntryeasy, printed_key, correct_answer, level, enterbutton, wordbutton, points, gamestartpoint, menub4
    level +=1
    gamestartpoint +=1
    answerlabel.config(text="")
    points.config(text=f"Points: {userpoints}")
    levels.config(text=f"Level: {level}")
    if level <= 10:
        AnswerEntryeasy.grid(row=2, column=0, padx=5, pady=5)
        AnswerEntryeasy.config(state = "normal")
        printed_key = random.choice(list(easy_spell_words_dict))
        correct_answer = easy_spell_words_dict.pop(printed_key)
        jumblelabel.config(text=f"Write the correct word!: {printed_key}")
        enterbutton.config(state="active", text="Enter!", command=checkanswer)
        enterbutton.grid(row=4, column=0, padx=3, pady=3)
        wordbutton.config(text="Print (new) word!", state = "disabled")
        menub4.grid(row=5, column=0, padx=3, pady=3)
        menub4.config(state="active")
        if level == 10:
            wordbutton.config(text="Finish!" , state = "disabled")
    else:
        easy.geometry("520x150")
        Gamestartlabel.config(text="Please press the 'End game' button to continue to the end screen")
        AnswerEntryeasy.destroy()
        enterbutton.destroy()
        points.destroy()
        levels.destroy()
        menub4.destroy()
        with open('easyscore.txt', 'a') as pointopen:
            pointopen.write(f"{playing_user}, {userpoints}" + "\n")
            pointopen.close()
        with open('easyscore.txt', 'r') as pointwrite:
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
    easy.destroy()
    resetgame()
    playing_user = ""
    warningwindow_open = False
    import resetprogram
    resetprogram.RP()


def leavewarning():
    global warningwindow_open, warningwindow
    if not warningwindow_open:
        warningwindow_open = True
        warningwindow = tk.Toplevel(easy)
        warningwindow.title("Spelling Bee's Spelling Game!")
        warningwindow.geometry("615x170")
        warningwindow.configure(bg ='#F56693')
        warningwindow.transient(easy)
        warningwindow.grab_set()
        warningwindow.protocol("WM_DELETE_WINDOW", nox)
        warninglabel = Label(warningwindow, text="Are you sure you want to leave?\nNote: Your progress will NOT be saved if you leave in the middle of the game.\n Progress (points) will only be saved once you complete the game.\nClicking 'Yes' will result in being taken back to the menu.\nClicking 'No' will result in the game continuing.", bg='#F56693', fg='#2A0134', font='helvetica 10 bold')
        warninglabel.grid(row=0, column=0, padx=5, pady=5)
        yesmenu = Buttons(warningwindow, text="Yes", command=lambda: leavemiddlegame())
        yesmenu.grid(row=1, column=0, padx=3, pady=3)
        nomenu = Buttons(warningwindow, text="No", command=lambda: backtogame())
        nomenu.grid(row=2, column=0, padx=3, pady=3)

def difficultywindow():
    easy.destroy()
    import Difficulty
    Difficulty.difficultywindow()

def menu():
    if gamestartpoint == 0:
        leavemiddlegame()
    else:
        leavewarning()

def easygamestart():
    global wordbutton
    easy.geometry("430x100")
    Gamestartlabel.config(text="Unscramble the words and write the correct spelling!")
    Gamestartlabel.grid(row=0, column=0, padx=5, pady=5)
    wordbutton = Buttons(text="Okay!", command=lambda: actualgame(playing_user))
    wordbutton.grid(row=3, column=0, padx=3, pady=3)

    e.destroy()
    conbutton.destroy()
    backb1.destroy()
    menub4.grid_forget()
    """Q1label = tk.Label(text="Please pick the correct spelling of [insert thing here]")
    Q1label.pack()
    Q1CB = Buttons(easy, text="paw")
    Q1CB.pack()
    Q1INCB1 = Buttons(text="liw")
    Q1INCB1.pack()
    Q1INCB2 = Buttons(text="pey")
    Q1INCB2.pack()"""


def easywindow():
    global easy, e, conbutton, backb1, menub4, Gamestartlabel, jumblelabel, answerlabel, points, levels, AnswerEntryeasy, enterbutton
    easy = Tk()
    easy.geometry('210x200')
    easy.configure(bg = '#6693F5')
    easy.title("Spelling Bee's Spelling Game!")
    e = Labels(text="You've picked easy mode")
    e.grid(row=0, column=0, padx=5, pady=5)
    validate_cmd = easy.register(validate_input)
    easy.protocol("WM_DELETE_WINDOW", nox)
    conbutton = Buttons(text="Continue", command = easygamestart)
    conbutton.grid(row=2, column=0, padx=3, pady=3)
    backb1 = Buttons(text="Back", command = difficultywindow)
    backb1.grid(row=3, column=0, padx=3, pady=3)
    menub4 = Buttons(text="Menu", command = menu)
    menub4.grid(row=4, column=0, padx=3, pady=3)
    Gamestartlabel = Labels(easy, text="")
    Gamestartlabel.grid(row=1, column=0, padx=5, pady=5)
    jumblelabel = Labels(easy, text="")
    jumblelabel.grid(row=1, column=0, padx=5, pady=5)
    answerlabel = Labels(easy, text="")
    answerlabel.grid(row=6, column=0, padx=5, pady=5)
    points = Labels(easy, text="")
    points.grid(row=0, column=1, padx=5, pady=5)
    levels = Labels(easy, text="")
    levels.grid(row=1, column=1, padx=5, pady=5)
    AnswerEntryeasy = tk.Entry(easy, bd =5, validate="key", validatecommand=(validate_cmd, "%S"))
    AnswerEntryeasy.grid()
    AnswerEntryeasy.grid_forget()
    enterbutton = Buttons(text="")
    enterbutton.grid()
    enterbutton.grid_forget()