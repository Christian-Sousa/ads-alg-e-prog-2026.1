def main():
    n1 = int(input('Primeiro numero: '))
    n2 = int(input('Segundo numero: '))
    
    if n1 > n2:
        mmc = n1
    else:
        mmc = n2

    while True:
        if mmc % n1 == 0 and mmc % n2 == 0:
            break
        mmc += 1
    print(f"O MMC entre {n1} e {n2} é: {mmc}")
    
main()