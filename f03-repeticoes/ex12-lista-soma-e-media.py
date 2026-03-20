def main():
    lista = int(input('Quantidade de números na lista: '))
    acumulativo_soma = 0

    for i in range(1,lista+1):
        num_lista = int(input(f'Escolha o {i}º número da lista: '))
        acumulativo_soma = acumulativo_soma+num_lista

    print(f'> A soma dos números listados é {acumulativo_soma}')
    media = acumulativo_soma/lista
    print(f'> A média dos números listados é {media:.1f}')
main()