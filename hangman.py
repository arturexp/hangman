import random

print("H A N G M A N")

word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)
word_input = input("Guess the word: ")

print("You survived!" if word == word_input else "You are hanged!")
