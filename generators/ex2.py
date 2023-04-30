# Generators Example 2
from time import time

# Performance Decorator
def performance(fn):
    
    def wrapper():
        
        t1 = time()
        fn()
        t2 = time()
        
        print(f"It took {t2 - t1} ms to execute this operation.")
    
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(100000):
        i * 5

@performance
def long_time2():
    print('2')
    for i in list(range(100000)):
        i * 5

long_time()
long_time2()
        