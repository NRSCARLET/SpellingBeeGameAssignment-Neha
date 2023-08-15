"""import random

my_dict = {
    'name': 'Borislav Hadzhiev',
    'fruit': 'apple',
    'number': 5,
    'website': 'bobbyhadz.com',
    'topic': 'Python'
}


# ✅ get random key-value pair from dictionary
key, value = random.choice(list(my_dict.items()))
print(key, value)  # 👉️ name Borislav Hadzhiev

# -----------------------------------------------

# ✅ get random key from dictionary
key = random.choice(list(my_dict))
print(key)  # 👉️ topic

# -----------------------------------------------

# ✅ get random value from dictionary
value = random.choice(list(my_dict.values()))
print(value)  # 👉️ bobbyhadz.com"""


import random

my_dict = {
    'name': 'Borislav Hadzhiev',
    'fruit': 'apple',
    'number': 5,
    'website': 'bobbyhadz.com',
    'topic': 'Python'
}

key = random.choice(list(my_dict))
print(key)  # 👉️ topic
if key == 'name':
    print("wow")

"""import random
lst = ['WHO','YOU','THINK','ARE']
random.shuffle(lst)
for x in lst:
   print (x)"""

"""WORDS = ("YOU","ARE","WHO","THINK")
for word in WORDS:
    newword=random.choice(WORDS)
    while newword==word is False:
          newword=random.choice(WORDS)
          word=newword
          print(word)"""
