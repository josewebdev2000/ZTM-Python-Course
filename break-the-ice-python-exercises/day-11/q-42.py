"""
Question:

    Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:

    Use map() to generate a list.Use filter() to filter elements of a list.Use lambda to define anonymous functions.

"""
from math import sqrt

def main():
    
    first_10 = range(1, 10 + 1)
    
    square_nums = list(map(square_num, first_10))
    
    squares_of_even = list(filter(check_square_of_even, square_nums))
    
    print(squares_of_even)


def square_num(num):
    return num ** 2

def check_square_of_even(num):
    
    square_root = sqrt(num)
    
    if square_root != int(square_root):
        return False
    
    elif square_root % 2 != 0:
        return False
    
    else:
        return True

if __name__ == "__main__":
    main()