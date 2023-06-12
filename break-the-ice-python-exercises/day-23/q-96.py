"""
Question:

    You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

    If the following string is given as input to the program:

    ABCDEFGHIJKLIMNOQRSTUVWXYZ
    4

Then, the output of the program should be:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

Hints:
    Use wrap function of textwrap module

"""
def main():
    
    s = input("Enter a string: ")
    w = int(input("Enter desired string width: "))
    
    new_s = ""
    
    for (i, char) in enumerate(s, 0):
        
        if i % w == 0 and i > 0:
            new_s += "\n"
        
        new_s += char
    
    print(new_s)

if __name__ == "__main__":
    main()