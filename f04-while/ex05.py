def main():
    x=int(input('Valor de X: '))
    n=int(input('Valor de N: '))
    while n!=2:
        divisao=x/n
        print(f'{divisao:.5f}')
        x=divisao
        n-=1
main()