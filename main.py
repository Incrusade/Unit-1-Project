import random
import string
import unittest


# Function to get a random character/digit
def rand_char():
    possibilities = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return random.choice(possibilities)
# Function to ask for input
def get_count():
    value = int(input("Pick A Number: "))
    return value 

count = get_count()

result = ""
# For loop to generate password off of count from input
for i in range(count):
    result += rand_char()

print(f'A random password with {count} characters is {result}.')

#Unit Test for function rand_char
class TestRandom(unittest.TestCase):
    def test_random(self):
        result = rand_char()
        self.assertEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()
