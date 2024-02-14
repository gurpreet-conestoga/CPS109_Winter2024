# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:17:36 2024

@author: gurpr
"""

# Define the correct password
correct_password = "python123"

# Initialize a variable to keep track of whether the password is correct
password_correct = False

# Start a while loop that continues until the password is correct
while not password_correct:
    # Ask the user to enter the password
    password_attempt = input("Enter the password: ")
    
    # Check if the entered password is correct
    if password_attempt == correct_password:
        print("Correct password! Welcome.")
        password_correct = True
    else:
        print("Incorrect password. Try again.")
