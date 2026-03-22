def main():
    list = []
    num = int(input('Número: '))
    for i in range(1,num+1):
        if i*i <= num:
            quadrado = i*i
            list.append(quadrado)
    print(f'> Maior quadrado menor/igual a {num}: {(max(list))})')

main()