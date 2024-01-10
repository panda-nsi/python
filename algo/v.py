import random

def tri_selection(arr):
    n = len(arr)
    for i in range(n - 1):
        index_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[index_min]:
                index_min = j
        arr[i], arr[index_min] = arr[index_min], arr[i]

# Tri d'une centaine d'entiers aléatoires
entiers = [random.randint(0, 1000) for _ in range(100)]
print("Avant le tri par sélection des entiers:")
print(entiers)
tri_selection(entiers)
print("Après le tri par sélection des entiers:")
print(entiers)

# Tri d'une dizaine de chaînes de caractères
chaines = [input("Entrez une chaîne de caractères : ") for _ in range(10)]
print("Avant le tri par sélection des chaînes:")
print(chaines)
tri_selection(chaines)
print("Après le tri par sélection des chaînes:")
print(chaines)