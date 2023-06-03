"""
Question:

    Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

Hints:

    Use map() to generate a list. Use lambda to define anonymous functions.

"""

def main():
    
    first_20 = range(1, 20 + 1)
    
    squares = list(map(get_squared, first_20))
    
    print(squares)

def get_squared(num):
    return num ** 2

if __name__ == "__main__":
    main()