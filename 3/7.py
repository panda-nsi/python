u = float(input('Valeur initiale: '))
rang = int(input("Jusqu'a quel rang: "))

print(0, u)
for i in range(1, rang):
    u = u/2 + 1/u
    print(i, u)