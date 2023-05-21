"""
Question:

    Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

Hints:
    Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use tuple() to get a tuple from a list.
"""

def main():
    
    print(make_squared_list())

def square_num(num):
    
    return num ** 2

def make_squared_list():
    
    nums = range(1, 20 + 1)
    
    return tuple(map(square_num, nums))   

if __name__ == "__main__":
    main()