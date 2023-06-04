"""
Question:
    By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
    
Hints:
    Use list comprehension to make an array.
"""

def main():
    
    le_list = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(3)]
    print(le_list)

if __name__ == "__main__":
    main()