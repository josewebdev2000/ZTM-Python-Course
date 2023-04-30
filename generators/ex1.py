# Generators are iterables that create values over time instead of storing them all in memory 
def main():
    
    g = generator_function(10)
    
    print(g) # Print info on generator object
    print(next(g)) # Get next number
    print(next(g)) # Get next number

# Creating our own generator
def generator_function(num):
    for i in range(num):
        # yield pauses the function but it does not cut it
        yield i * 2
        
if __name__ == "__main__":
    main()