#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CPS109 winter 2024

@author: mhabibi

                    ~ Lab Quiz 5 ~
"""

def faro_shuffle(lst, out: bool):
    """
    Performs a Faro Shuffle on an input list.
    
    A Faro Shuffle splits a list into two halves,
    left and right, and then interleaves the elements
    of each hald to create a new list:
        - OUT shuffle order: left, right
        - IN shuffle order: right, left
    
    
    if out_shuffle is True, perform an "out shuffle".
    Otherwise, perform an "in shuffle"
    
    Precondition: 
        - lst contains an even number of elements.
    
    Examples
    --------
    # Using OUT shuffle
    >>> faro_shuffle([1, 2, 3, 4, 5, 6, 7, 8], True)
    [1, 5, 2, 6, 3, 7, 4, 8]
    >>> faro_shuffle([], True)
    []
    >>> faro_shuffle(['bob', 'jack'], True)
    ['bob', 'jack']
    
    # Using IN shuffle
    >>> faro_shuffle([1, 2, 3, 4, 5, 6, 7, 8], False)
    [5, 1, 6, 2, 7, 3, 8, 4]
    >>> faro_shuffle(["bob", "jack"], False)
    ["jack", "bob"]
    """
    # Split lists:
    left = lst[:len(lst) // 2]
    right = lst[len(lst) // 2:]
    
    shuffled = []
    for i in range(len(left)):  # or right, doesn't matter
        if out is True:
            # Perform an OUT shuffle
            shuffled.append(left[i])
            shuffled.append(right[i])
        else:
            # Perform an IN shuffle
            shuffled.append(right[i])
            shuffled.append(left[i])
    return shuffled
    
faro_shuffle([1, 2, 3, 4, 5, 6, 7, 8], True)
    

