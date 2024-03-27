# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:34:58 2024

@author: gurpr
"""

a = input ("enter the number:")
print(f"Multiplication table of {a} is :")

for i in range(1,11):
    print(f"{a} * {i}= {int(a)*i}")
    
    
    
    
# what will happen if any body gives input as string

#lets execute and check
#Multiplication table of hello is :
# Traceback (most recent call last):

#   File ~\anaconda3\Lib\site-packages\spyder_kernels\py3compat.py:356 in compat_exec
#     exec(code, globals, locals)

#   File f:\phd\ta courses\python\python\lab6_tryexcept_table.py:12
#     print(f"{a} * {i}= {int(a)*i}")

# ValueError: invalid literal for int() with base 10: 'hello'



print("Some next lines in code")
print("****END OF PROGRAM ****")

# if there is exception then program never reached line 33 nd 34 of code

# if no exception then program reached line 33 and 34 of code

#Lets look another way around with try and except



