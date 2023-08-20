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
    
    
