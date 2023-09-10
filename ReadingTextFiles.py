"""names = open('names.txt', 'r')
names = names.read()
name_list = names.split()
print(name_list)

names = open('names.txt', 'a')

print("what your name")
inputname = input()

names.write(inputname)
print(names)"""

#Take input from user and assign it to variables
"""print("What is your first name?")
input1 = input()
print("What is your last name?")
input2 = input()
 
#Open the text.txt file for appending.
 
file1 = open('text.txt', 'a')
 
#Write the content of the variables to the text.txt file
file1.write(input1)
file1.write(" ")
file1.write(input2)
file1.write("\n")
 
#Close the text.txt file
file1.close()"""

"""print("Please create a username\n>> ")
user = input()
file = open('username.txt', 'a')
file.write(user)"""



#Trying code from YouTube video
"""def reg():
    db = open('names.txt', 'r')
    username = input("Please create a username")
    score = input("what is your score")
    u = []
    s = []
    for i in db:
        us, sc = i.split(", ")
        sc = sc.strip()
        u.append(us)
        s.append(sc)
        data = dict(zip(u, s))
        print(data)

reg()"""

#stackoverflow
"""def Register():
    print("Hello! You need to register an account before you can begin")
    username = input("Please enter a username: ")
    password = input("Now please enter a password: ")
    file = open("Login.txt","a")
    file.write (username)
    file.write (",")
    file.write (password)
    file.write("\n")
    file.close()
    print ("Your login details have been saved. ")
    print("You will now need to login")
    Login() 

def Login():
    print("Please enter your details to log in")
    username1 = input("Please enter your username: ")
    password1 = input("Please enter your password: ")

    file = open("Login.txt","r")

    for row in file:
        field = row.split(",")
        username = field[0]
        password = field[1]
        lastchar = len(password)-1
        password = password[0:lastchar]

    if username1 == username and password1 == password:
        print("Hello",username)

    else:

#file.close()


user=input("Are you already a user? ")

if user == "Yes":
         Login()
    
elif user =="No":
         Register()
    
print("Welcome to our game")"""

"""#ChatGPT help
def reg():
    username = input("Please create a username: ")
    with open('username.txt', 'a') as file:
        file.write(username + "\n")
    print("Your username has been saved")
    login()

def login():
    with open('username.txt', 'r') as file:
        usernames = [line.strip() for line in file.readlines()]
    print("Usernames in the file:", usernames)
    userlogin = input("Enter your username: ")
    userlogin = userlogin.strip()
    if userlogin in usernames:
        print("Welcome")
    else:
        print("This username does not exist")


def question():
    ask = input("reg or login: ")
    if ask == 'reg':
        reg()
    elif ask == 'login':
        login()
    else:
        print("Invalid choice")
        question()

question()"""



"""import tkinter as tk

def save():
    a = t.get()
    f = open((a + '.txt'), 'w')
    f.write(a)
    f.close()
    return

top = tk.Tk()
t = tk.StringVar()
e = tk.Entry(top, textvariable = t)
e.pack()
b = tk.Button(top, text = 'Save as a file', command = save)
b.pack()
top.mainloop()"""

    

"""import sys 
from tkinter import *
import tkinter as tk
def saveuser():
    usernames = E2.get()
    with open('username.txt', 'a') as useropen:
        useropen.write(usernames + "\n")

test = Tk()
test.geometry("330x130")
test.configure (bg = '#6693F5')
test.title("Spelling Bee's Spelling Game!")
word = Label(test, text="Please create a username")
word.pack()
E2 = Entry(test, bd = 5)
E2.pack()
savebutton = tk.Button(text="Save", command=saveuser)
savebutton.pack()"""

"""with open("username.txt", "r") as file:
    # Initialize a variable to store the last line
    last_line = None

    # Read the file line by line
    for line in file:
        last_line = line  # Overwrite the variable with the current line

# Now, last_line contains the final line of the file
print("Final line:", last_line)"""

import tkinter as tk

# Function to update the score in the text file
def update_score():
    # Get the username and new score from the Entry widgets
    username = username_entry.get()
    new_score = score_entry.get()

    # Read the existing data from the file into a list
    with open("scores.txt", "r") as file:
        lines = file.readlines()

    # Iterate through the lines to find and update the specific username
    for i, line in enumerate(lines):
        parts = line.strip().split(',')
        if parts[0] == username:
            lines[i] = f"{username},{new_score}\n"
            break  # Stop searching once the username is found and updated

    # Write the modified lines back to the file
    with open("scores.txt", "w") as file:
        file.writelines(lines)

    # Optionally, update a label or provide feedback to the user
    result_label.config(text=f"Score for {username} updated to {new_score}")

# Create a tkinter window
root = tk.Tk()
root.title("Update Score")

# Create Entry widgets for username and score
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

score_label = tk.Label(root, text="New Score:")
score_label.pack()
score_entry = tk.Entry(root)
score_entry.pack()

# Create a button to update the score
update_button = tk.Button(root, text="Update Score", command=update_score)
update_button.pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()