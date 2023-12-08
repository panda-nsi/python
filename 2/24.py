hight = float(input("Entrer votre taille en mètre: "))
weight = float(input("Entrer votre poids en kilogramme: "))
imc = weight / (hight ** 2) * 10000

if imc < 16.5:
    status = "Famine"
elif imc < 18.5:
    status = "Maigreur"
elif imc < 25:
    status = "Corpulence normale"
elif imc < 30:
    status = "Surpoids"
elif imc < 35:
    status = "Obésité modérée"
elif imc < 40:
    status = "Obésité sévère"
else:
    status = "Obésité morbide"

print("IMC:", imc, "Status:", status)