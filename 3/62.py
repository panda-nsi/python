message = input("Message a decoder: ").lower()
alphabet = 'defghijklmnopqrstuvwxyzabc'
ceasarCode = ''
letter = ''

for defaultLetter in message:
    if defaultLetter == ' ' or defaultLetter == "'":
        ceasarCode += defaultLetter
        continue
    num = alphabet.find(defaultLetter) - 3
    if num > 26:
        num = num - 26
    letter = alphabet[num]
    ceasarCode += letter
print(ceasarCode)


    