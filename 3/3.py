chaine = input("Entrez la chaine: ")
count = 0

for i in range(len(chaine)):
    if chaine[i] == "z" or chaine[i] == "Z":
        count += 1
print("Résultat:", count)

# 3b

print("Résultat:", chaine.count("z") + chaine.count("Z"))
