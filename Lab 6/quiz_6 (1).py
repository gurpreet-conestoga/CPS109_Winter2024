#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:44:10 2024

@author: mhabibi
"""

def is_prime(num: int) -> bool:
    """
    

    Parameters
    ----------
    num : int
        num is an integer >= 1.

    Returns
    -------
    bool
        True if and only if num is prime.

    """
    for i in range(2, num - 1):
        if num % i == 0:
            return True
    return False
    
    