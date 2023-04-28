# Python follows the following scope rules

# 1) Start with local scope
# 2) Get scope of parent functions
# 3) Get global scope

a = 1

def parent():
    a = 10
    
    def confusion():
        return a
    return confusion()

print(parent()) # Prints 10 bc parent of confusion() is parent()
print(a) # Prints 1 bc this function call is on the global scope