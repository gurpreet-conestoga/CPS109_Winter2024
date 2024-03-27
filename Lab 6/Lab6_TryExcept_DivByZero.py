# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:33:47 2024

@author: gurpr
"""

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    else:
        print("Result:", result)

# Example usage:
divide_numbers(10, 2)  # This will print: Result: 5.0
divide_numbers(10, 0)  # This will print: Error: Cannot divide by zero!
