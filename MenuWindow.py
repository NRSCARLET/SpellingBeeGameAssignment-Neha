from tkinter import *
import tkinter as tk
from os import system, name
from time import sleep
from UserRegandLog import Labels, Buttons
from PIL import Image, ImageTk, ImageSequence
from tkinter import Label, Tk
is_menu_closing = False
instructionwindow_open = False
playing_user = ""
def clear():
    """This definition is to add a mechanism to clear the screan."""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def nox():
    pass


def register():
    window.after_cancel(update_image)
    window.destroy()
    import UserRegandLog
    UserRegandLog.regwindow()


def login():
    window.destroy()
    import UserRegandLog
    UserRegandLog.logwindow()


def exit():
    window.destroy()
    import EndScreen
    EndScreen.endgame()


"""Got this code from ChatGPT. I got stuck trying to find out how to animate my gif (I only managed to insert it as a static image)"""
def update_image():
    global gif_frames_iter, gif_frames
    try:
        # Get the next frame from the GIF
        current_frame = next(gif_frames_iter)

        # Convert the PIL image to a Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(current_frame)

        # Update the label with the new image
        label.config(image=tk_image)
        label.image = tk_image  # This line is crucial for proper garbage collection
        window.after(50, update_image)  # Schedule the update after 100 milliseconds (adjust as needed)
    except StopIteration:
        # If we reach the end of the frames, restart the animation
        gif_frames_iter = iter(gif_frames_resized)
        window.after(100, update_image) # Schedule the update after 100 milliseconds (adjust as needed)
        # Open the GIF file


def resize_gif(gif_frames, new_width, new_height):
    # Resize each frame in the GIF
    resized_frames = [frame.resize((new_width, new_height)) for frame in gif_frames]
    return resized_frames


def closeinstructions():
    global instructionwindow_open
    instructionwindow.destroy()
    instructionwindow_open = False
    pass


def instructions():
    global instructionwindow_open, instructionwindow
    if not instructionwindow_open:
        instructionwindow_open = True
        instructionwindow = tk.Toplevel(window)
        instructionwindow.title("Spelling Bee's Spelling Game!")
        instructionwindow.geometry("600x290")
        instructionwindow.configure(bg ='#b4aaf9')
        instructionwindow.transient(window)
        instructionwindow.protocol("WM_DELETE_WINDOW", nox)
        instructionwindow.grab_set()
        instructionwindow.overrideredirect(1)
        instrctlabel = Label(instructionwindow, text="Game overview:\n>Easy mode: 10 levels, words have 4 letters each\n>Medium mode: 10 levels, words have 5 letters each\nHard mode: 10 levels, words have 6-7 letters each\nHow to play:\n>Register (or log in if you're an existing user)\n>Pick a difficulty (easy, medium, hard)\n>unscramble the word! Based on the letters that appear,\nenter the correct word into the text box!\nGetting the answer correct will reward you with 1 point.\n>Repeat for 10 levels.\n>Once you finish the final level, you will be presented with your score.\n>Play again or exit!\n>Most importantly: HAVE FUN!!", bg='#b4aaf9', fg='#2A0134', font='helvetica 10 bold')
        instrctlabel.grid(row=0, column=0, padx=5, pady=5)
        closebutton = Buttons(instructionwindow, text="Close", command = closeinstructions)
        closebutton.grid(row=1, column=0, padx=3, pady=3)


def menu_wind():
    global window, gif_frames_iter, label, gif_frames, gif_frames_resized
    window = tk.Tk()
    window.configure (bg = '#6693F5')
    window.title("Spelling Bee's Spelling Game!")
    window.geometry("400x350")
    hello = Labels(text="Welcome to Spelling Bee's Spelling Game!")
    hello.grid(row=0, column=0, padx=3, pady=5)
    b1 = Buttons(text="Register (new user)", command=register)
    b1.grid(row=2, column=0, padx=3, pady=3)
    b2 = Buttons(text="Login (old user)", command=login)
    b2.grid(row=3, column=0, padx=3, pady=3)
    b3 = Buttons(text="Exit Game", command=exit)
    b3.grid(row=4, column=0, padx=3, pady=3)
    window.overrideredirect(1)
    instructbutton = Buttons(text="?", command=instructions)
    instructbutton.grid(row=0, column=1, padx=3, pady=3)
    gif_path = "beeidlegif.gif"
    gif = Image.open(gif_path)
    # Extract individual frames from the GIF
    gif_frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]
    # Resize the frames
    new_width = 200  # Set the desired width
    new_height = 150  # Set the desired height
    gif_frames_resized = resize_gif(gif_frames, new_width, new_height)
    # Create an iterator to loop through the frames
    gif_frames_iter = iter(gif_frames_resized)

    # Display the initial frame
    initial_frame = next(gif_frames_iter)
    initial_frame_tk = ImageTk.PhotoImage(initial_frame)
    label = tk.Label(window, image=initial_frame_tk)
    label.grid(row=5, column=0, padx=5, pady=5)

    # Schedule the update function to animate the GIF
    window.after(50, update_image)
    tk.mainloop()
menu_wind()