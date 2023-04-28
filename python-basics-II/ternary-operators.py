# Ternary Operator

# Make short if-else statements with the format
# action_if_true if condition else action_if_false

is_blocked = False
can_message = "not allowed to message" if is_blocked else "allowed to message"

print(can_message)