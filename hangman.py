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


def hangedman(hangman):
	graphic = [
	"""
	+-------------+
	 |/      |
     |      
     |      
     |       
     |      
     |
    ===============
    """
    ,
    """
    +-------------+
	 |/      |
     |      (_)
     |      
     |       
     |      
     |
    ===============
    """
    ,
    """
    +-------------+
	 |/      |
     |      (_)
     |       |
     |       
     |      
     |
    ===============
    """
    ,
    """
    +-------------+
	 |/      |
     |      (_)
     |      \|
     |       
     |      
     |
    ===============
    """
    ,
    """
    +-------------+
	 |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    ===============
    """
    ,
    """
    +-------------+
	 |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    ===============
    """
    ,
    """
    +-------------+
	 |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    ===============
    """
    ,
    """
    +-------------+
	 |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    ===============
    """
    ,
    """
    +-------------+
	 |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    ================
	"""
	]