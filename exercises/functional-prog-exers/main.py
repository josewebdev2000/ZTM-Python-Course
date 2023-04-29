from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def cap(word):
    return word.capitalize()

cap_pets = list(map(cap, my_pets))
print(cap_pets)

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

my_numbers.sort()

association = list(zip(my_strings, my_numbers))
print(association)

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def over_50(num):
    return num > 50

high_scores = list(filter(over_50, scores))
print(high_scores)

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulate(acc, num):
    return acc + num

# Include scores in the list of my numbers
my_numbers.extend(scores)

total_num = reduce(accumulate, my_numbers, 0)
print(total_num)