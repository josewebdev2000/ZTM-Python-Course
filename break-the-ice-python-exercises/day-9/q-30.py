"""
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

Hints:

Use len() function to get the length of a string
"""

def main():
    
    sentence1 = input("Enter a sentence: ")
    sentence2 = input("Enter another sentence: ")
    
    print(f"The longest sentence if any is: {get_longest_str(sentence1, sentence2)}")

def get_longest_str(s1, s2):
    
    if len(s1) > len(s2):
        return s1
    
    elif len(s1) == len(s2):
        return f"{s1}\n{s2}"
    
    else:
        return s2

if __name__ == "__main__":
    main()