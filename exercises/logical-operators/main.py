# Simple message using if-else statements

is_magician = False
is_expert = True
message = ""

# Check if magician AND expert: "you are a master magician"
if is_magician and is_expert:
    message = "You are a master magician"
# Check if magician but not expert: "At least you're getting there"
elif is_magician and not is_expert:
    message = "At least you're getting there"
# If you're not a magician: "You need magic powers"
else:
    message = "You need magic powers"

print(message)