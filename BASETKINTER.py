import tkinter as tk

window = tk.Tk()
window.title("Spelling Bee Spelling Game")
window.geometry("300x300")

hello = tk.Label(text="Welcome to the Spelling Bee Spelling Game!")
hello.pack()
button = tk.Button(text="Test Button")
button.pack()
 
tk.mainloop()