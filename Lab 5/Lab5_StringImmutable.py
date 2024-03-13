# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:14:17 2024

@author: gurpr
"""

# Define a string
my_string = "Hello, World!"

# Attempt to modify the string
try:
    my_string[7] = 'F'  # Trying to change 'W' to 'F'
    print("Modified string:", my_string)
except TypeError as e:
    print("Error occurred:", e)
