"""
Question:

    Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:

    Use map() to generate a list.Use lambda to define anonymous functions.
    
"""

def main():
    
    first_10 = range(1, 10 + 1)
    
    squared_nums = list(map(square_num, first_10))
    
    print(squared_nums)
    

def square_num(num):
    return num ** 2
    

if __name__ == "__main__":
    main()