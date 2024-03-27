# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:25:35 2024

@author: gurpr
"""
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print("Division is:", result)
    finally:
        print("This will always execute, regardless of whether there was an exception or not.")

# Example usage
#divide(6, 2)  # No exception
divide(6, 0)  # Exception: Division by zero
