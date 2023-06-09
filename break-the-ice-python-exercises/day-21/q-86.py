"""
Question:
    By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

Hints:
    Use list's remove method to delete a value.
"""

def main():
    l = [12,24,35,24,88,120,155]
    new_l = [n for n in l if n != 24]
    print(new_l)

if __name__ == "__main__":
    main()