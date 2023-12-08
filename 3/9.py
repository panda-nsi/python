num = int(input("Nombre: "))
isPrime = True

for i in range(2, 10):
    if i != num and num % i == 0:
        isPrime = False
        
if isPrime:
    print("Le nombre est premier !")
else:
    print("Le nombre n'est pas premier :(")