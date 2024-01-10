# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.

Group 2-2
Garrett Ashcroft, Vivian Solgere, Caroline Tobler, Jared Rosenlund
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    gw = WordleGWindow()

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    # This sets the first row to the random word
    for iCount in range(N_COLS): #Iterates through the number of columns (5)
        gw.set_square_letter(0, iCount, randomWord[iCount])

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    # Hardcoded random word for display test
    randomWord = 'zesty'
    wordle()