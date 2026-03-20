def obter_numeros():
    primeiro = int(input("Digite o 1º número: "))
    segundo = int(input("Digite o 2º número: "))
    terceiro = int(input("Digite o 3º número: "))
    return primeiro, segundo, terceiro

def verificar_maior(a,b,c):
    if a > b > c:
        maior = print(f"Maior nº: {a}")
    elif b > a > c:
        maior = print(f"Maior nº: {b}")
    else:
        maior = print(f"Maior nº: {c}")
    return maior

def main():
    n1,n2,n3=obter_numeros()
    return verificar_maior(n1,n2,n3)

main()