"""
Question:

    Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

Hints:

    Use random.sample() to generate a list of random values.

"""

from random import sample

def main():
    
    nums = [n for n in range(1, 1000 + 1) if n % 35 == 0]
    
    print(sample(nums, 5))

if __name__ == "__main__":
    main()