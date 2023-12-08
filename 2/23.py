note = float(input("Entrer une note: "))

if note < 10:
    mention = "Recalé"
elif note < 12:
    mention = "Passable"
elif note < 14:
    mention = "Assez bien"
elif note < 16:
    mention = "Bien"
else:
    mention = "Très bien"

print("Mention:", mention)