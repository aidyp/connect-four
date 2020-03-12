import requests


def pick_word():
	'''
	This function returns a word for hangman
	'''
	
	words = ['cryptography']
	return words[0]

def init_count(word):
	'''
	Returns the number of guesses allowed for the word
	'''
	return 5

def check_win(state):
	'''
	Check if someone has won the game
	'''
	for elem in state:
		if elem == '*':
			return 0
	return 1

def start_game(word, state):
	print("The word is " + str(len(word)) + " letters long")
	print_state(state)	

def print_state(state):
	'''
	Prints the current state of hangman
	'''
	to_print = ""
	
	for elem in state:
		if elem == '*':
			to_print = to_print + "_ "
		else:
			to_print = to_print + elem + " "
	
	print(to_print)
	

def update_state(state, letter, indices):
	'''
	Changes the state to the include the letter
	'''
	for i in range(0, len(indices)):
		insert_point = indices[i]
		state[insert_point] = letter
		


def guess_letter(word, letter_guess):
	'''
	Checks to see if the guessed letter is in the word
	'''
	
	indices = []
	for i in range(0, len(word)):
		if word[i] == letter_guess:
			indices.append(i)
	
	return indices

def guess(word, state):
	'''
	Takes a guess, and returns if it's successful
	'''
	guess = input("Guess a letter: ")
	guessed_letters = guess_letter(word, guess)
	
	if len(guessed_letters) > 0:
		update_state(state, guess, guessed_letters)
		return 1
	
	return 0
	


def play():
	'''
	Plays hangman
	'''
	
	word = pick_word()
	max_guesses = init_count(word)
	state = initialise_state(word)
	count = 0
	start_game(word, state)
	while count < max_guesses:
		if guess(word, state) == 0:
			count += 1
		print_state(state)
		if check_win(state) == 1:
			print("You won!")
			return
	print("You lose!")

play()


class hangman:
	
	def __init__(self):
		self.word = pick_word()
		self.state = initialise_state()	
	
	def initialise_state(self):
		self.state = ['*'] * len(word)
	
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
	
	def get_state(self):
		return self.state
