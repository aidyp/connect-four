import requests
import random
import os

def pick_word():
	'''
	This function returns a word for hangman
	'''
	#Not sure how to make the filepath work properly
	script_dir = os.path.dirname(__file__)
	rel_path = "disk/hangman_words.txt"
	filepath = os.path.join(script_dir, rel_path)
	#Inefficient for now, but it will do for files of a reasonable size
	lines = open(filepath).read().splitlines()
	word = random.choice(lines)
	return word
	return

def init_count(word):
	'''
	Returns the number of guesses allowed for the word
	'''
	return 5

def initialise_state(word):
		state = ['*'] * len(word)
		return state



class hangman:

	def __init__(self):
		self.word = pick_word()
		self.state = initialise_state(self.word)

	def get_state(self):
		return self.state

	def update_state(self, letter, indices):
		'''
		Changes the state to the include the letter
		'''
		for i in range(0, len(indices)):
			insert_point = indices[i]
			self.state[insert_point] = letter

	def guess_letter(self, letter_guess):
		'''
		Checks to see if the guessed letter is in the word
		'''

		indices = []
		for i in range(0, len(self.word)):
			if self.word[i] == letter_guess:
				indices.append(i)

		return indices

	def guess(self):
		'''
		Takes a guess, and returns if it's successful
		'''
		guess = input("Guess a letter: ")
		guessed_letters = self.guess_letter(guess)

		if len(guessed_letters) > 0:
			self.update_state(guess, guessed_letters)
			return 1

		return 0

	def start_game(self):
		print("The word is " + str(len(self.word)) + " letters long")
		self.print_state()

	def check_win(self):
		'''
		Check if someone has won the game
		'''
		for elem in self.state:
			if elem == '*':
				return 0
		return 1

	def print_state(self):
		'''
		Prints the current state of hangman
		'''
		to_print = ""

		for elem in self.state:
			if elem == '*':
				to_print = to_print + "_ "
			else:
				to_print = to_print + elem + " "

		print(to_print)




def play():
	'''
	Plays hangman
	'''

	new_game = hangman()
	max_guesses = 5
	count = 0
	new_game.start_game()
	while count < max_guesses:
		if new_game.guess() == 0:
			count += 1
		new_game.print_state()
		if new_game.check_win() == 1:
			print("You won!")
			return
	print("You lose!")

if __name__ == '__main__':
	play()
