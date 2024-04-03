# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:39:36 2024

@author: gurpr
"""

f= open("writelinedata.txt" , 'w')
lines = ['line 1\n' , 'line 2\n' , 'line 3\n']
f.writelines(lines)
f.close()