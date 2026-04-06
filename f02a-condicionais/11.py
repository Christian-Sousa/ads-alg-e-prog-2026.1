def main():
    opcao=int(input('Valor de opcao: '))

    while opcao != 1 and opcao != 2 and opcao != 3:
        print('Os único valores aceitáveis são 1,2 e 3.')
        opcao=int(input('Valor de opcao: '))

    num1=int(input('valor de num1: '))
    num2=int(input('valor de num2: '))
    num3=int(input('valor de num3: '))
    if opcao == 1:
        print(f'>> Valor de num1: {num1}')
    elif opcao == 2:
        print(f'>> Valor de num2: {num2}')
    else:
        print(f'>> Valor de num3: {num3}')

main()