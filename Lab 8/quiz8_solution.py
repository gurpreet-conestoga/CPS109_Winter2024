#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:23:42 2024

@author: mhabibi
"""

def next_item(collection):
    """ Returns the next value from an iterator. 
    If the iterator runs out of values, return None. 
    """   
    # Create an iterable from collection
    iterator = iter(collection)
    for item in collection:
        print(next(iterator, None))
    
    return None

