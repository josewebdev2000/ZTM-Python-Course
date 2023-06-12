"""
Question

    You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.

    If the following string is given as input to the program:

    aabbbccde

Then, the output of the program should be:

b 3
a 2
c 2
d 1
e 1

Hints

    Count frequency with dictionary and sort by Value from dictionary Items
"""
def main():
    
    word = input("Enter a word: ")
    
    letters_n_count = {}
    
    # Count each occurrence of a letter in the given word
    for letter in word:
        
        if letter not in letters_n_count:
            letters_n_count[letter] = 1
        
        else:
            letters_n_count[letter] += 1
    
    # Sort a dictionary in descending order by value
    for letter in sorted(letters_n_count, key=lambda letter: letters_n_count[letter], reverse=True):
        print(letter, letters_n_count[letter])
    

if __name__ == "__main__":
    main()