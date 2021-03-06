"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                      
"""

#!/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5 python3
from random import *

player_score = 0
computer_score = 0
bDebugging = True

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def hangingman(hangman):
	HANGMANPICS = ['''
	  +---+
	  |   |
	      |
	      |
	      |
	      |
	=========''', '''
	  +---+
	  |   |
	  O   |
	      |
	      |
	      |
	=========''', '''
	  +---+
	  |   |
	  O   |
	  |   |
	      |
	      |
	=========''', '''
	  +---+
	  |   |
	  O   |
	 /|   |
	      |
	      |
	=========''', '''
	  +---+
	  |   |
	  O   |
	 /|\  |
	      |
	      |
	=========''', '''
	  +---+
	  |   |
	  O   |
	 /|\  |
	 /    |
	      |
	=========''', '''
	  +---+
	  |   |
	  O   |
	 /|\  |
	 / \  |
	      |
	=========''', '''
	  +---+
	      |
	      |
	  O   |
	 /|\  |
	 / \  |
	=========''', '''
	  +---+
	      |
              |
              |
         \__/ |
         / / 0|
	=========''']
	print (HANGMANPICS[hangman])
	return

class Hangman:
	def __init__(self,words):
		self.dictionary = ["hat","capital","rainbow","penguin","house","snake"]
		self.word = choice(words)
		self.word_length = len(word)
		self.hint = choice(word)
		self.clue = word_length * ["_"]
		self.tries = 7
		self.letters_tried = ""
		self.guesses = 0
		self.letters_right = 0
		self.letters_wrong = 0
		self.asked = 0
		global computer_score, player_score

	def start(self):
		print ("Lets play a game of Hangman.")
		while game():
			pass
		scores()

	def game(self):
		
		print ("Your word is",word_length,"letters in length!") 
		print (" ".join(clue))

		while (letters_wrong != tries) and ("".join(clue) != word):
			if (bDebugging):
				print ("Debugging--- tries is", tries, "and the len of letters_wrong is", letters_wrong)
			letter = guess_letter()
			if len(letter) == 1 and letter.isalpha():
				if letters_tried.find(letter) != -1:
					print ("You've already picked ", letter)
				else:
					letters_tried = letters_tried + letter
					first_index = word.find(letter)
					if first_index == -1:
						letters_wrong += 1
						print ("Sorry,",letter,"isn’t what we’re looking for.")
					else:
						print ("Congratulations,",letter,"is correct.")
						for i in range(word_length):
							if letter == word[i]:
								clue[i] = letter
			else:
				print ("Choose another.")

			hangingman(letters_wrong)
			print (" ".join(clue))
			print ("You have had ",len(letters_tried)," guesses - They are: ", letters_tried)
			if (len(letters_tried) == 3) and (asked != 1):
				ask = input("Do you want a hint: y/n")
				if ask in ("y", "Y", "Yes", "yes", "Of course"):
					asked = 1
					print ("Your hint is letter ", hint)
					for i in range(word_length):
						if hint == word[i]:
							clue[i] = hint

			if letters_wrong == tries:
				'''hangingman(letters_wrong + 1)'''
				print ("Game Over.")
				print ("The word was ", word)
				computer_score += 1
				break
			if "".join(clue) == word:
				print ("You win!")
				print ("The word was ", word)
				player_score += 1
				break
		return play_again()

	def guess_letter(self):
		print ()
		letter = input("Take a guess at our mystery word - choose a letter:")
		letter.strip()
		letter.lower()
		print ()
		return letter

def play_again():
	answer = input("Would you like to play again? y/n: ")
	if answer in ("y", "Y", "Yes", "yes", "Of course"):
		return answer
	else:
		print ("Thanks for playing!")

def scores():
	global player_score, computer_score
	hangingman(8)
	print ("HIGH SCORES")
	print ("Player: ", player_score)
	print ("Computer: ", computer_score)

if __name__ == '__main__':
		start()




