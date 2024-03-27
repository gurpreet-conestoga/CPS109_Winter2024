# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:02:00 2024

@author: gurpr
"""

try:
    num = int(input("enter an integer:"))
    a = [6,3]
    print(a[num])
except ValueError:
    print("number entered is not an integer")
except IndexError:
    print("Index error")