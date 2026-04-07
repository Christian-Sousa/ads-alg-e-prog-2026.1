def obter_numero_inteiro():
    n = int(input("Número inteiro: "))
    return n

def obter_int_positivo():
    n = int(input('Digite um número: '))
    while n<0:
        n=int(input('Insira um número positivo.'))
    return n

def obter_int_min_x():
    x = int(input('Insira o número mínimo: '))
    n = int(input('Insira um número inteiro: '))
    while n<x:
        print(f'> {n} é menor que {x}')
        n = int(input(f'Insira um número inteiro maior que {x}: '))
    return n

def obter_int_max_x():
    x = int(input('Insira o número máximo: '))
    n = int(input('Insira um número inteiro: '))
    while n>x:
        print(f'> {n} é maior que {x}')
        n = int(input(f'Insira um número inteiro menor que {x}: '))
    return n

def obter_min_max():
    x = int(input('Insira o número mínimo: '))
    y = int(input('Insira o número máximo: '))
    n = int(input('Insira um número inteiro: '))
    while n<x or n>y:
        if n<x:
            print(f'> {n} é menor que {x}')
            n = int(input('Insira um número inteiro: '))

        else:
            print(f'> {n} é maior que {y}')
            n = int(input(f'Insira um número entre {x} e {y}: '))
    return n