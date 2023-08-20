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

#ChatGPT help
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

question()

"""Changes made:

Used the with statement to properly open and close files, ensuring proper resource management.
Read the lines from the file and stored them in the usernames list for comparison.
Removed leading and trailing whitespace from the entered username using the strip() method.
Changed the comparison to check if the entered username is in the list of usernames.
Now the code should work as expected, allowing users to register and log in with their usernames."""






    

