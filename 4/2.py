from math import pi

def airedisque(rayon):
    return pi * rayon ** 2.0

def aireDisqueWithUnit(rayon, unit):
    print(airedisque(rayon), unit + "²")

aireDisqueWithUnit(2.5, 'cm')