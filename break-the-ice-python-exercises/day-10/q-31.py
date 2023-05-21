"""
Question:

    Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

Hints:
    Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.
"""

def main():
    
    display_squared_dict()

def display_squared_dict():
    
    num_n_square = {}
    
    for i in range(1, 20 + 1):
        
        num_n_square[i] = i ** 2
    
    print(num_n_square)

if __name__ == "__main__":
    main()