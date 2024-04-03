# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:09:31 2024

@author: gurpr
"""

f = open('datafile.txt' , 'r')
i=0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in Python is : {m1}")
    print(f"Marks of student {i} in Operating System is : {m2}")
    print(f"Marks of student {i} in ML is : {m3}")
    