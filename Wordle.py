# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.

Group 2-2
Garrett Ashcroft, Vivian Solgere, Caroline Tobler, Jared Rosenlund
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def randomWord():
    return random.choice(FIVE_LETTER_WORDS).upper()


def wordle():
    gw = WordleGWindow()

    def enter_action(s):
        # nonlocal randomWord
        gw.show_message("You have to implement this method.")

    chosen_word = randomWord()
    # This sets the first row to the random word
    for iCount in range(5): #5 because they are all 5 letter words
        gw.set_square_letter(0, iCount, chosen_word[iCount])

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    # Hardcoded random word for display test
    word = randomWord()
    wordle()