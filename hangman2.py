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
bDebugging = False

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
'''print ('words are', words)'''

hints = [' very small insect',' african animal ',' american ground animal',' sonar animal ',' giant of US parks',' live in the water and builds dams',' desert humps',' dometic animal ','hide the pearls ','king spitter ','rare forest dweller',' '
         ' desert howler ',' black bird ',' a rain...','mans best friend ',' not a horse ',' not a swan ','soaring in the sky ','like a weasel ','sly animal ','not a toad',' farmed for milk ',''
         ' big water bird ',' high flyer good sight',' not a tiger ',' not a snake ','another word for alpaca ',' blind ground dweller ','monafrican primatekey ','big horns ','quiet as a ... ','use to go down the grand canyon ','eye of ... ',''
         ' water animal ',' night big eyed animal ',' chinese rare animal ',' colorful bird ',' common park bird ','long and slipery ','down a hole ','like a sheep ','bigger than a mouse',' black brid',' '
         ' african horned anaimal ',' upstream swimmer ',' water animal trickster ','danger in the water ',' farm animal ','smelly animal',' 4 toed ','long and slipery',' arachnid ',''
         ' baby carrier ',' graceful water bird ',' not a lion ',' not a frog ',' colorful fish ',' not a chicken ','tropical swimmer ','sly long and thin ','big fish ','night howler '
         ' australian nocturnal ',' striped animal ']

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

def start():
	print ("Lets play a game of Hangman.")
	while game():
		pass
	scores()


def game():
	dictionary = ["hat","capital","rainbow","penguin","house","snake"]
	word = choice(words)
	word_length = len(word)
	hint = choice(word)
	hint2 = choice(word)
	clue = word_length * ["_"]
	word_index = words.index(word)
	tries = 7
	letters_tried = ""
	guesses = 0
	letters_right = 0
	letters_wrong = 0
	global computer_score, player_score
	print ("***** START *****")
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

			get_hint(letters_tried,hint,word_index,letter,word_length,word,clue,hint2)					

		else:
			print ("Choose another.")

		hangingman(letters_wrong)
		print (" ".join(clue))
		if (len(letters_tried) > 0):
			print ("You have had ",len(letters_tried)," guesses - They are: ", letters_tried)
		

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

def get_hint(letters_tried,hint,word_index,letter,word_length,word,clue,hint2):
	asked = 0
	if (len(letters_tried) == 3) and (asked != 1):
		ask = input("Do you want a hint: y/n")
		if ask in ("y", "Y", "Yes", "yes", "Of course"):
			asked = 1
			print ("Your hint is ", "'",hints[word_index],"'")
	if (len(letters_tried) == 5) and ((asked != 2) or (asked != 1)):
		ask = input("Do you want a hint: y/n")
		if ask in ("y", "Y", "Yes", "yes", "Of course"):
			asked = 2
			if (hint != letter) and (letters_tried.find(letter) == -1):
				print ("Your hint is letter ", hint, "and letter was ", letter)
				for i in range(word_length):
					if hint == word[i]:
						clue[i] = hint
			else:
				if letters_tried.find(letter) != -1:
					print ("Your hint2 is letter ", hint2, "and letter was ", letter," hint 1 was", hint)
					for i in range(word_length):
						if hint2 == word[i]:
							clue[i] = hint2

def guess_letter():
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




