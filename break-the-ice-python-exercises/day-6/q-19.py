"""
    You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

    1: Sort based on name
    2: Then sort based on age
    3: Then sort by score

    The priority is that name > age > score.

    If the following tuples are given as input to the program:

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

    Then, the output of the program should be:

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints:

    In case of input data being supplied to the question, it should be assumed to be a console input.We use itemgetter to enable multiple sort keys.
"""
from operator import itemgetter

def main() -> None:
    
    # Get data from user
    data_rows = get_stdin_data()
    
    # In the lambda function, x is the element contained in the data_rows list
    # In this case, the tuple (name, age, score)
    
    # data_rows.sort(key = x: (x[0], x[1], x[2]))
    
    # Sort them by score
    data_rows.sort(key = itemgetter(0,1,2))
    
    print(data_rows)
    

def get_stdin_data() -> "list[tuple]":
    """Get data from stdin and process it"""
    
    num_lines = int(input("Enter lines of data to provide: "))
    data_lines = []
    
    for i in range(num_lines):
        
        data_line = input("Enter data line with name, age, and score in the following format name,age,score: ")
        data_line = data_line.split(",")
        data_line[1] = int(data_line[1])
        data_line[2] = int(data_line[2])
        
        data_lines.append(tuple(data_line))
    
    return data_lines
        

if __name__ == "__main__":
    main()