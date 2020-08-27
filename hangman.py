import random
from string import ascii_lowercase

print("H A N G M A N")

word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)

letters_list = ["-"] * len(word)
lives = 8
guessed_letters = set()
wrong_letters = set()

while lives != 0:

	print("")
	for let in letters_list:
		print(let, end="")

	if "-" not in letters_list:
		print("""\nYou guessed the word!
You survived!""")
		break

	user_guess = input("\nInput a letter: ")

	if len(user_guess) != 1:
		print("You should input a single letter")
		continue

	if user_guess not in ascii_lowercase:
		print("It is not an ASCII lowercase letter")
		continue

	if user_guess not in word:
		if user_guess in wrong_letters:
			print("You already typed this letter")
		else:
			print("No such letter in the word")
			lives -= 1
			wrong_letters.add(user_guess)

	else:

		temp_list = []
		for m in range(len(word)):
			if word[m] == user_guess:
				temp_list.append(m)

		for x in range(len(temp_list)):
			letters_list[temp_list[x]] = user_guess
		if user_guess in guessed_letters:
			print("You already typed this letter")
		guessed_letters.add(user_guess)

if lives == 0:
	print("You are hanged!")
