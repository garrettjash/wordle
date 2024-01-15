# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.

Group 2-2
Garrett Ashcroft, Vivian Solgere, Caroline Tobler, Jared Rosenlund
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
KEY_COLOR = "#DDDDDD" 

def randomWord():
    return random.choice(FIVE_LETTER_WORDS).upper()

def wordle():

    gw = WordleGWindow()
    iGuessCounter = 0

    chosen_word = randomWord()

    def enter_action(s):
        nonlocal iGuessCounter
        # This line makes sure the empty cells don't count as spaces
        s = s.strip().lower()
        # If the length is less than 5 characters, don't submit and send a message
        if len(s) < N_COLS:
            gw.show_message(chosen_word)
            #gw.show_message("Try a longer word!")
        elif not checkValidWord(s):
            gw.show_message("Not a valid word.")
        #If the word is valid, add one to the guess counter and set the current row to the new guess counter (next row)
        else:
            # This stops the prgram from blowing up after guess 6
            if iGuessCounter  < N_ROWS -1:
                # Increases the guess counter after each guess
                iGuessCounter += 1
                gw.set_current_row(iGuessCounter)
                s = s.upper()
                # For loop to look through each letter of the user guess
                for iCount in range(N_COLS):
                    # if the letter is correct, set the keyboard color and the square to green
                    if s[iCount] == chosen_word[iCount]:
                        gw.set_key_color(s[iCount], CORRECT_COLOR)
                        gw.set_square_color(iGuessCounter - 1, iCount, CORRECT_COLOR)
                    # If the letter is incorrect, color it gray -NEED TO FIX AND CHANGE IT YELLOW 
                    else: 
                        gw.set_key_color(s[iCount], MISSING_COLOR)
                        gw.set_square_color(iGuessCounter - 1, iCount, MISSING_COLOR)

            else:
                gw.show_message("Game Over!")

    def checkValidWord(userGuess):
        print(f"User Guess: {userGuess}")
        return userGuess.lower() in FIVE_LETTER_WORDS

    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()


# Logic:
# User types in a word
# User presses enter
# Checks to see if the word is valid
# If valid word:
#     Guess count increase by 1
#     Iterate to next row
# If invalid: 
#     No count increase, display message maybe?

# WordleGWindow() Creates and displays the graphics window.
# set_square_letter(row, col, letter) Sets the letter in the specified row and column.
# get_square_letter(row, col) Returns the letter in the specified row and column.
# add_enter_listener(fn) Specifies a callback function for the ENTER key.
# show_message(msg) Shows a message below the squares.
# set_square_color(row, col, color) Sets the color of the specified square.
# get_square_color(row, col) Returns the color of the specified square.
# set_current_row(row) Sets the row in which typed characters appear.
# get_current_row() Gets the current row.
# set_key_color(letter, color) Sets the color of the specified key letter.
# get_key_color(letter) Returns the color of the specified key letter