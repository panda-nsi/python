num = int(input("Entrer un entier signé en complément à deux (-128 à +127): "))

if num < 0:
    num = 256 + num

print("En binaire naturel:", num)