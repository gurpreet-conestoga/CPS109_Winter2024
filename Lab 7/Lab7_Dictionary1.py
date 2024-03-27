# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:03:40 2024

@author: gurpr
"""

# Creating a dictionary for a student
student = {
    "name": "Alice",
    "age": 22,
    "major": "Engineering",
    "grade": "A"
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])
print("Grade:", student["grade"])

# Modifying values
student["age"] = 23
student["grade"] = "A+"
print("Updated Age:", student["age"])
print("Updated Grade:", student["grade"])

# Adding new key-value pairs
student["email"] = "alice@example.com"
print("Email:", student["email"])

# Removing a key-value pair
del student["grade"]
print("Dictionary after removing 'grade':", student)
