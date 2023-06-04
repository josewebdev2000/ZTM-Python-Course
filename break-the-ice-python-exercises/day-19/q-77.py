"""
Question:
    Please write a program to print the running time of execution of "1+1" for 100 times.

Hints:
    Use timeit() function to measure the running time.

"""
import datetime

def main():
    
    before_running = datetime.datetime.now()
    
    for _ in range(100):
        1 + 1
    
    after_running = datetime.datetime.now()
    
    speed = after_running - before_running
    
    print(speed)

if __name__ == "__main__":
    main()