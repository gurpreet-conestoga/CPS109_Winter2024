# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:28:53 2024

@author: gurpr
"""

# Define a list containing both numbers and strings
mixed_list = [1, 'a', 3.14, 'hello']

# Print the original list
print("Original list:", mixed_list)

# Modify the list by changing one of its elements
mixed_list[1] = 'b'

# Attempt to modify a string element
try:
    mixed_list[3][0] = 'H'  # Trying to change 'h' in 'hello' to 'H'
except TypeError as e:
    print("Error occurred:", e)
else:
    print("Modified string in list:", mixed_list[3])

# Print the modified list
print("Modified list:", mixed_list)
