"""
    A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2

    The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2

    Then, the output of the program should be:

2

Hints:

    In case of input data being supplied to the question, it should be assumed to be a console input.Here distance indicates to euclidean distance.Import math module to use sqrt function.

"""

import math
from functools import reduce

def main():
    
    # Get data from the user
    moves = grab_stdin()
    
    # Get total horizontal moves
    total_hor_moves = reduce(add_all_horizontal_moves, moves, 0)
    
    # Get total vertical moves
    total_ver_moves = reduce(add_all_vertical_moves, moves, 0)
    
    # Calculate the distance between vertical and horizontal points
    distance_traveled = round(calculate_distance_between_two_points(total_hor_moves, total_ver_moves))
    
    # Print the distance
    print(distance_traveled)

def grab_stdin():
    """Get stdin input"""
    
    dirs_n_moves = []
    
    while True:
        
        data = input("Enter move: ")
        
        if not data:
            break
        
        else:
            data = data.split(" ")   
            direction = data[0].upper()
            move = float(data[1])
            
            dirs_n_moves.append((direction, move))
    
    return dirs_n_moves

def add_all_horizontal_moves(acc, given_tuple):
    
    if given_tuple[0] == "RIGHT":
        return acc + given_tuple[1]
    
    elif given_tuple[0] == "LEFT":
        return acc - given_tuple[1]
    
    else:
        return acc

def add_all_vertical_moves(acc, given_tuple):
    
    if given_tuple[0] == "UP":
        return acc + given_tuple[1]
    
    elif given_tuple[0] == "DOWN":
        return acc - given_tuple[1]
    
    else:
        return acc

def calculate_distance_between_two_points(x_total, y_total):
    return math.sqrt((x_total ** 2) + (y_total ** 2))
    
    

if __name__ == "__main__":
    main()