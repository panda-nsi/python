def carre(num):
    return num**2
def carreBoucle():
    num = 1
    while num <= 100:
        print(str(num) + "²", "=", carre(num))
        num += 1
print(carre(11.1111))
carreBoucle()