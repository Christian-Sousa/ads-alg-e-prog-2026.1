total_hora = int(input("Horas: "))
total_dia = total_hora // 24
semana = total_dia // 7
hora = total_hora - total_dia*24
dia = total_dia - semana*7
print(f"> {total_hora} horas corresponde a {semana} semana(s), {dia} dia(s) e {hora} hora(s).")