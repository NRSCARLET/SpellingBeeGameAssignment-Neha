import sys 
from tkinter import *
import tkinter as tk
import random
from UserRegandLog import playing_user, Labels, Buttons
"""easy_spell_word_hint = ["btut", "bzzu", "ogod", "tars", "labl", "alfl", "chea", "anme", "ctih", "rogw", "etre", "mila", "wrad", "leyl", "meit", "sahd", "chsa", "eadd", "nabg", "urde", "siks", "ribd", "avse", "orpe", "uleg", "uphs", "ulpl", "stre", "yter", "ewts", "stea", "ongs", "sevt", "kics", "eken", "ttse", "darh", "ysea", "rohn"]"""

easy_spell_words_dict={
"tebn":"bent","bzzu":"buzz","ogod":"good","tars":"star","labl":"ball","alfl":"fall","chea":"ache","anme":"name",
"ctih":"itch","rogw":"grow","etre":"tree","sneo":"nose",      "mila":"mail","wrad":"draw","leyl":"yell","meit":"time",      "sahd":"dash","chsa":"cash","eadd":"dead","nabg":"bang",      "urde":"rude","eahv":"have","ribd":"bird","avse":"vase",      "orpe":"rope","uleg":"glue","uphs":"push","ulpl":"pull",      "stre":"rest","yter":"tyre","ewts":"west","stea":"east",      "ongs":"song","sevt":"vest","kics":"sick","eken":"knee",
"ttse":"test","darh":"hard","ysea":"easy","rohn":"horn"}

jumbled_word = ""
correct_answer = ""
printed_key = ""
AnswerEntry = None
enterbutton = None
wordbutton = None
points = None
userpoints = 0
level = 0
gamestartpoint = 0
#words for hints (in order): butt, buzz, good, star, ball, fall, ache, name, itch, grow, tree, nose, mail, draw, yell, time, dash, cash, dead, bang, rude, kiss, bird, vase, rope, glue, push, pull, rest, tyre, west, east, song, vest, sick, knee, test, hard, easy, horn - 40 words (unjumbled words)
        
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


def validate_input(typed_char):
    return typed_char.isalpha() or typed_char == ""
    

def end():
    easy.destroy()
    import EndScreen
    EndScreen


def checkanswer():
    global userpoints
    user_answer = AnswerEntryeasy.get().lower()
    AnswerEntryeasy.delete(0, END)
    AnswerEntryeasy.config(state = "disabled")
    enterbutton.config(state = "disabled")
    wordbutton.config(state = "active")
    if user_answer == correct_answer:
        answerlabel.config(text=f"CORRECT! The answer is {correct_answer}!")
        userpoints += 1
        points.config(text=f"Points: {userpoints}")
    else:
        answerlabel.config(text=f"INCORRECT! The answer was {correct_answer}!")

    
def actualgame():
    easy.geometry("520x250")
    global AnswerEntryeasy, printed_key, correct_answer, level, enterbutton, wordbutton, points, gamestartpoint
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
    else:
        Gamestartlabel.config(text="Please press the 'End game' button to continue to the end screen")
        AnswerEntryeasy.destroy()
        enterbutton.destroy()
        points.destroy()
        levels.destroy()
        with open('easyscore.txt', 'a') as pointopen:
            pointopen.write(f"{playing_user}, {userpoints}" + "\n")
            pointopen.close()
        with open('easyscore.txt', 'r') as pointopen:
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
    easy.destroy()
    import MenuWindow
    MenuWindow.menu_wind()


def leavewarning():
    warningwindow = tk.Toplevel(easy)
    warningwindow.title("Spelling Bee's Spelling Game!")
    warningwindow.geometry("615x170")
    warningwindow.configure(bg ='#F56693')
    warningwindow.transient(easy)
    warningwindow.grab_set()
    warninglabel = Label(warningwindow, text="Are you sure you want to leave?\nNote: Your progress will NOT be saved if you leave in the middle of the game.\n Progress (points) will only be saved once you complete the game.\nClicking 'Yes' will result in being taken back to the menu.\nClicking 'No' will result in the game continuing.", bg='#F56693', fg='#2A0134', font='helvetica 10 bold')
    warninglabel.grid(row=0, column=0, padx=5, pady=5)
    yesmenu = Buttons(warningwindow, text="Yes", command=lambda: leavemiddlegame(warningwindow))
    yesmenu.grid(row=1, column=0, padx=3, pady=3)
    nomenu = Buttons(warningwindow, text="No", command=lambda: backtogame(warningwindow))
    nomenu.grid(row=2, column=0, padx=3, pady=3)

def difficultywindow():
    easy.destroy()
    import Difficulty
    Difficulty.difficultywindow()

def menu():
    if gamestartpoint == 0:
        easy.destroy()
        import MenuWindow
        MenuWindow.menu_wind()
    else:
        leavewarning()

def easygamestart():
    global wordbutton
    easy.geometry("430x100")
    Gamestartlabel.config(text="Unscramble the words and write the correct spelling!")
    Gamestartlabel.grid(row=0, column=0, padx=5, pady=5)

    wordbutton = Buttons(text="Okay!", command = actualgame)
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

"""Got this code from ChatGPT. I got stuck trying to find out how to animate my gif (I only managed to insert it as a static image)"""
def update_image():
    global gif_frames_iter  # Declare gif_frames_iter as a global variable
    try:
        # Get the next frame from the GIF
        current_frame = next(gif_frames_iter)

        # Convert the PIL image to a Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(current_frame)

        # Update the label with the new image
        label.config(image=tk_image)
        label.image = tk_image  # This line is crucial for proper garbage collection
        root.after(50, update_image)  # Schedule the update after 100 milliseconds (adjust as needed)
    except StopIteration:
        # If we reach the end of the frames, restart the animation
        gif_frames_iter = iter(gif_frames)
        root.after(100, update_image)  # Schedule the update after 100 milliseconds (adjust as needed)

# Create the main Tkinter window
root = tk.Tk()
root.title("Animated GIF")

# Open the GIF file
gif_path = "beeidlegif.gif"
gif = Image.open(gif_path)
# Extract individual frames from the GIF
gif_frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]
# Create an iterator to loop through the frames
gif_frames_iter = iter(gif_frames)

# Display the initial frame
initial_frame = next(gif_frames_iter)
initial_frame_tk = ImageTk.PhotoImage(initial_frame)
label = tk.Label(root, image=initial_frame_tk)
label.pack()

# Schedule the update function to animate the GIF
root.after(50, update_image)


def easywindow():
    global easy, e, conbutton, backb1, menub4, Gamestartlabel, jumblelabel, answerlabel, points, levels, AnswerEntryeasy, enterbutton
    easy = Tk()
    easy.geometry('210x200')
    easy.configure(bg = '#6693F5')
    easy.title("Spelling Bee's Spelling Game!")
    e = Labels(text="You've picked easy mode")
    e.grid(row=0, column=0, padx=5, pady=5)
    validate_cmd = easy.register(validate_input)
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


"""label_answer_test = Labels(easy, text="")
label_answer_test.grid(row=1, column=0, padx=5, pady=5)"""
