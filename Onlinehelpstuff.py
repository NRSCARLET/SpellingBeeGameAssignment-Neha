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

# Open the file in read mode
with open('userpoints.txt', 'r') as file:
    lines = file.read().splitlines()

# Check if there are any lines in the file
if lines:
    # Extract the last line (the last number)
    last_line = lines[-1]

    # Convert the last line to an integer (assuming it contains a number)
    last_number = int(last_line)

    # Use last_number as needed
    print("Last number:", last_number)
else:
    # Handle the case where the file is empty
    print("File is empty.")
