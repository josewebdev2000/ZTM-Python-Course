"""
Question:

    You are given an integer, N. 
    Your task is to print an alphabet rangoli of size N.
    (Rangoli is a form of Indian folk art based on creation of patterns.)

    Different sizes of alphabet rangoli are shown below:
    
    #size 3

    ----c----
    --c-b-c--
    c-b-a-b-c
    --c-b-c--
    ----c----

    #size 5

    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------

Hints:

First print the half of the Rangoli in the given way and save each line in a list. 
Then print the list in reverse order to get the rest.

"""

from string import ascii_lowercase

def main():
    
    n = int(input("Enter size of Rangoli Alphabet: "))
    print_rangoli(n)

def print_rangoli(size):
    n = size
    alph = ascii_lowercase
    width = 4 * n - 3 # Calculate total width of each line

    ans = [] # Store each line of the pattern
    
    for i in range(n):
        left = '-'.join(alph[n - i - 1:n]) # Generate left side of the line with appropriate characters
        mid = left[-1:0:-1] + left # 
        final = mid.center(width, '-')
        ans.append(final)

    if len(ans) > 1:
        for i in ans[n - 2::-1]:
            ans.append(i)
    ans = '\n'.join(ans)
    print(ans)

if __name__ == "__main__":
    main()