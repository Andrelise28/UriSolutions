contador = 0
for numero in range(1, 6):
    ehPositivo = float(input())
    if ehPositivo%2 == 0:
        contador = contador + 1
print('{} valores pares'.format(contador))
