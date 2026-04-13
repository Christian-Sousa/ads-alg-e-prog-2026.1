import os

def main():
    os.system('cls')

    entrada = int(input('Número: '))
    while entrada !=0:
        print(f'divisores de {entrada}:')
        for i in range(1,entrada+1):
            if entrada%i==0:
                print(f'{i}', end=' ')
        break
    print('\n> FIM DO PROGRAMA')

main()