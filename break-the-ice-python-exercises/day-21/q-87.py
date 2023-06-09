"""
Question:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

Hints:
    Use set() and "&=" to do set intersection operation.

"""

def main():
    
    l1 = [1,3,6,78,35,55]
    l2 = [12,24,35,24,88,120,155]
    
    l3 = [n for n in l1 if n in l2]
    l3.extend([n for n in l2 if n in l1])
    print(l3)
    

if __name__ == "__main__":
    main()