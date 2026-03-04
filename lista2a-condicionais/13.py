def obter_numeros():
    primeiro = int(input("Digite o 1º valor: "))
    segundo = int(input("Digite o 2º valor: "))
    terceiro = int(input("Digite o 3º valor: "))
    quarto = int(input("Digite o 4º valor: "))
    quinto = int(input("Digite o 5º valor: "))
    return primeiro, segundo, terceiro, quarto, quinto

def verificar_maior(a, b, c, d, e):
    if a > b and a > c and a > d and a > e:
        maior = a
    elif b > a and b > c and b > d and b > e:
        maior = b
    elif c > a and c > b and c > d and c > e:
        maior = c
    elif d > a and d > b and d > c and d > e:
        maior = d
    else:
        maior = e

    if a < b and a < c and a < d and a < e:
        menor = a
    elif b < a and b < c and b <d and b < e:
        menor = b
    elif c < a and c < b and c < d and c < e:
        menor = c
    elif d < a and d < b and d < c and d < e:
        menor = d
    else:
        menor = e

    return maior, menor

def main():
    n1, n2, n3, n4, n5=obter_numeros()
    maior, menor =  verificar_maior(n1, n2, n3, n4, n5)
    print(f"> O menor valor é {menor} e o maior valor é {maior}.")

main()
