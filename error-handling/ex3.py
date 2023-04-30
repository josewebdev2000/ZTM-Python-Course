# Error Handling 3

# finally 

while True:
    try:
        age = int(input("Enter your age: "))
        10/age
        
    except ValueError:
        print("Please enter a number")
        
    except ZeroDivisionError:
        print("Please enter a number higher than 0")
    
    else:
        print("Thank you")
        break
    finally:
        print("Ok, I'm finally done")