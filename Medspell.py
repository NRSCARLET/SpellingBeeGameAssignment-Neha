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


def update_image():
    global easy, gif_frames_iter, gif_frames, gif_playing
    try:
        current_frame = next(gif_frames_iter)
        tk_image = ImageTk.PhotoImage(current_frame)
        label.config(image=tk_image)
        label.image = tk_image
        easy.after(50, update_image)
        if gif_playing:
            easy.after_update(gif_after_id)
    except StopIteration:
        gif_frames_iter = iter(gif_frames_resized)
        easy.after(100, update_image)


def resize_gif(gif_frames, new_width, new_height):
    resized_frames = [frame.resize((new_width, new_height)) for frame in gif_frames]
    return resized_frames


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
        gif_after_id=easy.after(80, update_image)

    
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


def backtogame(warningwindow):
    warningwindow.destroy()
    pass


def leavemiddlegame(warningwindow):
    med.destroy()
    import MenuWindow
    MenuWindow.menu_wind()


def leavewarning():
    warningwindow = tk.Toplevel(med)
    warningwindow.title("Spelling Bee's Spelling Game!")
    warningwindow.geometry("615x170")
    warningwindow.configure(bg ='#F56693')
    warningwindow.transient(med)
    warningwindow.grab_set()
    warninglabel = Label(warningwindow, text="Are you sure you want to leave?\nNote: Your progress will NOT be saved if you leave in the middle of the game.\n Progress (points) will only be saved once you complete the game.\nClicking 'Yes' will result in being taken back to the menu.\nClicking 'No' will result in the game continuing.", bg='#F56693', fg='#2A0134', font='helvetica 10 bold')
    warninglabel.grid(row=0, column=0, padx=5, pady=5)
    yesmenu = Buttons(warningwindow, text="Yes", command=lambda: leavemiddlegame(warningwindow))
    yesmenu.grid(row=1, column=0, padx=3, pady=3)
    nomenu = Buttons(warningwindow, text="No", command=lambda: backtogame(warningwindow))
    nomenu.grid(row=2, column=0, padx=3, pady=3)



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
    global med, m, conbutton, backb2, menub5, Gamestartlabel, jumblelabel, answerlabel, points, levels, AnswerEntrymed, enterbutton
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
