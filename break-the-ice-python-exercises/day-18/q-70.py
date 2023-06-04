"""
Question:

    Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

Hints:

    Use random.choice() to a random element from a list.

"""
from random import choice

def main():
    
    nums = tuple([n for n in range(0, 10 + 1)])
    print(choice(nums))

if __name__ == "__main__":
    main()