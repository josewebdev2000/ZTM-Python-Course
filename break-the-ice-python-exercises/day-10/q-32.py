"""
Question:
    Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

Hints:
    Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
"""

def main():
    
    print(print_keys_squared_dict())

def print_keys_squared_dict():
    
    num_n_squares = {}
    
    for i in range(1, 20 + 1):
        
        num_n_squares[i] = i ** 2
    
    return num_n_squares.keys()

if __name__ == "__main__":
    main()