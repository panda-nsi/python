num = int(input("Nombre a décomposer: "))
baseNum = num
caract = ""
primedNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]

while num != 1:
    for i in primedNumbers:
        if num % i == 0:
            caract += str(i) + " * "
            num = num/i

print(baseNum, "=", caract[0:len(caract) - 2])