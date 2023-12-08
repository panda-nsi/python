def carre(num):
    return num ** 2


def carreAll():
    for i in range(1, 101):
        print(str(i) + "²", ">", carre(i))
