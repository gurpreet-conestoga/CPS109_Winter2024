# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:20:01 2024

@author: gurpr
"""

import random

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)

# Initialize a variable to keep track of whether the user has guessed correctly
correct_guess = False

# Start a while loop that continues until the user guesses correctly
while not correct_guess:
    # Ask the user to guess a number
    guess = input("Guess a number between 1 and 10: ")
    
    # Convert the user's input to an integer
    guess = int(guess)
    
    # Check if the guess is correct
    if guess == target_number:
        print("Congratulations! You guessed the correct number.")
        correct_guess = True
    else:
        print("Sorry, that's not the correct number. Try again.")
