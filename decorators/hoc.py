# Higher Order Function HOC

# HOC are functions that return other functions

def greet(func):
    func()
    
def greet2():
    def func():
        return 5
    return func

