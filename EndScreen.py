#not using, will put an end screen at the end of each game in the same file.
import sys 
from tkinter import *
import tkinter as tk
import random
from UserRegandLog import Labels, Buttons
from PIL import Image, ImageTk, ImageSequence
from tkinter import Label, Tk
"""def menu():
    import exitscreen
    Exitscreen
"""
def playagain():
    end.destroy()
    import resetprogram
    resetprogram.RP()


def update_image():
    global end, gif_frames_iter, gif_frames
    try:
        current_frame = next(gif_frames_iter)
        tk_image = ImageTk.PhotoImage(current_frame)
        label.config(image=tk_image)
        label.image = tk_image
        end.after(50, update_image)
    except StopIteration:
        gif_frames_iter = iter(gif_frames_resized)
        end.after(100, update_image)


def resize_gif(gif_frames, new_width, new_height):
    resized_frames = [frame.resize((new_width, new_height)) for frame in gif_frames]
    return resized_frames


def endgame():
    global gif_frames_iter, label, gif_frames, gif_frames_resized
    end.geometry("500x220")
    endlabel.destroy()
    notelabel.destroy()
    menub.destroy()
    difficultyb.destroy()
    ty = Labels(end, text="Thank you for playing! See you later!\nPlease press the 'x' at the top right of the window to close it.")
    ty.grid(row=0, column=0, padx=5, pady=5)
    gif_path = "beebyebye.gif"
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
    label = tk.Label(end, image=initial_frame_tk)
    label.grid(row=5, column=0, padx=5, pady=5)

    # Schedule the update function to animate the GIF
    end.after(50, update_image)


def endwindow():
    global endlabel, notelabel, menub, difficultyb, end
    end = Tk()
    end.geometry('640x200')
    end.configure(bg = '#6693F5')
    end.title("Spelling Bee's Spelling Game!")
    endlabel = Labels(text="You've completed the Spelling Bee Spelling Game!")
    endlabel.grid(row=0, column=0, padx=5, pady=5)
    notelabel = Labels(end, text="Note: Pressing the 'Play Again' button will take you back to the menu screen.\nPressing the 'End Game' button will end the game.")
    notelabel.grid(row=1, column=0, padx=5, pady=5)
    menub = Buttons(text="End Game", command=endgame)
    menub.grid(row=3, column=0, padx=3, pady=3)
    difficultyb = Buttons(text="Play Again", command=playagain)
    difficultyb.grid(row=4, column=0, padx=3, pady=3)
    tk.mainloop()
endwindow()

