"""
Question

    Write a Python program that accepts a string and calculate the number of digits and letters.

Input

    Hello321Bye360

Output

    Digit - 6
    Letter - 8

Hints

    Use isdigit() and isalpha() function
"""
from functools import reduce

def main():
    
    word = input("Enter a word composed of letters and/or digits: ")
    chars = [char for char in word]
    
    digits = reduce(count_digit, chars, 0)
    letters = reduce(count_letter, chars, 0)
    
    print(f"Digit - {digits}")
    print(f"Letter - {letters}")
    

def count_digit(inc, item):
    
    if item.isdigit():
        return inc +  1
    
    else:
        return inc

def count_letter(inc, item):
    
    if item.isalpha():
        return inc + 1
    
    else:
        return inc

if __name__ == "__main__":
    main()