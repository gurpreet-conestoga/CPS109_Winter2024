#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:47:14 2024

@author: mhabibi

CPS109 - Lab 7: Dictionaries

"""

def has_single_word(d):
    """ (dict of {str: list of int}) -> bool
    
    Returns True if and only if there is only one str word
    in the dictionary d.
    
    >>> has_single_word({"I": 1, "like": 2, "cats": 3})
    False
    >>> has_single_word({"apple": 2})
    True
    """
    return len(d) == 1


def count_occurrences(L):
    """ (list of object) -> dict of {object: int}
    
    Returns a dictionary in which the keys are the elements in L and
    their associated values are number of times the element appears in L.
    
    Examples
    --------
    >>> count_occurrences([8, 9, 8, 8, 9])
    {8: 3, 9: 2}
    
    >>> count_occurrences(['apple', 'apple', 'orange', 'banana', 'orange', 'orange', 'apple', 'banana'])
    {'apple': 3, 'orange': 3, 'banana': 2}
    """
    result = {}
    
    for item in L:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
            
    return result


def get_positions(text):
    """ (str) -> dict of {str: list of int}
    
    Returns a dictionary where the keys are the individual words in text, and
    the values are the positions in the text where the words occur (starting 
    at 1). Include punctuation and numbers in words, and convert alphabetic 
    characters to lowercase.
    
    >>> result = get_positions('cats Cats CATS CATS!!!')
    >>> result == {'cats': [1, 2, 3], 'cats!!!': [4]}
    True
    >>> result = get_positions("I think I like CPS109.")
    >>> result == {'i': [1, 3], 'think': [2], 'like': [4], 'cps109.': [5]}
    True
    """
    print("Original text --> ", text)    
    
    # Convert all words to lowercase
    lowercase_text = text.lower()
    print("After converting to lowercase --> ", lowercase_text)
    
    # Split string into a list of individual word token using split function
    split_text = lowercase_text.split()
    print("Text after splitting --> ", split_text)
    

    result = {}
    position = 1   # start at position 1, not 0!!
    for word in split_text:
        # is word already a key in our dict?
        if word not in result:
            result[word] = []
        result[word].append(position)
        position += 1
    return result
    

def find_population(continent_info):
    """ (dict of {str: dict of {str: dict of {str: int}}}) -> dict of {str: int}
    
    continent_info has keys representing continents, and the
    values are dictionaries where the keys represent countries on that
    continent and the values are dictionaries where the keys represent cities
    in that country and the values represent city populations.
    
    Returns a dictionary where the keys are continents from continent_info
    and the values are the total population of all cities on that coninent.
    
    
    >>> data = {'Europe': {'France': {'Paris': 5000, 'Lyon': 2000, 'Nice': 3200},
                           'Italy': {'Venice': 1200}}}
    
    >>> result = find_population(data)
    >>> result == {'Europe': 11400}
    True
    
    >>> data = {'North America': {
                    'Canada': {'Toronto': 5000, 'Ottawa': 2000}, 
                    'USA': {'Portland': 4000, 'New York': 5000, 'Chicago': 1000}}, 
                'Asia': {
                    'Thailand': {'Bangkok': 456}, 
                    'Japan': {'Tokyo': 10000, 'Osaka': 5000}}, 
                'Antartica': {}}
    
    >>> result = find_population(data)
    >>> result == {'North America': 17000, 'Asia': 15456, 'Antartica': 0}
    True
    """
    populations = {}
    
    for continent in continent_info:
        
        if continent not in populations:
            populations[continent] = 0
            
        for country in continent_info[continent]:
            for city in continent_info[continent][country]:
                city_population = continent_info[continent][country][city]
                populations[continent] += city_population
    
    return populations
    
    
    
    
    
    
    
    
    
    
    
    
    
