# Error Handling 4

# Raise Error
while True:
    try:
        age = int(input("Enter your age: "))
        10/age
        raise ValueError("Hey cut it out")
        
    except ValueError:
        print("Please enter a number")
        
    except ZeroDivisionError:
        print("Please enter a number higher than 0")
    
    else:
        print("Thank you")
    finally:
        print("Ok, I'm finally done")