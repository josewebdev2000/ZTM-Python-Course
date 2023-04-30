# Replace the following code using comprehension

def main():
    
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    
    print(f"Without Comprehension: {without_comprehension(some_list)}")
    print(f"With Comprehension: {with_comprehension(some_list)}")
    
def without_comprehension(l):

    duplicates = []
    
    for value in l:
        if l.count(value) > 1:
            if value not in duplicates:
                duplicates.append(value)
    
    return duplicates

def with_comprehension(l):
    
    return sorted(list({char for char in l if l.count(char) > 1}))

if __name__ == "__main__":
    main()
