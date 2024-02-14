# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:12:33 2024

@author: gurpr
"""

def find_factors(n):
    factors = []
    for i in range(2, 11):
        if n % i == 0:
            factors.append(i)
    return factors

def main():                                                                                                                                                                                                                                                                                                                                                                                   
    num = int(input("Enter an integer: "))
    factors = find_factors(num)
    if factors:
        print(f"The factors of {num} between 2 and 10 are: {', '.join(map(str, factors))}")
    else:
        print("This number has no factors between 2 and 10")

if __name__ == "__main__":
    main()
