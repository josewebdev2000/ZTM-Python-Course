"""
Question:

    Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

Hints:

    Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list.
"""

def main():
    
    t = tuple(range(1, 10 + 1))
    new_t = []
    
    for i in t:
        
        if i % 2 == 0:
            new_t.append(i)
    
    print(tuple(new_t))

if __name__ == "__main__":
    main()