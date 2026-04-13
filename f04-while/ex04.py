def main():
    numero=int(input('Número: '))
    while numero/2>1:
        numero=numero/2
    numero = numero/2
    print(f'{numero:.2f}')
main()