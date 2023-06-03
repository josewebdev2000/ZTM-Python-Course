"""
Question:

    Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

    Example: If the following words is given as input to the program:
    
    2 cats and 3 dogs.

    Then, the output of the program should be:

    ['2', '3']

    In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

    Use re.findall() to find all substring using regex.
"""
import re

def main():
    
    sentence = input("Enter some words: ")
    
    print(contains_only_digits(sentence))

def contains_only_digits(string):
    digit_regex = r'\d+'
    return re.findall(digit_regex, string)

if __name__ == "__main__":
    main()