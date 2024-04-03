#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:55:20 2024

@author: mhabibi
"""

def rlen(L: list) -> int:
    """ 
    Returns the length of L recursively.
    
    >>> rlen([])
    0
    >>> rlen([5, 9, 8, 7])
    4
    """
    # BASE CASE
    if not L: # is list empty?
        return 0
    # RECURSIVE CASE
    else:
        return 1 + rlen(L[:-1])



    
    
