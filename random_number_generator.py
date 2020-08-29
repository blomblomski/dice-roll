import random


def random_number():
    return random.randint(0, 6)


def random_numbers(amount):
    c = []
    while len(c) < amount:
        c.append(random_number())

    return c
