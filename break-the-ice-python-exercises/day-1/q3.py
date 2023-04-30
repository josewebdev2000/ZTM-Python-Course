"""
    With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). 
    and then the program should print the dictionary.
    Suppose the following input is supplied to the program: 8
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

def main() -> None:
    
    num = get_num()
    
    print({n:n ** 2 for n in range(num + 1)})

def get_num() -> int:
    
    got_error = True
    
    while got_error:
        
        try:
            num = int(input("Enter a number: "))
        
        except TypeError:
            print("Please enter a number.")
            print("Try again.\n")
        
        else:
            got_error = False
    
    return num

if __name__ == "__main__":
    pass

if __name__ == "__main__":
    main()