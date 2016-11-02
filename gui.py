#!/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5 python3
from tkinter import *

import rockpaperscissors 
import hangman2

root = Tk()
root.title ("Games Collection")

mainframe = Frame(root, height = 200, width = 500) 
mainframe.pack_propagate(0)
mainframe.pack(padx = 5, pady = 5)

intro = Label(mainframe, text = """Please select one of the following games to play:""")

intro.pack(side = TOP)

rps_button = Button(mainframe, text = "Rock, Paper, Scissors", command = rockpaperscissors.gui)
rps_button.pack()

'''hm_button = Button(mainframe, text = "Hangman", command = hangman.start) 
hm_button.pack()'''

exit_button = Button(mainframe, text = "Quit", command = root.destroy) 
exit_button.pack(side = BOTTOM)

root.mainloop()