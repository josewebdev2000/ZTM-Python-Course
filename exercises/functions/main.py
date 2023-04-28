# Make a function that returns the highest even number

def highest_even(li):
    
    # Set a holder variable for the highest even number at the moment
    high_e = 0
    
    # Loop through each number
    for num in li:
        
        # If the number is even and greater than the holder variable, store it in the holder variable
        if num % 2 == 0 and num > high_e:
            high_e = num
    
    # Return the highest even number
    return high_e

highest_e = highest_even([10, 2, 3, 4, 8, 11])
print(highest_e)