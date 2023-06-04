"""
Question:

    Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

Hints:

    Use random.sample() to generate a list of random values.

"""

from random import sample

def main():
    
    print(sample([n for n in range(100, 200 + 1) if n % 2 == 0], 5))

if __name__ == "__main__":
    main()