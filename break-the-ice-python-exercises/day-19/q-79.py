"""
Question:
    Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:
    Use list[index] notation to get a element from a list.
"""

from itertools import product

def main():
    
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey", "Football"]
    
    sentence = [subjects, verbs, objects]
    
    combinations = list(product(*sentence))
    
    for combination in combinations:
        print(combination)

if __name__ == "__main__":
    main()