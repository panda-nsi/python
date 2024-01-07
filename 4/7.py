from random import sample


def million():
    num = []

    numbers = list(range(1, 51))
    stars = list(range(1, 12))
    num += sample(numbers, 5)
    num += sample(stars, 2)
    return num

print(million())
