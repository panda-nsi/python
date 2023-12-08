#secu = "189112610826891"
#key = secu.replace("91", "")

#print("La clé de contrôle de ", secu, "est")

key = "189112610826891"
res = key[13] + key[14]
key = key.replace(res, "")

print("La clé de controle de ", key, " est ", res)