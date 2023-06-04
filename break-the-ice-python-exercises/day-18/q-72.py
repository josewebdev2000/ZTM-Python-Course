"""
Question:

    Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

Hints:
    Use random.sample() to generate a list of random values.
"""
from random import sample

def main():
    print(sample(range(100, 200 + 1), 5))

if __name__ == "__main__":
    main()