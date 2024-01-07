from math import factorial

def factorielle(num):
    number = 1
    for i in range(1, num - 1):
        number *= i
    return number

print(factorielle(50))
print(factorial(50))