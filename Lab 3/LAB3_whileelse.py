# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:32:34 2024

@author: gurpr
"""

# Calculate the factorial of a number
num = 5
factorial = 1
counter = num

# Start a while loop to calculate the factorial
while counter > 0:
    factorial *= counter
    counter -= 1
else:
    print("Factorial of", num, "is", factorial)
