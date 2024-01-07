import random

ListeCarte = ['2s','2h','2d','2c','3s','3h','3d','3c','4s','4h','4d','4c','5s','5h','5d','5c', '6s','6h','6d','6c','7s','7h','7d','7c','8s','8h','8d','8c','9s','9h','9d','9c', 'Ts','Th','Td','Tc','Js','Jh','Jd','Jc','Qs','Qh','Qd','Qc','Ks','Kh','Kd','Kc','As','Ah','Ad','Ac']

def tirageCard(num:int) -> int:
    choiceCards = []
    for i in range(0, num):
        choiceCards.append(random.choice(ListeCarte))
    return choiceCards

print(tirageCard(5))