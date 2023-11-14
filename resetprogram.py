import subprocess
import tkinter as tk
from UserRegandLog import Labels, Buttons



def relaunch():
    window.destroy()
    python_script = "MenuWindow.py"
    subprocess.run(["python", python_script])


def update_label():
    global current_index
    loading.config(text=text[:current_index + 1])
    current_index += 1
    if current_index < len(text):
        window.after(100, update_label)
    else:
        # After the animation is complete, wait for some time and then relaunch
        window.after(1000, relaunch)


def RP():
    global window, loading, text, current_index
    try:
        raise SystemExit
    except SystemExit:
        window = tk.Tk()
        window.title("Spelling Bee Spelling Game")
        window.geometry("230x50")
        window.configure (bg = '#6693F5')
        window.overrideredirect(1)
        loading = Labels(text="")
        text = "Loading... Please wait..."
        loading.grid(row=2, column=0, padx=5, pady=5)
        current_index = 0
        window.after(100, update_label)
        tk.mainloop()

RP()