# From a 2D matrix that represents the pixels in a picture, print empty spaces for each 0
# and print * for each 1 number

# Make a dictionary to associate each binary number to its character
num_n_char = {
    0 : " ",
    1 : "*"
}

# Initialize the 2D matrix for the picture
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# Make a string to represent the picture
pic_rep = ""

# Make a nested loop to get each element
for each_list in picture:
    
    for bit in each_list:
        
        pic_rep += num_n_char.get(bit)
    
    pic_rep += "\n"

# Print the string representation of the picture
print(pic_rep)
        

