import random

# picks random word from words.txt file randomly
lines = open('words.txt').read().splitlines()
pick = random.choice(lines)
word = pick.lstrip()

# number of lives to start
lives = 6

# create list to hold guessed words
guess = []

# makes a list of underscores for the guess
for letters in word:
	guess.append("_ ") 

#prints guess so player can see how many letters
print ''.join(guess)

# will play the game while player still has lives
while lives > 0:
	print "Guess a letter"
	letter = raw_input()

	i = 0
	# if they get a letter wrong, dock one life, print lives left
	if letter in word:
		print "You got one!"
	else:
		print "Not in word. You lose a life!"
		lives = lives - 1
		print "Your remaining lives: %s" % lives

	# if lives is 0, the player lost
	if lives == 0:
		print "You Lost! Bummer!"
		print "The word was %s" % word

	# if they didn't lose, check each letter of word against their guess
	# if it's right, put it in guess in the correct space
	while i < len(word):
		if letter == word[i]:
			guess[i] = word[i]
			i = i + 1
		else:
			i = i + 1
	
	# if there are still free spaces and player has lives, keep playing
	if "_ " in guess:
		print ''.join(guess)
	# if no free spaces and lives left, player wins	
	else:
		print "You won the game!!"
		print ''.join(guess)
		break

