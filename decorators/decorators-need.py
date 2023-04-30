# Code that shows why decorators are necessary
from time import time

def main():
    long_time()

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} ms to run')
        return result
    return wrapper

@performance
def long_time():
    
    for i in range(100000):
        i * 5

if __name__ == "__main__":
    main()
