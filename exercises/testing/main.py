from random import randint

def main():
    
    # generate a number 1~10
    answer = randint(1, 10)
    
    # check that input is a number 1~10
    while True:
        try:
            guess = int(input("Take a guess: "))
            if run_guess(guess, answer):
                break
        
        except ValueError:
            print("please enter a number")
            continue

# input from user?
def run_guess(guess, answer):
    
    if 0 < guess < 11:
        if guess == answer:
            print("You're a genius")
            return True
        else:
            print("Hey bozo, I said 1-10")
            return False  

if __name__ == "__main__":
    main()  