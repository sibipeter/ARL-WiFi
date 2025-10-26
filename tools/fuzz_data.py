import random


def make_random_numbers(n: int):
    """
    Generate a list of pseudo-random numbers for fuzz testing.
    This is not security-sensitive, so using random is acceptable.
    """
    return [random.randint(1, 100) % 10 for _ in range(n)]  # nosec B311


def make_random_pairs(n: int):
    """
    Generate a list of deterministic pairs for fuzz testing.
    """
    return [(i, (i * 3) % 7) for i in range(n)]
