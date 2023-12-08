identifiant = input("Quel est votre identifiant ?")
password = input("Quel est votre mdp ?")

identifiants = {
    "lea.martin": "monty",
    "ale.lecouturier": "Huz4"
    }

if identifiant not in identifiants:
    print("This identifiant doesn't exist")
else:
    for elem in identifiants:
        if elem == identifiant:
            print(identifiants[elem] == password)
