# Check for duplicates in the following list without using the set data type
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

# Make lists for elements that are repeated
duplicates = []

# Loop through each letter in the some_list list
for letter in some_list:
    # Add letter to the duplicates list only if they appear more than once and are not present in the duplicates list
    if some_list.count(letter) > 1 and letter not in duplicates:
        duplicates.append(letter)

# Print original list
print(f"Original List: {some_list}")

# Print the duplicates
print(f"Duplicates: {duplicates}")
