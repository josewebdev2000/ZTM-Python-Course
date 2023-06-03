"""
Question:

    With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

Hints:

    Use [n1:n2] notation to get a slice from a tuple.
"""

def main():
    
    the_t = tuple(range(1, 10 + 1))
    
    half_length = len(the_t) // 2
    
    print(the_t[:5])
    print(the_t[5:])

if __name__ == "__main__":
    main()