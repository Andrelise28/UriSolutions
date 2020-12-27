
triangulo = input().split()
a, lado2, lado3 = triangulo

n1 = float(1)
n2 = float(1)
n3 = float(1)
a = float(a)
lado2 = float(lado2)
lado3 = float(lado3)

if lado2 >= a and lado2 >= lado3:
    n1 = lado2
    if a >= lado3:
        n2 = a
        n3 = lado3
    else:
        n2 = lado3
        n3 = a
if lado3 >= a and lado3 >= lado2:
    n1 = lado3
    if a >= lado2:
        n2 = a
        n3 = lado2
    else:
        n2 = lado2
        n3 = a
if a >= lado2 and a >= lado3:
    n1 = a
    if lado2 >= lado3:
        n2 = lado2
        n3 = lado3
    else:
        n2 = lado3
        n3 = lado2
if a == lado2 and lado2 == lado3:
    n1 =a
    n2 =lado2
    n3 =lado3

a = n1
lado2 = n2
lado3 = n3

if a >= (lado2 + lado3):
    print('NAO FORMA TRIANGULO')
else:
    if (a ** 2) == (lado2 ** 2 + lado3 ** 2):
        print('TRIANGULO RETANGULO')
    if (a ** 2) > (lado2 ** 2 + lado3 ** 2):
        print('TRIANGULO OBTUSANGULO')
    if (a ** 2) < (lado2 ** 2 + lado3 ** 2):
        print('TRIANGULO ACUTANGULO')
    if (a == lado2 == lado3):
        print('TRIANGULO EQUILATERO')
    if a == lado2 != lado3 or lado2 == lado3 != a or a == lado3 != lado2:
        print('TRIANGULO ISOSCELES')
