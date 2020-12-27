andar1 = int(input())
andar2 = int(input())
andar3 = int(input())

tempo1 = andar1 * 0 + andar2 * 2 + andar3 * 4
tempo2 = andar1 * 2 + andar2 * 0 + andar3 * 2
tempo3 = andar1 * 4 + andar2 * 2 + andar3 * 0

if tempo1 <= tempo2:
    menor = tempo1
else:
    menor = tempo2
if menor >= tempo3:
    menor = tempo3
print(menor)
