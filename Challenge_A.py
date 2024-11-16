import random
import string

def generateRandomString(length):
    result = ''.join(random.choices(string.ascii_letters,k=length))
    return result

def generateRandomRealNum():
    result = random.uniform(-1e6, 1e6)
    return str(result)

def generateRandomInteger():
    result = random.randint(-2**63, 2**63 - 1)
    return str(result)

def generateRandomAlnum(length):
    result = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    spaces_before = ' ' * random.randint(0, 10)
    spaces_after = ' ' * random.randint(0, 10)
    return spaces_before+result+spaces_after

current_size = 0
size_limit = 10 * 1024 * 1024

objectGenerator=[
    lambda: generateRandomString(5),
    generateRandomRealNum,
    generateRandomInteger,
    lambda: generateRandomAlnum(5)
]

with open("test.txt", "w") as f:
    while current_size < size_limit:
        # Randomly choose a generator and create an object
        obj = random.choice(objectGenerator)()
        # Add the object to the file
        if current_size > 0:  # Ensure comma separation after the first object
            f.write(",")
            current_size += 1
        f.write(obj)
        current_size += len(obj)


