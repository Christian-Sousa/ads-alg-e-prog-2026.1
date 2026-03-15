def ler_num(entrada):
    return int(input(entrada))

def tempo_jogo(horas_inicio, minutos_inicio, horas_termino, minutos_termino):
    total_horas = 0
    total_minutos = 0
    if horas_inicio > horas_termino and minutos_inicio > minutos_termino:
        total_horas = total_horas+24
        total_minutos = (minutos_inicio+minutos_termino)%60
        total_horas = total_horas-1
    else: 
        total_horas = horas_inicio+horas_termino
        total_minutos = (minutos_inicio+minutos_termino)%60
    return total_horas, total_minutos
        

def main():
    horas_inicio=ler_num("Hora do início do jogo: ")
    minutos_inicio=ler_num("Minutos do início do jogo: ")
    horas_termino=ler_num("Hora do término do jogo: ")
    minutos_termino=ler_num("Minuto do término do jogo: ")
    total_horas, total_minutos = tempo_jogo(horas_inicio, minutos_inicio, horas_termino, minutos_termino)
    print(f"""
            Início do jogo - {horas_inicio}:{minutos_inicio}
            Término do jogo - {horas_termino}:{minutos_termino}

            Tempo de jogo - {total_horas}:{total_minutos}
""")

main()
