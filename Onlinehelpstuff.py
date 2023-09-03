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

import tkinter as tk
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

ez.mainloop()