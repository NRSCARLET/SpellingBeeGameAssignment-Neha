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

import tkinter as tk

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
root.mainloop()





