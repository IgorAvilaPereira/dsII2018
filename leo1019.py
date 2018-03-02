tempoSegundos = input()
horas = tempoSegundos/3600
minutos = (tempoSegundos%3600)/60
segundos = (tempoSegundos%3600)%60
print(str(horas)+":"+str(minutos)+":"+str(segundos))