"""
Question:

    Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).


Hint:

    Use filter() to filter elements of a list.Use lambda to define anonymous functions.
"""

def main():
    
    first_20 = range(1, 20 + 1)
    
    only_even = list(filter(check_even, first_20))
    
    print(only_even)

def check_even(num):
    return num % 2 == 0

if __name__ == "__main__":
    main()