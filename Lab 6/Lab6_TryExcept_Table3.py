# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:49:36 2024

@author: gurpr
"""

a = input ("enter the number:")
print(f"Multiplication table of {a} is :")

# this is block where error might appear 

try:
 for i in range(1,11):
    print(f"{a} * {i}= {int(a)*i}")
except Exception as e:  # e is used as template 
    print("Default message : OOPS!! error occured ")
    
    # though gives warning but still works
    # lets try by removing "Exception as e:" 
    
print("Some next lines in code")
print("****END OF PROGRAM ****")


# try:
#     #statements that could generate exception 
#     #exception
# except:
#     #solution of generated exception    