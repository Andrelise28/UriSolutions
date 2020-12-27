diaInicio = input().split()
horaInicio = input().split()
diaFim = input().split()
horaFim = input().split()
di, df = int(diaInicio[1]), int(diaFim[1])
hi, mi, si = int(horaInicio[0]), int(horaInicio[2]), int(horaInicio[4])
hf, mf, sf = int(horaFim[0]), int(horaFim[2]), int(horaFim[4])

minuto_seg = 60
hora_seg = minuto_seg * 60
dia_seg = hora_seg * 24
i = si + mi * minuto_seg + hi * hora_seg + di * dia_seg
f = sf + mf * minuto_seg + hf * hora_seg + df * dia_seg
if i < f:
    tempo = f - i
    dias = int(tempo / dia_seg)
    tempo = tempo % dia_seg
    horas = int(tempo / hora_seg)
    tempo = tempo % hora_seg
    minutos = int(tempo / minuto_seg)
    tempo = tempo % minuto_seg
    segundos = tempo
    print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias, horas, minutos, segundos))
