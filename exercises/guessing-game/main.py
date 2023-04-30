# main file that will run all the game
from utilities.take_user_input import take_num, take_num_range
from utilities.generate_random_number import get_random_num
from utilities.give_feedback import check_number

def main() -> None:
    
        # Introduce the user to the program
        intro()
        
        # Get data from user
        lo, hi, at = get_user_data()
        
        # Run the main game loop
        # Keep running as long as the user wants
        again = game_loop(lo, hi, at)
        
        while again:
            intro()
            lo, hi, at = get_user_data()
            again = game_loop(lo, hi, at)
    

def game_loop(lo, hi, at) -> None:
    """Represents a round of the game"""
    
    user_won = False
    
    # Write main game loop
    while True:
        
        # Get a random number
        random_num = get_random_num(lo, hi)
        
        # Ask the user for a number
        user_guess = take_num_range("Guess a number: ", lo, hi)
        
        # Evaluate user guess
        result = check_number(user_guess, random_num)
        
        # If user guess equals 'E' exit the loop and congratulate
        if result == "H":
            print("Your guess is too high. Try a lower number")
        
        elif result == "L":
            print("Your guess is too low. Try a higher number.")
        
        else:
            print(f"You're right!\nThe correct number was {user_guess}")
            user_won = True
            break
    
    if user_won:
        print("Fantastic. You won the game.")
    
    else:
        print("Try again next time.")
    
    # Ask the user to play again
    again = input("Do you want to play again (y/n)? ")
    
    return again == "y"

def get_user_data() -> tuple:
    
    # Get the lowest and highest numbers of the range
    lowest_num = take_num("Enter the lowest number to guess from: ")
    highest_num = take_num("Enter the highest number to guess from: ")
    
    # Ask the user for the attempts they want
    attempts = take_num("Enter the number of desired attempts: ")
    
    return lowest_num, highest_num, attempts

def intro() -> None:
    """Introduce the game to the user"""
    
    print("\n\nWelcome to the Guess My Number Program")
    print("Choose a range of numbers to guess from.")
    print("Then choose your number of attempts to guess")
    print("Have fun\n\n")

if __name__ == "__main__":
    main()