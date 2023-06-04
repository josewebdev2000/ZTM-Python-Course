"""
Question:
    Please write a program to randomly print a integer number between 7 and 15 inclusive.

Hints:
    Use random.randrange() to a random integer in a given range.

"""
from random import randrange

def main():
    print(randrange(7, 15 + 1))

if __name__ == "__main__":
    main()