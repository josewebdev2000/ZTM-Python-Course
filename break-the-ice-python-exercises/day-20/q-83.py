"""
Question:
    By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

Hints:
    Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.
"""

def main():
    
    ori_l = [12,24,35,70,88,120,155]
    
    new_l = [n for (i, n) in enumerate(ori_l, 0) if i not in (2-1, 4-1)]
    
    print(new_l)

if __name__ == "__main__":
    main()