def obter_numero_inteiro(entrada):
    return int(input(entrada))

def obter_inteiro_positivo(entrada):
    entrada = int(input(entrada))
    if entrada<0:
        int(input('Digite um número positivo: '))
    return int(input(entrada))

n1 = obter_inteiro_positivo('N1: ')