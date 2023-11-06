#CHATGPT help
"""import tkinter as tk

def button_click():
    if button["text"] == "Click Me":
        button["text"] = "Clicked!"
    else:
        button["text"] = "Click Me"

# Create the main window
root = tk.Tk()
root.title("Button Example")

# Create a button
button = tk.Button(root, text="Click Me", command=button_click)
button.pack(padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()"""
"""
import tkinter as tk

def update_label():
    current_value = int(label["text"])
    new_value = current_value + 1
    label["text"] = str(new_value)
    
    if new_value >= 5:
        button["text"] = "Maximum Reached"
        button["state"] = tk.DISABLED

# Create the main window
root = tk.Tk()
root.title("Label and Button Example")

# Create a label
label = tk.Label(root, text="0")
label.pack(padx=20, pady=10)

# Create a button
button = tk.Button(root, text="Increment", command=update_label)
button.pack(padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()
"""
"""import tkinter as tk

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    
    label = tk.Label(new_window, text="This is a new window!")
    label.pack(padx=20, pady=10)

# Create the main window
root = tk.Tk()
root.title("Main Window")

# Create a label in the main window
label_main = tk.Label(root, text="Main Window")
label_main.pack(padx=20, pady=10)

# Create a button to open a new window
button = tk.Button(root, text="Open New Window", command=open_new_window)
button.pack(padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()"""
"""import tkinter as tk

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.grab_set()  # Make the new window modal
    
    label = tk.Label(new_window, text="This is a new window!")
    label.pack(padx=20, pady=10)

# Create the main window
root = tk.Tk()
root.title("Main Window")

# Create a label in the main window
label_main = tk.Label(root, text="Main Window")
label_main.pack(padx=20, pady=10)

# Create a button to open a new window
button = tk.Button(root, text="Open New Window", command=open_new_window)
button.pack(padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()"""
"""import tkinter as tk

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")

    # Calculate the position for the new window relative to the main window
    x_offset = root.winfo_x() + 50  # Adjust the x-offset as needed
    y_offset = root.winfo_y() + 50  # Adjust the y-offset as needed
    new_window.geometry(f"+{x_offset}+{y_offset}")
    
    label = tk.Label(new_window, text="This is a new window!")
    label.pack(padx=20, pady=10)

# Create the main window
root = tk.Tk()
root.title("Main Window")

# Create a label in the main window
label_main = tk.Label(root, text="Main Window")
label_main.pack(padx=20, pady=10)

# Create a button to open a new window
button = tk.Button(root, text="Open New Window", command=open_new_window)
button.pack(padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()"""
"""import tkinter as tk
import random

# List of words
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
used_words = []

def change_label_text():
    if word_list:
        random_word = random.choice(word_list)
        used_words.append(random_word)
        word_list.remove(random_word)
        label["text"] = random_word
        if not word_list:
            button["state"] = tk.DISABLED

# Create the main window
root = tk.Tk()
root.title("Random Word Label Example")

# Create a label
label = tk.Label(root, text="Click the button to show a random word")
label.pack(padx=20, pady=10)

# Create a button
button = tk.Button(root, text="Generate Random Word", command=change_label_text)
button.pack(padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()"""
"""import tkinter as tk
import random

# List of words
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

def change_label_text():
    if word_list:
        random_word = random.choice(word_list)
        label["text"] = random_word
        word_list.remove(random_word)
        check_button_state()

def check_button_state():
    if label["text"] == "apple":
        button_apple["state"] = tk.DISABLED
    else:
        button_apple["state"] = tk.NORMAL

# Create the main window
root = tk.Tk()
root.title("Random Word Label Example")

# Create a label
label = tk.Label(root, text="Click the button to show a random word")
label.pack(padx=20, pady=10)

# Create a button to generate a random word
button_generate = tk.Button(root, text="Generate Random Word", command=change_label_text)
button_generate.pack(padx=20, pady=10)

# Create buttons for specific words
button_apple = tk.Button(root, text="Apple", state=tk.DISABLED)
button_apple.pack(padx=20, pady=10)

# Check button states initially
check_button_state()

# Run the Tkinter event loop
root.mainloop()"""
"""import tkinter as tk
import random

root = tk.Tk()
root.title("Spelling Game")

easy_spell_word_hint = ["btut", "apple", "grape", "banana"]  # Example word list
used_hints = []

def change_label():
    if easy_spell_word_hint:
        choose_word = random.choice(easy_spell_word_hint)
        used_hints.append(choose_word)
        label["text"] = choose_word
        easy_spell_word_hint.remove(choose_word)

def easygame():
    maingamelabel = tk.Label(text="Choose the correct spelling of the word!")
    maingamelabel.pack()

    if label["text"] == 'btut':
        W1 = tk.Button(text="bttu")
        W1.pack()
        W2 = tk.Button(text="tubt")
        W2.pack()
        C1 = tk.Button(text="butt")
        C1.pack()

    new_word_button = tk.Button(text="New Word", command=change_label)
    new_word_button.pack()

# Create a label initially with some default text
label = tk.Label(root, text="")
label.pack()

start_button = tk.Button(root, text="Start Easy Game", command=easygame)
start_button.pack()

root.mainloop()"""
"""import tkinter as tk
import random

root = tk.Tk()
root.title("Random Dictionary Key Check")

# Dictionary
my_dict = {
    "name": "John",
    "age": 25,
    "topic": "Programming",
    "city": "New York"
}

def check_key():
    key = random.choice(list(my_dict))
    label_key.config(text=f"Random Key: {key}")
    if key == 'name':
        label_result.config(text="Key is 'name': WOW!")
    else:
        label_result.config(text="Key is not 'name'")

# Create labels
label_key = tk.Label(root, text="", font=("Helvetica", 14))
label_key.pack(pady=10)

label_result = tk.Label(root, text="", font=("Helvetica", 16))
label_result.pack(pady=10)

# Button to check random key
button_check = tk.Button(root, text="Check Random Key", command=check_key)
button_check.pack(pady=10)

root.mainloop()"""
"""import tkinter as tk
import random

# Initialize the main tkinter window
ez = tk.Tk()
ez.title("Easy Game")

# Create the label
jumblelabel = tk.Label(ez, text="")
jumblelabel.pack()

# Define the easy_spell_words dictionary
easy_spell_words = {"btut": "butt", "trseh": "shirt", "wdoorr": "door", "hwon": "won"}

def actualgame():
    key = random.choice(list(easy_spell_words))
    jumblelabel.config(text=f"Write the correct word!: {key}")
    AnswerEntry = tk.Entry(ez, bd=5)
    AnswerEntry.pack()
    nextword.config(command=actualgame)  # Update the button's command

# Create the initial button
nextword = tk.Button(ez, text="Print word!", command=actualgame)
nextword.pack()

ez.mainloop()"""
"""import tkinter as tk
import random

# Initialize the main tkinter window
ez = tk.Tk()
ez.title("Easy Game")

# Create the label
jumblelabel = tk.Label(ez, text="")
jumblelabel.pack()

# Define the easy_spell_words dictionary
easy_spell_words = {"btut": "butt", "trseh": "shirt", "wdoorr": "door", "hwon": "won"}

# Create the Entry widget
AnswerEntry = tk.Entry(ez, bd=5)
AnswerEntry.grid(row=0, column=0, padx=10, pady=10)  # Adjust padx and pady as needed

def actualgame():
    key = random.choice(list(easy_spell_words))
    jumblelabel.config(text=f"Write the correct word!: {key}")

# Create the button
nextword = tk.Button(ez, text="Print word!", command=actualgame)
nextword.grid(row=1, column=0, padx=10, pady=10)  # Adjust padx and pady as needed

ez.mainloop()"""
"""import tkinter as tk
import random

# Initialize the main tkinter window
ez = tk.Tk()
ez.title("Easy Game")

# Create the label
jumblelabel = tk.Label(ez, text="")
jumblelabel.grid(row=0, column=0, padx=10, pady=10)  # Adjust padx and pady as needed

# Define the easy_spell_words dictionary
easy_spell_words = {"btut": "butt", "trseh": "shirt", "wdoorr": "door", "hwon": "won"}

def actualgame():
    key = random.choice(list(easy_spell_words))
    jumblelabel.config(text=f"Write the correct word!: {key}")

# Create the Entry widget
AnswerEntry = tk.Entry(ez, bd=5)
AnswerEntry.grid(row=1, column=0, padx=10, pady=10)  # Adjust padx and pady as needed

# Create the button
nextword = tk.Button(ez, text="Print word!", command=actualgame)
nextword.grid(row=2, column=0, padx=10, pady=10)  # Adjust padx and pady as needed

ez.mainloop()"""
"""import tkinter as tk
import random

# Dictionary of word pairs (scrambled word: unscrambled word)
word_dict = {
    "lpape": "apple",
    "aaanbn": "banana",
    "hcyerr": "cherry",
    "rgeap": "grape",
    "onrgae": "orange",
    "eytrsrbarw": "strawberry",
    "lmoenratwe": "watermelon"
}

def choose_random_word(word_dict):
    return random.choice(list(word_dict.keys()))

def next_word():
    global current_word, scrambled_word, correct_word
    scrambled_word = choose_random_word(word_dict)
    current_word = word_dict[scrambled_word]
    correct_word = current_word
    label.config(text=scrambled_word)
    entry.delete(0, tk.END)

def check_answer():
    user_answer = entry.get().lower()
    if user_answer == correct_word:
        label.config(text="Correct!")
    else:
        label.config(text="Incorrect. Try again: " + correct_word)

root = tk.Tk()
root.title("Word Unscramble Game")

current_word = ""
scrambled_word = ""
correct_word = ""

label = tk.Label(root, text="", font=("Helvetica", 24))
label.pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 18))
entry.pack(pady=10)

check_button = tk.Button(root, text="Check", command=check_answer)
check_button.pack()

next_button = tk.Button(root, text="Next Word", command=next_word)
next_button.pack()

next_word()

root.mainloop()"""
"""def checkanswer(user_input):
    # Assuming you have a dictionary named easy_spell_words_dict
    easy_spell_words_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

    user_answer = user_input.lower()

    for key, value in easy_spell_words_dict.items():
        if user_answer == key.lower() and user_answer == value.lower():
            print("wow jeff")
            return  # Exit the function if a match is found

    # If no match is found in the loop, print "sad"
    print("sad")

# Example usage:
user_input = input("Enter a value: ")
checkanswer(user_input)"""
"""import tkinter as tk
import random

easy_spell_words_dict = {
    "tebn": "bent",
    "bzzu": "buzz",
    # ... (other words)
    "ttse": "test",
    "darh": "hard",
    "ysea": "easy",
    "rohn": "horn"
}"""
"""AnswerEntry = None  # Define AnswerEntry as a global variable
current_key = None  # Keep track of the current key

def checkanswer(user_answer):
    global current_key
    user_answer = user_answer.lower()
    
    if current_key is not None:
        correct_value = easy_spell_words_dict.get(current_key, "").lower()
        
        if user_answer == correct_value:
            print("wow jeff")
        else:
            print("sad")
    else:
        print("No word to check")

def easygame():
    def actualgame():
        global AnswerEntry, current_key
        current_key = random.choice(list(easy_spell_words_dict))
        jumblelabel.config(text=f"Write the correct word!: {current_key}")
        if AnswerEntry:
            AnswerEntry.destroy()  # Destroy the previous Entry widget
        AnswerEntry = tk.Entry(ez, bd=5)
        AnswerEntry.grid(row=2, column=0, padx=5, pady=5)
        AnswerEntry.delete(0, tk.END)

    actualgame()
    wordbutton.config(text="Print (new) word!", command=actualgame)
    enterbutton = tk.Button(ez, text="Enter!", command=lambda: checkanswer(AnswerEntry.get()))
    enterbutton.grid(row=4, column=0, padx=3, pady=3)

# Create a Tkinter window
ez = tk.Tk()
ez.title("Easy Word Game")

# Create and configure labels and buttons
jumblelabel = tk.Label(ez, text="")
jumblelabel.grid(row=0, column=0, padx=5, pady=5)
wordbutton = tk.Button(ez, text="Print (new) word!", command=easygame)
wordbutton.grid(row=1, column=0, padx=5, pady=5)

# Start the game
easygame()

# Start the Tkinter main loop
ez.mainloop()"""
"""import tkinter as tk
import random

easy_spell_words_dict = {
    "paple": "apple",
    "banarna": "banana",
    "orngae": "orange",
    "grpae": "grape",
}

def checkanswer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("wow jeff")
    else:
        print("sad")

def actualgame():
    global printed_key, correct_answer  # Declare these as global variables
    printed_key = random.choice(list(easy_spell_words_dict))
    correct_answer = easy_spell_words_dict[printed_key]
    jumblelabel.config(text=f"Write the correct word!: {printed_key}")
    AnswerEntry.delete(0, tk.END)

def easygame():
    actualgame()
    wordbutton.config(text="Print (new) word!", command=actualgame)
    enterbutton = tk.Button(ez, text="Enter!", command=lambda: checkanswer(AnswerEntry.get().lower(), correct_answer))
    enterbutton.grid(row=4, column=0, padx=3, pady=3)

# Create the main tkinter window
ez = tk.Tk()
ez.title("Jumbled Word Game")

jumblelabel = tk.Label(ez, text="")
jumblelabel.grid(row=0, column=0, padx=5, pady=5)

wordbutton = tk.Button(ez, text="Start Game", command=easygame)
wordbutton.grid(row=1, column=0, padx=5, pady=5)

AnswerEntry = tk.Entry(ez, bd=5)
AnswerEntry.grid(row=2, column=0, padx=5, pady=5)

ez.mainloop()"""
"""from tkinter import Tk, Label

# Read the points from the file and convert them to integers
with open('userpoints.txt', 'r') as file:
    points = [int(line) for line in file.read().splitlines()]

end = Tk()
end.geometry('200x200')
end.configure(bg='#6693F5')
end.title("Spelling Bee's Spelling Game!")

endlabel = Label(text="You've finished easy mode!")
endlabel.grid(row=0, column=0, padx=5, pady=5)

# Calculate the total points earned
total_points = sum(points)

pointslabel = Label(text=f"You got {total_points} out of 10 points for easy mode!")
pointslabel.grid(row=1, column=0, padx=5, pady=5)

moti = Label(end, text="")
moti.grid(row=2, column=0, padx=5, pady=5)

if total_points < 5:
    moti.config(text="Better luck next time!")
elif total_points == 10:
    moti.config(text="WOAH, perfect score! Great job!")
else:
    moti.config(text="Good Job!")

end.mainloop()"""

"""import tkinter as tk

def limit_characters(event):
    # Get the current text in the Entry widget
    current_text = entry.get()
    
    # Define the maximum character limit
    max_characters = 10  # Change this to your desired character limit
    
    # Check if the current text exceeds the character limit
    if len(current_text) > max_characters:
        # Truncate the text to the maximum allowed characters
        entry.delete(max_characters, tk.END)

root = tk.Tk()
root.title("Character Limit Example")

# Create an Entry widget
entry = tk.Entry(root)
entry.pack(padx=10, pady=10)

# Bind the limit_characters function to the KeyRelease event
entry.bind("<KeyRelease>", limit_characters)

root.mainloop()"""

"""from tkinter import *

def display_scores():
    with open('easyscore.txt', 'r') as file:
        scores = file.read().splitlines()

    for i, score in enumerate(scores):
        name, points = score.split(', ')
        name_label = Label(end, text=f"Name: {name}")
        name_label.grid(row=i+1, column=0, padx=5, pady=5)
        points_label = Label(end, text=f"Points: {points}")
        points_label.grid(row=i+1, column=1, padx=5, pady=5)
        

end = Tk()
end.geometry('300x300')
end.configure(bg='#6693F5')
end.title("Spelling Bee's Spelling Game!")

display_scores_button = Button(end, text="Display Scores", command=display_scores)
display_scores_button.grid(row=0, column=0, padx=5, pady=5)

end.mainloop()"""

"""import tkinter as tk

def hide_top_label():
    top_label.pack_forget()

root = tk.Tk()
root.title("Label Overlay Example")

# Create the bottom label
bottom_label = tk.Label(root, text="This is the bottom label")
bottom_label.pack(pady=20)

# Create the top label
top_label = tk.Label(root, text="This label will appear over the bottom label")
top_label.pack(pady=20)

# Schedule the hide_top_label function to be called after 2000 milliseconds (2 seconds)
root.after(2000, hide_top_label)

root.mainloop()"""

"""import tkinter as tk
import random

def on_button_click():
    # Draw sparkles on the canvas
    for _ in range(10):
        x = random.randint(0, 200)
        y = random.randint(0, 200)
        canvas.create_oval(x, y, x + 5, y + 5, fill="yellow", outline="yellow")

root = tk.Tk()
root.title("Button with Sparkles")

# Create a canvas
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack(pady=10)

# Create a button
button = tk.Button(root, text="Press Me", command=on_button_click)
button.pack()

root.mainloop()"""

"""import tkinter as tk

def validate_input(char):
    # Check if the character is a valid string character
    return char.isalpha() or char == ""

root = tk.Tk()
root.title("String Entry Example")

validate_cmd = root.register(validate_input)

entry = tk.Entry(root, validate="key", validatecommand=(validate_cmd, "%S"))
entry.pack(padx=10, pady=10)

root.mainloop()"""

"""import tkinter as tk

def show_top_window():
    top_window = tk.Toplevel(root)
    top_window.title("Top Window")
    top_window.geometry("300x150")

    # Make the top window modal (user can't interact with the root window until this is closed)
    top_window.transient(root)
    top_window.grab_set()

    # Add content to the top window
    label = tk.Label(top_window, text="This is the top window")
    label.pack(padx=20, pady=20)

    # Add a button to close the top window and enable interaction with the root window
    close_button = tk.Button(top_window, text="Close", command=lambda: close_top_window(top_window))
    close_button.pack(pady=10)

def close_top_window(top_window):
    # Release the grab, allowing interaction with the root window
    top_window.grab_release()

    # Close the top window
    top_window.destroy()

root = tk.Tk()
root.title("Main Window")
root.geometry("400x200")

# Add a button to show the top window
show_button = tk.Button(root, text="Show Top Window", command=show_top_window)
show_button.pack(pady=20)

root.mainloop()"""

"""import tkinter as tk

window = tk.Tk()

# Load the animated GIF directly
gif_path = "beeidlegif.gif"
animated_gif = tk.PhotoImage(file=gif_path)

# Create a label to display the GIF
label = tk.Label(window, image=animated_gif)
label.grid(row=5, column=0, padx=3, pady=3)

window.mainloop()"""

"""import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

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

# Start the Tkinter main loop
root.mainloop()




#My easyspell code
import sys 
from tkinter import *
import tkinter as tk
import random
from UserRegandLog import playing_user, Labels, Buttons
from PIL import Image, ImageTk
from tkinter import Label, Tk
easy_spell_word_hint = ["btut", "bzzu", "ogod", "tars", "labl", "alfl", "chea", "anme", "ctih", "rogw", "etre", "mila", "wrad", "leyl", "meit", "sahd", "chsa", "eadd", "nabg", "urde", "siks", "ribd", "avse", "orpe", "uleg", "uphs", "ulpl", "stre", "yter", "ewts", "stea", "ongs", "sevt", "kics", "eken", "ttse", "darh", "ysea", "rohn"]

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
label = None
userpoints = 0
level = 0
gamestartpoint = 0
#words for hints (in order): butt, buzz, good, star, ball, fall, ache, name, itch, grow, tree, nose, mail, draw, yell, time, dash, cash, dead, bang, rude, kiss, bird, vase, rope, glue, push, pull, rest, tyre, west, east, song, vest, sick, knee, test, hard, easy, horn - 40 words (unjumbled words)

def change_label():
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
            quit()


def validate_input(typed_char):
    return typed_char.isalpha() or typed_char == ""


def end():
    easy.destroy()
    import EndScreen
    EndScreen


def checkanswer():
    global userpoints, label
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

    else:
        easy.geometry("520x400")
        answerlabel.config(text=f"INCORRECT! The answer was {correct_answer}!")




def actualgame():
    easy.geometry("520x230")
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
                    image = Image.open("beegoodjobyes.png")
                    photo = ImageTk.PhotoImage(image)
                    label = tk.Label(image=photo)
                    easy.update_idletasks()
                    label.grid(row=7, column=0, padx=5, pady=5)
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
    Q1label = tk.Label(text="Please pick the correct spelling of [insert thing here]")
    Q1label.pack()
    Q1CB = Buttons(easy, text="paw")
    Q1CB.pack()
    Q1INCB1 = Buttons(text="liw")
    Q1INCB1.pack()
    Q1INCB2 = Buttons(text="pey")
    Q1INCB2.pack()


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
    easy.mainloop()"""


"""label_answer_test = Labels(easy, text="")
label_answer_test.grid(row=1, column=0, padx=5, pady=5)"""

"""import tkinter as tk

def flash_window(window, flash_count):
    for _ in range(flash_count):
        window.iconify()  # Hide the window
        window.update_idletasks()
        window.after(200)  # Adjust the duration of the flash (in milliseconds)
        window.deiconify()  # Show the window
        window.update_idletasks()
        window.after(200)

def button_pressed():
    flash_window(top, 1)

# Create the main window
top = tk.Tk()

# Create a button to trigger the flashing effect
button = tk.Button(top, text="Flash Window", command=button_pressed)
button.pack(pady=20)

# Run the Tkinter event loop
top.mainloop()"""

"""import tkinter as tk

def create_window():
    if not hasattr(create_window, 'top') or not create_window.top.winfo_exists():
        create_window.top = tk.Toplevel()
        label = tk.Label(create_window.top, text="New Window")
        label.pack()

# Create the main window
top = tk.Tk()

# Create a button to create a new window
button = tk.Button(top, text="Create Window", command=create_window)
button.pack(pady=20)

# Run the Tkinter event loop
top.mainloop()"""

"""import tkinter as tk
import ctypes

# Constants from the Windows API
GWL_STYLE = -16
WS_CAPTION = 0x00C00000

def disable_dragging(window):
    hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
    style = ctypes.windll.user32.GetWindowLongPtrW(hwnd, GWL_STYLE)
    style = style & ~WS_CAPTION
    ctypes.windll.user32.SetWindowLongPtrW(hwnd, GWL_STYLE, style)

root = tk.Tk()
root.title("Non-draggable Window")

# Your window content here...

# Call disable_dragging after the window is created
root.after(1, lambda: disable_dragging(root))

root.mainloop()"""


import subprocess
import sys
import time

def main():
    while True:
        print("Program is running...")
        time.sleep(1)

if __name__ == "__main__":
    subprocess.Popen([sys.executable, sys.argv[0]])

    try:
        main()
    except SystemExit:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Program has exited.")