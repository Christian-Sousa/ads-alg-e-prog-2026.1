def main():
    numero = int(input('\nNúmero: '))
    acumulativo=0
    for i in range(1,numero+1):
        acumulativo=acumulativo+i

    print(acumulativo)

main()