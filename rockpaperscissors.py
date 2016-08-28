'''

 _____     ____     ____
|  _  \   |  _ \   /   _\
| |_|  |  | |_| |  \__ \
|     /   |  __/      \ \
|  |\ \   | |       __/ |
|__| \_|  |_|      |___/
 

'''
#!/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5 python3
from tkinter import * 
from tkinter.ttk import *
import random
import time

def gui():
	rock = 1
	paper = 2
	scissors = 3

	names = { rock: "Rock", paper: "Paper", scissors: "Scissors"}
	rules = { rock: scissors, paper: rock, scissors: paper}

	'''player_score = 0
	computer_score = 0'''

	def start():
		'''print ("Lets play a game of Rock, Paper, Scissors.")'''
		while game():
			pass
		'''scores()'''

	def game():
		player = player_choice.get() 
		computer = random.randint(1,3)
		computer_choice.set(names[computer])
		result(player,computer)
		'''return play_again()'''

	def result(player, computer): 
		new_score = 0
		if player == computer: 
			result_set.set("Tie game.")
		else:
			if rules[player] == computer:
				result_set.set("Your victory has been assured.") 
				new_score = player_score.get()
				new_score += 1
				player_score.set(new_score)
			else:
				result_set.set("The computer laughs as you realise you have been defeated.")
				new_score = computer_score.get() 
				new_score += 1 
				computer_score.set(new_score)

	rps_window = Toplevel()
	rps_window.title ("Rock, Paper, Scissors")

	player_choice = IntVar() 
	computer_choice = StringVar()
	result_set = StringVar() 
	player_choice.set(1) 
	player_score = IntVar() 
	computer_score = IntVar()

	rps_frame = Frame(rps_window, padding = '3 3 12 12', width = 300) 
	rps_frame.grid(column=0, row = 0, sticky=(N,W,E,S)) 
	rps_frame.columnconfigure(0, weight=1) 
	rps_frame.rowconfigure(0,weight=1)

	Label(rps_frame, text='Player').grid(column=1, row = 1, sticky = W) 
	Radiobutton(rps_frame, text ='Rock', variable = player_choice, value = 1).grid(column=1, row=2, sticky=W)
	Radiobutton(rps_frame, text ='Paper', variable = player_choice, value = 2).grid(column=1, row=3, sticky=W)
	Radiobutton(rps_frame, text ='Scissors', variable = player_choice, value = 3).grid(column=1, row=4, sticky=W)
	
	Label(rps_frame, text='Computer').grid(column=3, row = 1, sticky = W) 
	Label(rps_frame, textvariable = computer_choice).grid(column=3, row=3, sticky = W)
	
	Button(rps_frame, text="Play", command = start).grid(column = 2, row = 2) 

	Label(rps_frame, text = "Score").grid(column = 1, row = 5, sticky = W)
	Label(rps_frame, textvariable = player_score).grid(column = 1, row = 6, sticky = W)
	
	Label(rps_frame, text = "Score").grid(column = 3, row = 5, sticky = W) 
	Label(rps_frame, textvariable = computer_score).grid(column = 3, row = 6, sticky = W)
	
	Label(rps_frame, textvariable = result_set).grid(column = 2, row = 7)
	
	'''def move():
		while True:
			print ()
			player = input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
			try:
				player = int(player)
				if player in (1,2,3):
					return player
			except ValueError:
				pass
			print ("Oops! I didn't understand that. Please enter 1,2 or 3.")

	def result(player,computer):
		print ("1...")
		time.sleep(1)
		print ("2...")
		time.sleep(1)
		print ("3!")
		time.sleep(0.5)
		print ("Computer threw {0}!".format(names[computer]))
		global player_score, computer_score
		if player == computer:
			print ("Tie game.")
		else:
			if rules[player] == computer:
				print ("Your victory has been assured.")
				player_score += 1
			else:
				print ("The computer laughs as you realise you have been defeated.")
				computer_score += 1

	def play_again():
		answer = input("Would you like to play again? y/n: ")
		if answer in ("y", "Y", "yes", "Yes", "Of course"):
			return answer
		else:
			print ("Thank you very much for playing our game. See you next time!")

	def scores():
		global player_score, computer_score
		print ("HIGH SCORES")
		print ("Player: ", player_score)
		print ("Computer: ", computer_score)
	'''

if __name__ == '__main__':
	'''start()'''
	gui()



