minutos_inicial = int(input("Minutos: "))
horas_inicial = minutos_inicial // 60
dias = horas_inicial // 24
minutos = minutos_inicial - horas_inicial*60
horas = horas_inicial - dias*24
print(f"> {minutos_inicial} minuto(s) corresponde a {dias} dia(s), {horas} hora(s) e {minutos} minuto(s).")
