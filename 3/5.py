import random

number = random.randint(1, 100)
playerNum = int(input("---> "))
count = 0

while playerNum != number:
    count += 1
    if playerNum < number:
        print("Trop petit !")
    else:
        print("Trop grand !")
    playerNum = int(input("---> "))

print("Bravo, tu as gagné en", count, "coups !")