contador = 0
for numero in range(1, 7):
    ehPositivo = float(input())
    if ehPositivo > 0:
        contador = contador + 1
print('{} valores positivos'.format(contador))
