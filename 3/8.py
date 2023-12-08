many = int(input("Combien de fois le sang: "))
u = 0

for i in range(1, many):
    u = 1+u/i
    print(i, u)