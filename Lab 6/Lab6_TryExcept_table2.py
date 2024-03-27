# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:42:03 2024

@author: gurpr
"""


# I want my program gets correct input then kit must run normally but 
# if there is error then I want it to handle gracefully

# wherever we doubt error we put under try

a = input ("enter the number:")
print(f"Multiplication table of {a} is :")

# this is block where error might appear 

try:
 for i in range(1,11):
    print(f"{a} * {i}= {int(a)*i}")
except Exception as e:  # e is used as template 
    print(e)
    
print("Some next lines in code")
print("****END OF PROGRAM ****")

# lets run and check with number and string 

# what if we dont want to write e
