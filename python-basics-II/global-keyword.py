# Global Keyword

# Use it to refer to global variables inside functions to change their value
total = 0

def count():
    global total
    total += 1
    return total

print(f"Initial count: {count()}")

for i in range(5):
    print(f"Current count: {count()}")

# Print the final value of total
print(f"Final count: {total}")