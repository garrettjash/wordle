# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.

Group 2-2
Garrett Ashcroft, Vivian Solgere, Caroline Tobler, Jared Rosenlund
"""

import random
import sys
from tkinter import messagebox

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
KEY_COLOR = "#DDDDDD" 


def randomWord():
    return random.choice(FIVE_LETTER_WORDS).upper()

def setColorBlind():
    CORRECT_COLOR = "#1E88E5"

def wordle():

    gw = WordleGWindow()
    iGuessCounter = 1
    chosen_word = randomWord()


    def enter_action(s):
        nonlocal iGuessCounter
        # This line makes sure the empty cells don't count as spaces
        s = s.strip().upper()
        # If the length is less than 5 characters, don't submit and send a message
        if len(s) < N_COLS:
            gw.show_message(chosen_word)
            #gw.show_message("Try a longer word!")                                       #GARRETT DO NOT FORGET TO UNCOMMENT THIS OUT :)
        elif not checkValidWord(s):
            gw.show_message("Not a valid word.")
            gw.set_current_row(iGuessCounter - 1)
        #If the word is valid, add one to the guess counter and set the current row to the new guess counter (next row)
        else:
            # This stops the program from blowing up after guess 6
            if iGuessCounter  < N_ROWS:
                # Increases the guess counter after each guess
                iGuessCounter += 1
                gw.set_current_row(iGuessCounter - 1)
                # For loop to look through each letter of the user guess
                for iCount in range(N_COLS):
                    # Checks is the guess is the correct word
                    if chosen_word == s:
                        # Set all the squares green on a correct guess
                        for iCorrect in range(N_COLS):
                            gw.set_key_color(s[iCorrect], CORRECT_COLOR)
                            gw.set_square_color(iGuessCounter - 2, iCorrect, CORRECT_COLOR)
                        gw.show_message("Congratulations!")
                        messagebox.showinfo("You Won!", "Congratulations, You Guessed the Word!")
                        sys.exit()
                    else:
                        # if the letter is correct, set the keyboard color and the square to green
                        if s[iCount] == chosen_word[iCount]:
                            gw.set_key_color(s[iCount], CORRECT_COLOR)
                            gw.set_square_color(iGuessCounter - 2, iCount, CORRECT_COLOR)
                        # If the letter is incorrect, color it properly
                        elif s[iCount] in chosen_word:
                            if gw.get_key_color(s[iCount]) == CORRECT_COLOR:
                                gw.set_square_color(iGuessCounter - 2, iCount, PRESENT_COLOR)
                            else:
                                gw.set_key_color(s[iCount], PRESENT_COLOR)
                                gw.set_square_color(iGuessCounter - 2, iCount, PRESENT_COLOR)
                        else: 
                            gw.set_key_color(s[iCount], MISSING_COLOR)
                            gw.set_square_color(iGuessCounter - 2, iCount, MISSING_COLOR)
            # Code that executes after the last guess
            else:
                if s == chosen_word:
                    messagebox.showinfo("You Won!", "Congratulations, You Guessed the Word!")
                else:
                    for iEnd in range(N_COLS):
                        # if the letter is correct, set the keyboard color and the square to green
                        if s[iEnd] == chosen_word[iEnd]:
                            gw.set_key_color(s[iEnd], CORRECT_COLOR)
                            gw.set_square_color(5, iEnd, CORRECT_COLOR)
                        # If the letter is incorrect, color it gray -NEED TO FIX AND CHANGE IT YELLOW 
                        elif s[iEnd] in chosen_word:
                            gw.set_key_color(s[iEnd], PRESENT_COLOR)
                            gw.set_square_color(5, iEnd, PRESENT_COLOR)
                        else: 
                            gw.set_key_color(s[iEnd], MISSING_COLOR)
                            gw.set_square_color(5, iEnd, MISSING_COLOR)
                    gw.show_message("Game Over!")
                    # Ask the group if we want this?
                    messagebox.showinfo("Game Over", "Game Over! Nice try, the word was " +  chosen_word)
                sys.exit()

            # Left to do:
                # On guess 6 it says nice try even if they guess it right - should be ready
                # Double letters
                # Clear boxes if they guess an invalid word

    def checkValidWord(userGuess):
        print(f"User Guess: {userGuess}")
        return userGuess.lower() in FIVE_LETTER_WORDS
    
    def evaluate_guess(guess, target_word):
        """
        Evaluates the guess against the target word and returns a list of colors
        representing the evaluation result for each letter in the guess.
        """
        # Initialize colors as MISSING_COLOR for all letters in the guess
        result_colors = [MISSING_COLOR for _ in guess]

        # First pass: mark correct letters in the correct position (green)
        for i in range(len(guess)):
            if guess[i] == target_word[i]:
                result_colors[i] = CORRECT_COLOR

        # Keep track of how many times each letter appears in the target word
        target_letter_count = {}
        for letter in target_word:
            if letter not in target_letter_count:
                target_letter_count[letter] = 1
            else:
                target_letter_count[letter] += 1

        # Subtract the green matches from the target letter count
        for i in range(len(guess)):
            if result_colors[i] == CORRECT_COLOR and guess[i] in target_letter_count:
                target_letter_count[guess[i]] -= 1

        # Second pass: mark correct letters in the wrong position (yellow)
        for i in range(len(guess)):
            if guess[i] in target_word and result_colors[i] != CORRECT_COLOR:
                if target_letter_count[guess[i]] > 0:
                    result_colors[i] = PRESENT_COLOR
                    target_letter_count[guess[i]] -= 1

        return result_colors
    
    

    gw.add_enter_listener(enter_action)

#if __name__ == "__main__":
        #wordle()

import tkinter as tk
from tkinter import messagebox

import random
import sys
from tkinter import messagebox

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR, COLORBLIND_CORRECT
KEY_COLOR = "#DDDDDD" 

def randomWord():
    return random.choice(FIVE_LETTER_WORDS).upper()

def checkValidWord(userGuess):
    print(f"User Guess: {userGuess}")
    return userGuess.lower() in FIVE_LETTER_WORDS

def checkDoubles(chosen_word):
    double_letters = []
    for i in range(len(chosen_word)):
        modified_word = chosen_word[:i] + chosen_word[i+1:]
        if chosen_word[i] in modified_word and chosen_word[i] not in double_letters:
            double_letters.append(chosen_word[i])

    return double_letters if double_letters else False



#HARD MODE *** make a toggle ? or ask a question at the beginning of the game?
def wordleHard():

    gw = WordleGWindow()
    iGuessCounter = 1
    chosen_word = randomWord()

    correct_letters = [''] * N_COLS  # Tracks the letters in the correct position
    present_letters = []  # Tracks letters that are present but not in the right spot


    def enter_action(s):
        nonlocal iGuessCounter
        # This line makes sure the empty cells don't count as spaces
        s = s.strip().upper()
        # If the length is less than 5 characters, don't submit and send a message
        if len(s) < N_COLS:
            gw.show_message(chosen_word)
            #gw.show_message("Try a longer word!")                                       #GARRETT DO NOT FORGET TO UNCOMMENT THIS OUT :)
        elif not checkValidWord(s):
            gw.show_message("Not a valid word.")
            gw.set_current_row(iGuessCounter - 1)
        elif not checkHardMode(s):
            gw.show_message("You must use all green and yellow letters")
            gw.set_current_row(iGuessCounter - 1)
        #If the word is valid, add one to the guess counter and set the current row to the new guess counter (next row)
        else:
            # This stops the program from blowing up after guess 6
            if iGuessCounter  < N_ROWS:
                # Increases the guess counter after each guess
                iGuessCounter += 1
                gw.set_current_row(iGuessCounter - 1)
                # For loop to look through each letter of the user guess
                for iCount in range(N_COLS):
                    # Checks is the guess is the correct word
                    if chosen_word == s:
                        # Set all the squares green on a correct guess
                        for iCorrect in range(N_COLS):
                            gw.set_key_color(s[iCorrect], CORRECT_COLOR)
                            gw.set_square_color(iGuessCounter - 2, iCorrect, CORRECT_COLOR)
                        gw.show_message("Congratulations!")
                        messagebox.showinfo("You Won!", "Congratulations, You Guessed the Word!")
                        sys.exit()
                    else:
                        # This if statement checks for double lettes and sets the colors appropriately
                        if checkDoubles(s) == False:
                            # if the letter is correct, set the keyboard color and the square to green
                            if s[iCount] == chosen_word[iCount]:
                                gw.set_key_color(s[iCount], CORRECT_COLOR)
                                gw.set_square_color(iGuessCounter - 2, iCount, CORRECT_COLOR)
                                correct_letters[iCount] = s[iCount]
                            # If the letter is incorrect, color it properly
                            elif s[iCount] in chosen_word:
                                if gw.get_key_color(s[iCount]) == CORRECT_COLOR:
                                    gw.set_square_color(iGuessCounter - 2, iCount, PRESENT_COLOR)
                                    if s[iCount] not in present_letters: #shouldnt happen
                                        present_letters.append(s[iCount])

                                else:
                                    gw.set_key_color(s[iCount], PRESENT_COLOR)
                                    gw.set_square_color(iGuessCounter - 2, iCount, PRESENT_COLOR)
                                    if s[iCount] not in present_letters:
                                         present_letters.append(s[iCount])
                            else: 
                                gw.set_key_color(s[iCount], MISSING_COLOR)
                                gw.set_square_color(iGuessCounter - 2, iCount, MISSING_COLOR)
                        else: # If the entered word has double letters
                            # used_letters = checkDoubles(s) - maybe create a function that gets used letters and not doubles
                            double_letters = checkDoubles(s)

                            for iCount, guess_letter in enumerate(s):
                                if guess_letter in double_letters and guess_letter in chosen_word:
                                    letter_count_in_word = chosen_word.count(guess_letter)  # Number of times the guessed letter appears in the chosen word
                                    letter_used_count = s[:iCount + 1].count(guess_letter)  # Number of times the guessed letter has been used
                                    if letter_used_count <= letter_count_in_word:
                                        if guess_letter == chosen_word[iCount]:
                                            gw.set_key_color(guess_letter.upper(), CORRECT_COLOR)
                                            gw.set_square_color(iGuessCounter - 2, iCount, CORRECT_COLOR)
                                            correct_letters[iCount] = guess_letter
                                        elif guess_letter in chosen_word:
                                            if gw.get_key_color(guess_letter.upper()) == CORRECT_COLOR:
                                                gw.set_square_color(iGuessCounter - 2, iCount, PRESENT_COLOR)
                                                if s[iCount] not in present_letters: #shouldnt happen
                                                    present_letters.append(s[iCount])
                                            else:
                                                gw.set_key_color(guess_letter.upper(), PRESENT_COLOR)
                                                gw.set_square_color(iGuessCounter - 2, iCount, PRESENT_COLOR)
                                                if s[iCount] not in present_letters:
                                                    present_letters.append(s[iCount])
                                        else:
                                            gw.set_key_color(guess_letter.upper(), MISSING_COLOR)
                                            gw.set_square_color(iGuessCounter - 2, iCount, MISSING_COLOR)
                                    else:
                                        gw.set_square_color(iGuessCounter - 2, iCount, MISSING_COLOR)
                                        gw.set_key_color(guess_letter.upper(), MISSING_COLOR)
                                else:
                                    # If the letter is correct, set the keyboard color and the square to green
                                    if guess_letter == chosen_word[iCount]:
                                        gw.set_key_color(guess_letter.upper(), CORRECT_COLOR)
                                        gw.set_square_color(iGuessCounter - 2, iCount, CORRECT_COLOR)
                                        correct_letters[iCount] = guess_letter
                                    # If the letter is incorrect, color it properly
                                    elif guess_letter in chosen_word:
                                        if gw.get_key_color(guess_letter.upper()) == CORRECT_COLOR:
                                            gw.set_square_color(iGuessCounter - 2, iCount, PRESENT_COLOR)
                                            if s[iCount] not in present_letters:
                                                present_letters.append(s[iCount])
                                        else:
                                            gw.set_key_color(guess_letter.upper(), PRESENT_COLOR)
                                            gw.set_square_color(iGuessCounter - 2, iCount, PRESENT_COLOR)
                                            if s[iCount] not in present_letters:
                                                present_letters.append(s[iCount])
                                    else:
                                        gw.set_key_color(guess_letter.upper(), MISSING_COLOR)
                                        gw.set_square_color(iGuessCounter - 2, iCount, MISSING_COLOR)
            # Code that executes after the last guess
            else:
                if s == chosen_word:
                    messagebox.showinfo("You Won!", "Congratulations, You Guessed the Word!")
                else:
                    for iEnd in range(N_COLS):
                        # if the letter is correct, set the keyboard color and the square to green
                        if s[iEnd] == chosen_word[iEnd]:
                            gw.set_key_color(s[iEnd], CORRECT_COLOR)
                            gw.set_square_color(5, iEnd, CORRECT_COLOR)
                            correct_letters[iCount] = guess_letter
                        # If the letter is incorrect, color it gray -NEED TO FIX AND CHANGE IT YELLOW 
                        elif s[iEnd] in chosen_word:
                            gw.set_key_color(s[iEnd], PRESENT_COLOR)
                            gw.set_square_color(5, iEnd, PRESENT_COLOR)
                        else: 
                            gw.set_key_color(s[iEnd], MISSING_COLOR)
                            gw.set_square_color(5, iEnd, MISSING_COLOR)
                    gw.show_message("Game Over!")
                    # Ask the group if we want this?
                    messagebox.showinfo("Game Over", "Game Over! Nice try, the word was " +  chosen_word)
                sys.exit()

    gw.add_enter_listener(enter_action)

    def checkHardMode(userGuess):
        for x in range(len(correct_letters)):
            if not correct_letters[x] == '':
                if not userGuess[x] == correct_letters[x]:
                    return False
                
        for y in range(len(present_letters)):
            if present_letters[y] not in userGuess:
                return False
            
        return True
    

def ask_user_mode():
    root = tk.Tk()
    # Hide the main window
    root.withdraw()

    # Ask the user for mode
    user_response = messagebox.askyesno("Mode Selection", "Would you like to play in Hard Mode?")
    
    # 'user_response' will be True for "Yes" (Hard Mode), and False for "No" (Regular Mode)
    hardMode = user_response

    user_response2 = messagebox.askyesno("Color Selection", "Would you like to play in color blind mode?")
    colorBlind = user_response2

    root.destroy()
    return hardMode, colorBlind

if __name__ == "__main__":
    hardMode, colorBlind = ask_user_mode()

    if colorBlind:
        setColorBlind()
        print("colorBlindSet")

    if hardMode:
        print("Hard Mode selected")
        wordleHard()
    else:
        print("Regular Mode selected")
        wordle()

    




#if __name__ == "__main__":
    #wordle()



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
# get_key_color(l