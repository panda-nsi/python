a = float(input("Entrer a: "))
b = float(input("Entrer b: "))
c = float(input("Entrer c: "))

delta = b ** 2 - 4 * a * c

print("Delta:", delta)
if delta < 0:
    print("Pas de solution")
elif delta == 0:
    print("Une solution:", -b / (2 * a))
else:
    print("Deux solutions: \nx1:", (-b - delta ** 0.5) / (2 * a), "\nx2:", (-b + delta ** 0.5) / (2 * a))