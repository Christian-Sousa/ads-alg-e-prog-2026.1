def obter_numeros():
    primeiro = int(input("Digite o 1º lado: "))
    segundo = int(input("Digite o 2º lado: "))
    terceiro = int(input("Digite o 3º lado: "))
    return primeiro, segundo, terceiro

def formar_triangulo(l1,l2,l3):
    if l1+l2>l3 and l2+l3>l1 and l3+l1>l2:
        if l1==0 or l2==0 or l3==0:
            print("Não existe lado com tamanho 0 (zero).")
        elif l1==l2==l3:
            print("O triângulo é equilátero.")
        elif l1==l2!=l3 or l1!=l2==l3 or l3==l1!=l2:
            print("O triângulo é isósceles")
        else:
            print("O triângulo é escaleno.")
    else:
        print("Os valores lidos não formam um triângulo.")
def main():
    n1,n2,n3=obter_numeros()
    return formar_triangulo(n1,n2,n3)

main()