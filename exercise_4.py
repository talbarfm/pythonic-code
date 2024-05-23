import random


def three_random_numbers():
    return [random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)]


a, b, c = three_random_numbers()
print(a + c)
