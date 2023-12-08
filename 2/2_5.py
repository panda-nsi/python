from math import *

print("Résolution de l'équation du second degré: ax²+bx+c = 0")

a = float(input("Rentrez a: "))
b = float(input("Rentrez b: "))
c = float(input("Rentrez c: "))

delta = b**2-4*a*c

print("Discriminant:", delta)
if delta < 0:
    print("Aucune solution possible car le discriminant < 0")
elif delta == 0:
    x = -b/2*a
    print("Une seule solution possible Réelles car le discriminant = 0: ")
    print("S = {", str(x), "}")
elif delta > 0:
    x1 = (-b - sqrt(delta))/2*a
    x2 = (-b + sqrt(delta))/2*a
    print("Deux solutions possible Réelles car le discriminant > 0: ")
    print("S={x1;x2} : S={" + str(x1) + ";" + str(x2) + "}")