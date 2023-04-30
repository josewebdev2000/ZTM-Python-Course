# How Generators work under the hood

def main():
    special_for([1,2,3])

    gen = MyGen(0,100)

    for i in gen:
        print(i)

# Mimic the range() function in Python
class MyGen():
    current = 0
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration
        

# Mimic the for loop in Python
def special_for(iterable):
    iterator = iter(iterable)
    
    while True:
        
        try:
            print(next(iterator))
        
        except StopIteration:
            break

if __name__ == "__main__":
    main()