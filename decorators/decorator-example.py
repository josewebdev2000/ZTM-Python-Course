# Decorators supercharge functions

# Decorators are HOC

# Decorators allow Python functions to have extra features
def main():
    hello("Hello")
    bye("Goodbye")
    
    # a = my_decorator(hello)
    # a('hiii')

# Make a function that will extend the behavior of another function
def my_decorator(func): # Func is the function to be extended by the extension
    def wrap_func(param): # param is the parameter/s of the function to extend
        print('****')
        func(param)
        print('****')
    return wrap_func


# Make common functions
@my_decorator
def hello(greeting):
    print(greeting)

@my_decorator
def bye(goodbye):
    print(goodbye)
    
if __name__ == "__main__":
    main()
