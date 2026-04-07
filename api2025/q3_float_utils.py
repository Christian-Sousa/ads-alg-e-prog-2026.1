def obter_numero_float():
    n = float(input("Número decimal: "))
    return n

def obter_float_positivo():
    n = float(input('Digite um número:'))
    while n<0:
        n=float(input('Insira um número decimal positivo.'))
    return n

def obter_float_min_x():
    x = float(input('Insira o número mínimo: '))
    n = float(input('Insira um número decimal: '))
    while n<x:
        print(f'> {n} é menor que {x}')
        n = float(input(f'Insira um número decimal maior que {x}: '))
    return n

def obter_float_max_x():
    x = float(input('Insira o número máximo: '))
    n = float(input('Insira um número decimal: '))
    while n>x:
        print(f'> {n} é maior que {x}')
        n = float(input(f'Insira um número decimal menor que {x}: '))
    return n

def obter_min_max():
    x = float(input('Insira o número mínimo: '))
    y = float(input('Insira o número máximo: '))
    n = float(input('Insira um número decimal: '))
    while n<x or n>y:
        if n<x:
            print(f'> {n} é menor que {x}')
            n = float(input('Insira um número decimal: '))

        else:
            print(f'> {n} é maior que {y}')
            n = float(input(f'Insira um número entre {x} e {y}: '))
    return n