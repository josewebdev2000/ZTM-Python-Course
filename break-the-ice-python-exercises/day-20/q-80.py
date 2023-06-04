"""
Question:

    Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

Hints:

    Use list comprehension to delete a bunch of element from a list.

"""

def main():
   
   ori_l = [5,6,77,45,22,12,24] 
   
   odd_l = [n for n in ori_l if n % 2 != 0]
   
   print(odd_l)

if __name__ == "__main__":
    main()