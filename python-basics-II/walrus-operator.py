# The Walrus Operator assigns values to variables as parts of larger expressions

# Example with if statement
def if_walrus_example():
    
    a = 'Hello'
    
    # The n variable is assigned the length of the string a in the if statement
    if ((n := len(a)) > 10):
        print(f"Too long {n} elements")

# Example with while statement
def while_walrus_example():
    
    while (option := input("Enter some text: ")) != "quit":
        print("You entered: " + option)

if_walrus_example()
while_walrus_example()