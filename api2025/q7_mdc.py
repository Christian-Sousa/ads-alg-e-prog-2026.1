import os

def main():
    os.system('cls')

    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    a=n1
    b=n2
    while b!=0:
        if a<b:
            a,b=b,a
        resto=a%b
        a=b
        b=resto
    print(f'O mdc de {n1} e {n2} = {a}')

main()