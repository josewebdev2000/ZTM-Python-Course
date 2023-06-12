"""
Question:

    Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

    If the following string is given as input to the program:
    
    5
    2 3 6 6 5
    
    Then, the output of the program should be:
    5

Hints:

    Make the scores unique and then find 2nd best number

"""
def main():
    """Find the second highest score"""
    n = int(input("Enter number of participants: "))
    
    scores = [int(input("Enter participant score: ")) for _ in range(n)]
    
    scores = list(set(scores))
    
    scores.remove(max(scores))
    
    print(max(scores))
        

if __name__ == "__main__":
    main()