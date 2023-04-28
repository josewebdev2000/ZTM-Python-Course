# You may initialize several variables in the same statement
a, b, c = 1, 2, 3

# In this case a = 1, b = 2, c = 3
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

# However, in order to unpack a list place a * character before the variable name
a, b, c, *d = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0

# In this case a = 1, b = 2, c = 3, d = [4, 5, 6, 7, 8, 9, 0]
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")

# You may even add an extra variable to define the limit of list unpacking
a, b, c, *d, e = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e}")