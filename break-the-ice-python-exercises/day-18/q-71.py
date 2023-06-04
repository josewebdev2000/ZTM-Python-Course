"""
Question:

    Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.
    
Hints:
    Use random.choice() to a random element from a list.
"""
from random import choice

def main():
    
    nums = [n for n in range(10, 150 + 1) if n % 35 == 0]
    print(choice(nums))

if __name__ == "__main__":
    main()