# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:41:39 2024

@author: gurpr
"""

# give a letter grade based on a number score
# - if a student gets above 80, they get an A
# - otherwise if a student gets above 70 (but below 80), they get a B
# - Otherwise (student's score is below 70) they get a C
# - if score is less than 50, they get an F

score = 38

if score > 80:
    print("A")
elif 70 < score:      # score > 70 and score < 80
    print("B")
elif score > 50:
    print("C")
else: 
    print("F")










 