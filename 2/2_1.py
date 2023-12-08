key = int(input("Entrez votre numéro de sécurité sociale (13 chiffres): "))
controleKey = int(input("Entrez votre clé de controle: "))

formule = 97 - key % 97

if formule == controleKey:
    print("Votre numéro de sécurité sociale est valide")
else:
    print("Votre numéro de sécurité sociale est invalide")