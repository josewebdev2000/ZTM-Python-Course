"""
Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following:

    D 100
    W 200

D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:

    D 300
    D 300
    W 200
    D 100

Then, the output should be:

    500
"""
import sys

def main(clargs) -> None:
    
    # Get how many lines of input should be taken
    input_lines = int(clargs)
    
    # Get required input
    account_balance = total_amount(input_lines)
    
    print(account_balance)
    
def total_amount(input_lines: int) -> int:
    
    total = 0
    
    for _ in range(input_lines):
        
        stdin = input("Enter transaction type and money amount separated by a space: ").split(" ")
        
        if stdin[0].lower() == "d":
            total += int(stdin[1])
        
        else:
            total -= int(stdin[1])
        
    return total
        

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))