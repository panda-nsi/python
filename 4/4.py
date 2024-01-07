from random import randint, choice
chaine = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def password(length):
    password = ""
    for i in range(0, length - 1):
        random = randint(0, len(chaine))
        password += chaine[random]
    return password

def newPassword(length):
    password = ""
    for i in range(0, length):
        password += choice(chaine)
    return password

print(password(6))
print(newPassword(5))