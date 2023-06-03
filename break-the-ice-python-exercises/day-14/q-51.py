"""
Question:

    Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

    Use try/except to catch exceptions.

"""

def main():
    
    try:
        division_result = 5 / 0
    
    except ZeroDivisionError:
        print("Can't divide by zero.")
    
    except Exception:
        print("Unknown error took place")
    
    else:
        print(division_result)

if __name__ == "__main__":
    main()