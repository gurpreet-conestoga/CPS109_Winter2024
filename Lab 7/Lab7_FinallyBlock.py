# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:18:49 2024

@author: gurpr
"""

try:
    l = [ 1,5,6,7]
    i = int(input("enter the index: "))
    print(l[i])
except:
    print("some error occured")
# finally:
   
print("always executed")
    
    
    # question arises .. What's the need of finally block
    # could have been written out of try except just as normal print statement 