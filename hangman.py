import random

print("H A N G M A N")

word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)

letters_list = ["-"] * len(word)

for i in range(8):

	# if "-" not in letters_list:
		# break
	print("")
	for let in letters_list:
		print(let, end="")

	user_guess = input("\nInput a letter: ")

	if user_guess not in word:
		print("No such letter in the word")
	else:
		temp_list = []
		for m in range(len(word)):
			if word[m] == user_guess:
				temp_list.append(m)
		for x in range(len(temp_list)):
			letters_list[temp_list[x]] = user_guess

print("""\nThanks for playing!
We'll see how well you did in the next stage""")

