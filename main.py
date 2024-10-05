#
def get_count():
    value = int(input("Pick A Number: "))
    return value 

count = get_count()

result = ""

for i in range(count):
    result += "a"

print(result)


