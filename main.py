import random
import string

# Function to get a random character/digit
def rand_char():
    possibilities = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return random.choice(possibilities)
  
def get_count():
    value = int(input("Pick A Number: "))
    return value 

count = get_count()

result = ""

for i in range(count):
    result += rand_char()

print(f'A random password with {count} characters is {result}.')