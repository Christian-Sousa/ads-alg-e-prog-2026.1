def obter_numeros():
    primeiro = int(input("Digite o 1º ângulo: "))
    segundo = int(input("Digite o 2º ângulo: "))
    terceiro = int(input("Digite o 3º ângulo: "))
    return primeiro, segundo, terceiro

def formar_triangulo(a1,a2,a3):
    if a1 + a2 + a3 == 180:
        if a1<90 and a2<90 and a3<90:
            print("O triângulo é acutângulo.")
        elif a1==90 or a2==90 or a3==90:
            print("O triângulo é retângulo.")
        elif a1>90 or a2>90 or a3>90:
            print("O triângulo é obtusângulo.")
    else: 
        print("Os ângulos não formam um triângulo.")
    return print()

def main():
    n1,n2,n3=obter_numeros()
    return formar_triangulo(n1,n2,n3)

main()