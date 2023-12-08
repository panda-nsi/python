from math import *

size = int(input("Entrez votre taille en cm: "))
weight = int(input("Entrez votre masse en kg: "))

imc = (weight/size**2)*10000

print("Votre IMC: ", round(imc))

if imc < 16:
    print("Anorexie ou dénutrition")
elif imc > 16.5 and imc < 18.5:
    print("Maigreur")
elif imc > 18.5 and imc < 25:
    print("Corpulence normale")
elif imc > 25 and imc < 30:
    print("Surpoids")
elif imc > 30 and imc < 35:
    print("Obésité modérée (Classe 1)")
elif imc > 35 and imc < 40:
    print("Obésité modérée (Classe 2)")
elif imc > 40:
    print("Obésité morbide ou massive")