tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def searchSequentially(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

""" Cette fonction renvoie l'indice (position) de la première
occurrence d'un nombre entier x dans un tableau t non trié ou -1 si x n'est pas présent """

def searchSequentially2(array, target):
    for i in array:
        if array[i] == target:
            return i
    return -1
