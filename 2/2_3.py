num = int(input("Entrez votre note: "))

if num < 10:
    print("Recalé")
elif num > 10 and num < 12:
    print("Pas de mentions")
elif num > 12 and num < 14:
    print("Assez bien")
elif num > 14 and num < 16:
    print("Bien")
elif num > 18:
    print("Félicitation")