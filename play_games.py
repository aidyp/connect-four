import game_shelf.connect4 as c4
import game_shelf.hangman as hm





if __name__ == '__main__':
		choice = input("What do you want to play, Connect4 (1) or Hangman (2): ")
		if int(choice) == 1:
			c4.play()
		elif int(choice) == 2:
			hm.play()
		else:
			print("Wrong choice")
