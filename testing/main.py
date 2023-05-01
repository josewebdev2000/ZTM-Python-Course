def main() -> None:
    print(do_stuff(8))

def do_stuff(num=0) -> int:
    """does stuff"""
    try:
        if num:
            return int(num) + 5
        else:
            return "please enter a number"
    
    except ValueError as e:
        return e

if __name__ == "__main__":
    main()

# Use Bash command "python3 -m unittest" to run all unit tests in the same directory
# Use "-v" flag for verbose