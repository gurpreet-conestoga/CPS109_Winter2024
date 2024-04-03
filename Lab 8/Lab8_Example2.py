# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:33:27 2024

@author: gurpr
"""

f = open('example.txt' , 'r')
#print(f)
text = f.read()
print(text)
f.close()