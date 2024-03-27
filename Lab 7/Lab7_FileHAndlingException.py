# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:35:36 2024

@author: gurpr
"""

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:", content)
    except FileNotFoundError:
        print("Error: File not found!")
    finally:
        print("Finally block: Closing the file.")
        # File is automatically closed due to the 'with' statement, 
        # but you can perform additional cleanup or logging here if needed.

# Example usage
# read_file('C:\\Users\\gurpr\\Desktop\\example.txt')
read_file('C:\\Users\\gurpr\\Desktop\\example2.txt')

