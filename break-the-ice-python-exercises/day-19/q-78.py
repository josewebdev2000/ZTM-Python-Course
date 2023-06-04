"""
Question:    

    Please write a program to shuffle and print the list [3,6,7,8].

Hints:

    Use shuffle() function to shuffle a list.

"""
from random import shuffle

def main():
    
    l = [3,6,7,8]
    
    shuffle(l)
    
    print(l)

if __name__ == "__main__":
    main()