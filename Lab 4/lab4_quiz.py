#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:34:25 2024

@author: mhabibi
"""

def print_nums():
    """
    For multiples of:
        - 3, print "Fizz" instead of the number.
        - 5, print "Buzz" instead of the number.
        - both 3 and 5, print "FizzBuzz".
        
    Otherwise, print the number.
       
    Other rules:
       - If N <= 1, print "N must be greater than 1"
       - If N > 100, print "Too much work, no thanks"
       
    """ 
    N = int(input("Enter an integer: "))
    
    if N <= 1:
        print("N must be greater than one")
        return None
    
    elif N > 100:
        print("Too much work, no thanks")
        return None
    
    else:
        for num in range(1, N+1):
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)
                
    return None



