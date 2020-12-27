salarioAtual = float(input())

if salarioAtual <= 400.00:
    salario = salarioAtual * 1.15
    reajuste = salario - salarioAtual
    percentual = 15
if 400.01 <= salarioAtual <= 800.00:
    salario = salarioAtual * 1.12
    reajuste = salario - salarioAtual
    percentual = 12
if 800.01 <= salarioAtual <= 1200.00:
    salario = salarioAtual * 1.10
    reajuste = salario - salarioAtual
    percentual = 10
if 1200.01 <= salarioAtual <= 2000.00:
    salario = salarioAtual * 1.07
    reajuste = salario - salarioAtual
    percentual = 7
if  salarioAtual > 2000.00:
    salario = salarioAtual * 1.04
    reajuste = salario - salarioAtual
    percentual = 4

print('Novo salario: {:.2f}'.format(salario))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(percentual))