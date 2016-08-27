#!/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5 python3
import random
import time

rock = 1
paper = 2
scissors = 3

names = { rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = { rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

def start():
	print ("Lets play a game of Rock, Paper, Scissors.")
	while game():
		pass
	scores()

def game():
	player = move()
	computer = random.randint(1,3)
	result(player,computer)
	return play_again()

def move():
	while True:
		print
		player = raw_input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
		try:
			player = int(player)
			if player in (1,2,3):
				return player
		except ValueError:
			pass
		print "Oops! I didn't understand that. Please enter 1,2 or 3."

		pass