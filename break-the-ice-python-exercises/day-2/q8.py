"""
    Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

    Suppose the following input is supplied to the program:
    without,hello,bag,world
    
    Then, the output should be:
    bag,hello,without,world

"""
def main() -> None:
    
    word_sequence = get_word_seq()
    word_sequence.sort()
    print(",".join(word_sequence))

def get_word_seq() -> list:
    """Return a string of comma separated numbers from the user"""
    
    got_error = True
    
    while got_error:
    
        try:
            word_seq = input("Enter a comma separated sequence of words: ")
            words = [word for word in word_seq.split(",")]
        
        except ValueError:
            print("\nRemember to enter a comma separated sequence of words")
            print("Example: bay, buy, good, awesome, fantastic")
            print("Try again\n")
        
        else:
            got_error = False
            
    return words 

if __name__ == "__main__":
    main()