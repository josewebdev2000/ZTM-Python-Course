# Return a list with all squares of the following list
my_list = [5,4,3]

squared_list = list(map(lambda n : n ** 2, my_list))
print(squared_list)

# Sort the following list of tuple integers according to the last integer from lowest to highest number
a = [(0,2), (4,3), (9,9), (10, -1)]

# Use lambda function to get last element from tuple of integers
a.sort(key = lambda tuple_of_ints : tuple_of_ints[-1])
print(a)