"""
Questions:
    Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hints:
    Use for loop to iterate all possible solutions.

"""

# Use a system of equations to solve this problem

# System to use

# Heads -> x + y = 35
# Legs -> 2x + 4y = 94

# x -> Chickens
# y -> Rabbits

import numpy as np

def main():
    
    # Make lists of coefficients of each formula
    heads_coefficients = [1, 1]
    legs_coefficients = [2, 4]
    
    # Make a list of solutions
    solutions = [35, 94]
    
    # Make numpy array of coefficients
    coefficients = np.array([heads_coefficients, legs_coefficients])
    
    # Make numpy array of solution
    solutions_arr = np.array(solutions)
    
    # Find number of chicken and rabbits
    nums_of_each = np.linalg.solve(coefficients, solutions_arr)
    
    print(f"There were {int(nums_of_each[0])} chickens and {int(nums_of_each[1])} rabbits among a total of 35 heads and 94 legs of chickens and rabbits in a farm.")

if __name__ == "__main__":
    main()