# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:25:33 2024

@author: gurpr
"""
#  loop encounters a negative number in the list, it prints the number and exits
# List of numbers
numbers = [1, 3, 7, -2, 9, 4, -5, 6]

# Initialize a variable to keep track of whether a negative number is found
negative_found = False

# Start a while loop to iterate through the list of numbers
index = 0
while index < len(numbers):
    # Get the current number
    current_number = numbers[index]
    
    # Check if the current number is negative
    if current_number < 0:
        print("Negative number found:", current_number)
        negative_found = True
        # Exit the loop early because we found a negative number
        break
    
    # Move to the next number in the list
    index += 1

# If a negative number was not found, print a message
if not negative_found:
    print("No negative numbers found in the list.")
