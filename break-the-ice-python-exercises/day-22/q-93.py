"""
Question:
    Please write a program which prints all permutations of [1,2,3]

Hints:
    Use itertools.permutations() to get permutations of list.
"""
from itertools import permutations
def main():
    
    perms= list(permutations([1,2,3]))
    print(perms)
    
if __name__ == "__main__":
    main()