"""
Question:
    By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Hints:
    Use list comprehension to delete a bunch of element from a list.
"""

def main():
    
    ori_l = [12,24,35,70,88,120,155]
    new_l = [n for n in ori_l if n % 35 != 0]
    print(new_l)

if __name__ == "__main__":
    main()