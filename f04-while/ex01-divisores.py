def main():
    entrada = int(input('Número: '))
    while entrada !=0:
        print(f'divisores de {entrada}')
        for i in range(1,entrada+1):
            if entrada%i==0:
                print(f'{i}', end=';')
        entrada = int(input('\nDigite o próximo número ou 0 para encerrar. '))

    print('> FIM DO PROGRAMA')

main()