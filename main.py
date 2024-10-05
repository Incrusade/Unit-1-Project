import random
import string


result = ""
# Function to get a random character/digit
def rand_char():
    possibilities = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return random.choice(possibilities)

for i in range(10):
    result += rand_char()

print(result)

