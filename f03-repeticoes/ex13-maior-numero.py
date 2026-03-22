def main():
    lista = []
    quantidade_lista = int(input('Quantidade de números: '))
    for i in range(1,quantidade_lista+1):
        lista.append(int(input(f'Escolha o {i}º número da lista: ')))
    print(f'> Maior número: {max(lista)}')

main()