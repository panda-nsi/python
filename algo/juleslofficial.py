def recherche_sequentielle_1(x, t):
    for i in range(len(t)):
        if t[i] == x:
            return i


def recherche_sequentielle_2(x, t):
    for i in range(len(t)):
        if t[i] == x:
            return i
    return -1

def recherche_sequentielle_3(x, t):
    searchNum = 0
    while t[searchNum] != x:
        searchNum += 1
        if searchNum == len(t):
            return -1
    return searchNum