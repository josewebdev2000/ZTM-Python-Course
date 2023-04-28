my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(f"Initial my_set: {my_set}")
print(f"Initial your_set: {your_set}")

# Get elements of my_set that are not present in your_set
print(f"Set difference: {my_set.difference(your_set)}")

# Get elements that are present in both my_set and your_set
print(f"Set intersection: {my_set.intersection(your_set)}")

# Get all elements between my_set and your_set
print(f"Set union: {my_set.union(your_set)}")

# Check if my_set does not have elements in common with your_set
print(f"my_set is disjoint to your_set: {my_set.isdisjoint(your_set)}")

# Check if all elements of my_set are present in your_set
print(f"your_set is subset of my_set: {my_set.issubset(your_set)}")

# Check if all elements of your_set are present in my_set
print(f"my_set is superset of your_set: {my_set.issuperset(your_set)}")

# Remove all elements from my_set that are present in your_set
my_set.difference_update(your_set)
print(f"my_set: {my_set}")