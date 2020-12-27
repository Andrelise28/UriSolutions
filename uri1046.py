x = input().split()
horaInicial, horaFinal = x

horaInicial = int(x[0])
horaFinal = int(x[1])

if horaInicial < horaFinal:
    t = horaFinal - horaInicial
else:
    t = (24 - horaInicial) + horaFinal
print('O JOGO DUROU {} HORA(S)'.format(t))
