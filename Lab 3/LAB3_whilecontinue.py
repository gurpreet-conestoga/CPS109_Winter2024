# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:27:02 2024

@author: gurpr
"""

# List of numbers
numbers = [1, 3, 7, -2, 9, 4, -5, 6]

# Start a while loop to iterate through the list of numbers
index = 0
while index < len(numbers):
    # Get the current number
    current_number = numbers[index]
    
    # Check if the current number is negative
    if current_number < 0:
        # Skip printing negative numbers and move to the next iteration
        index += 1
        continue
    
    # Print the current number if it's not negative
    print("Current number:", current_number)
    
    # Move to the next number in the list
    index += 1
