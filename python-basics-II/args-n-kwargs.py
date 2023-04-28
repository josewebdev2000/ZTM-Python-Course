# Learning about *args and **kwargs
# *args -> Get any number of positional arguments
# **kwargs -> Get any number of keyword arguments

def super_func(*args, **kwargs):
    
    total = 0
    
    for items in kwargs.values():
        total += items
    
    return sum(args) + total

sum_value = super_func(1, 2, 3, 4, 5, num=6, num2= 7, num3= 8, num4 = 9, num5 = 10)
print(sum_value)