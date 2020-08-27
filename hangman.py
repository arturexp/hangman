import random

print("H A N G M A N")

word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)  

letters_list = ["-"] * len(word)
lives = 8
guessed_letters = set()
while lives != 0:

	print("")
	for let in letters_list:  
		print(let, end="")

	if "-" not in letters_list:
		print("""\nYou guessed the word!
You survived!""")
		break

	user_guess = input("\nInput a letter: ")

	if user_guess not in word:
		print("No such letter in the word")
		lives -= 1
	else:

		if user_guess in guessed_letters:
			print("No improvements")
			lives -= 1

		temp_list = []
		for m in range(len(word)):
			if word[m] == user_guess:
				temp_list.append(m)
		for x in range(len(temp_list)):
			letters_list[temp_list[x]] = user_guess

		guessed_letters.add(user_guess)

if lives == 0:
	print("You are hanged!")


