contador = 0
soma = 0

for numero in range(1, 7):
    ehPositivo = float(input())
    if ehPositivo > 0:
        contador = contador + 1
        soma = soma + ehPositivo

print('{} valores positivos'.format(contador))
print("%0.1f"%(soma/contador))

