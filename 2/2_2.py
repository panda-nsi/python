num = int(input("Entrez un entier signé en complément à deux (-128 à +127): "))

if num < 0:
    nb = 256 + num
else:
    nb = num

print("Votre entier naturel est: ", nb)