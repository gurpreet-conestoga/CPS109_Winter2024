#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Wed Mar 20 01:35:16 2024

@author: mhabibi

Recursion Examples

"""

def list_sum(numslist):
    """
    Returns the sum of a list of numbers using recursion.
    
    Precondition: len(numslist) >= 1
    """
    # ----- BASE CASE ------
    # 1 number left in list
    if len(numslist) == 1:
        return numslist[0]
    
    # --- RECURSIVE CASE ---
    else:
        # Return the sum of the first element
        return numslist[0] + list_sum(numslist[1:])
    
# print(list_sum([2, 4, 5, 6, 7])
        
        
def rreverse(s):
    """
    Returns the reverse of a string
    
    Example
    -------
    >>> rreverse("Hello")
    olleH

    """
    if len(s) == 1:
        return s
    else:
        return rreverse(s[1:]) + s[0] 
        
        
def sum_digits(num: int) -> int:
    """
    Returns the sum of all digits in num.
    
    Example
    -------
    >>> sum_digits(552)   # 5 + 5 + 2 = 12
    12
    
    """
    # BASE CASE - last digit reached?
    if num <= 9:
        return num
    # RECURSIVE CASE 
    last_digit = num % 10  # 552 % 10 = 2, 55 % 10 = 5
    return sum_digits(num // 10) + last_digit # 552 // 10 = 55, 55 // 10 = 5
    
# print(sum_digits(552))
  
def is_palindrome(s: str) -> bool:
    """
    Returns True if s is a palindrome.
    
    A palindrome is a word that can be read forwards and backwards.
    
    Precondition:
        - all letters in s are lowercase
        - len(s) > 0
    
    Example
    -------
    >>> is_palindrome("abba")
    True
    >>> is_palindrome("abc")
    False
    >>> is_palindrome("racecar")
    True
    """  
    # BASE CASE - only one letter in s
    if len(s) == 1: 
        return True
    # RECURSIVE CASE - more characters to evaluate
    if s[0] != s[-1]: 
        # no need to recurse anymore
        return False
    # first and last letter are the same. Check inner chars.
    return is_palindrome(s[1:-1])

# print(is_palindrome("racecar"))    
# print(is_palindrome("abc"))

        
        
        
        
        
    

