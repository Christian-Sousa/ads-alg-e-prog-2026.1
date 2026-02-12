total_segundos = int(input("Segundos: "))
total_minutos = total_segundos // 60
horas = total_minutos // 60
segundos = total_segundos - total_minutos*60
minutos = total_minutos - horas*60
print(f"> {total_segundos} segundos equivale a {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s).")