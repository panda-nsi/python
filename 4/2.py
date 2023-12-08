from math import pi
def aireDisque(r):
    return pi * r ** 2

def aireDisqueWithUnit(r, unit):
    return str(aireDisque(r)) + unit + "²"
