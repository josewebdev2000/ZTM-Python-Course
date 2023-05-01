"""
    Define a class which has at least two methods:

        getString: to get a string from console input
        printString: to print the string in upper case.

    Also please include simple test function to test the class methods.
    
    Use init method to construct some parameters
"""

def main() -> None:
    
    stdin_stdout_handler = STDIN_N_STDOUT()
    stdin_stdout_handler.getString()
    stdin_stdout_handler.printString()

class STDIN_N_STDOUT(object):
    """Get string from STDIN and print it to STDOUT"""
    
    def __init__(self):
        
        self.__string = ""
    
    def getString(self):
        """Ask user for a string and set it to the private string."""
        
        self.__string = input("Enter some text here: ")
    
    def printString(self):
        """Show the text the user entered to the console."""
        print(self.__string)

if __name__ == "__main__":
    pass