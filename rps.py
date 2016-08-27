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
