import random


def make_random_numbers(n: int):
    return [random.randint(1, 100) % 10 for _ in range(n)]


def make_random_pairs(n: int):
    return [(i, (i * 3) % 7) for i in range(n)]
