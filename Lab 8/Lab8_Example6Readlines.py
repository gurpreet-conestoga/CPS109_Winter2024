# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:06:52 2024

@author: gurpr
"""

f = open('example3.txt' , 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
    
    #lets create an example 