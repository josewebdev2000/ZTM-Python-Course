"""
Question:

    Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:

    Use + sign to concatenate the strings.
"""

def main():
    
    sentence1 = input("Enter a sentence: ")
    sentence1 += " "
    sentence2 = input("Enter another sentence: ")
    
    print(f"Your combined sentence is: {conc_them(sentence1, sentence2)}")

def conc_them(s1, s2):
    return s1 + s2

if __name__ == "__main__":
    main()