import sys 
from tkinter import *
import tkinter as tk
import random

class Buttons(Button):
    def __init__(self,*args, **kwargs):
        Button.__init__(self,*args, **kwargs)
        self['bg'] = '#DA70D6'
        self['fg'] = 'white'
        self['font'] = 'helvetica 9 bold'

class Labels(Label):
    def __init__ (self, *args, **kwargs):
        Label.__init__(self, **kwargs)
        self['bg'] = '#6693F5'
        self['fg'] = 'purple'
        self['font'] = 'helvetica 10 bold'


end = Tk()
end.geometry('200x200')
end.configure(bg = '#6693F5')
end.title("Spelling Bee's Spelling Game!")
endlabel = Labels(text="You've finished easy mode!")
endlabel.grid(row=0, column=0, padx=5, pady=5)