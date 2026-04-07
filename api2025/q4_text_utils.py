def obter_texto():
    text = input()
    return text

def obter_texto_tamanho_min():
    tamanho = int(input('Tamanho mínimo do texto: '))
    text = input('Texto: ')
    while len(text) < tamanho:
        text = input('Texto menor que o valor mínimo. Insira novamente: ')
    return text

def obter_texto_tamanho_max():
    tamanho = int(input('Tamanho máximo do texto: '))
    text = input('Texto: ')
    while len(text) > tamanho:
        text = input('Texto maior que o valor máximo. Insira novamente: ')
    return text

def obter_texto_min_max():
    minimo = int(input('Tamanho mínimo do texto: '))
    maximo = int(input('Tamanho máximo do texto: '))
    text = input('Texto: ')
    while len(text)<minimo or len(text) > maximo:
        if len(text)<minimo:
            text = input('Texto menor que o valor mínimo. Insira novamente: ')
        else:
            text = input('Texto maior que o valor máximo. Insira novamente: ')
    return text