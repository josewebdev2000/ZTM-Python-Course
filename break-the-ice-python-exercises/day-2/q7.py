"""
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
    The element value in the i-th row and j-th column of the array should be i _ j.*

    Note: i=0,1.., X-1; j=0,1,­Y-1. Suppose the following inputs are given to the program: 3,5

    Then, the output of the program should be:
    
    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

"""

def main() -> None:
    
    x, y = get_num_seq()
    the_2D_arr = build_to_arr(x, y)
    print(the_2D_arr)

def build_to_arr(x,y) -> "list[list]":
    
    # Build initial dimensions of the 2D array
    arr_2d_dims = [[None for j in range(y)] for i in range(x)]
    
    # Loop through each array of the 2D array
    for i in range(x):
        
        for j in range(y):
            
            prod = i * j
            arr_2d_dims[i][j] = prod
    
    return arr_2d_dims    

def get_num_seq() -> list:
    """Return a string of comma separated numbers from the user"""
    
    got_error = True
    
    while got_error:
    
        try:
            num_seq = input("Enter a comma separated sequence of numbers: ")
            nums = [int(num) for num in num_seq.split(",")]
        
        except ValueError:
            print("\nRemember to enter a comma separated sequence of numbers")
            print("Example: 2,4,6,8,10")
            print("Try again\n")
        
        else:
            got_error = False
            
    return nums  

if __name__ == "__main__":
    main()