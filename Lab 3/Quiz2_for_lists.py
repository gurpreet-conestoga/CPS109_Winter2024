# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:02:37 2024

@author: gurpr
"""

num = int(input("Enter an integer: "))

factors = []

for i in range(2, 11):
    if num % i == 0:
        factors.append(str(i))

if factors:
    print("The factors of", num, "between 2 and 10 are:", end=" ")
    for factor in factors:
        print(factor, end=", ")
    print()  # print newline after factors
else:
    print("This number has no factors between 2 and 10")
