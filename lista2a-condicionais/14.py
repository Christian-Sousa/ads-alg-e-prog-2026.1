def obter_numero():
    primeiro = int(input("Digite o 1º valor: "))
    segundo = int(input("Digite o 2º valor: "))
    terceiro = int(input("Digite o 3º valor: "))
    quarto = int(input("Digite o 4º valor: "))
    quinto = int(input("Digite o 5º valor: "))
    return primeiro, segundo, terceiro, quarto, quinto

def calcular_media(a, b, c, d, e):
    media = (a+b+c+d+e)/5
    return a, b, c, d, e, media

def maiores_media(a, b, c, d, e, media):
    if media<a:
        print(f"O valor {a} é maior que a média.")
    elif media<b:
        print(f"O valor {b} é maior que a média.")
    elif media<c:
        print(f"O valor {c} é maior que a média.")
    elif media<d:
        print(f"O valor {d} é maior que a média.")
    else:
        print(f"O valor {e} é maior que a média.")
    return print()

def main():
    a,b,c,d,e = obter_numero()
    a1,a2,a3,a4,a5,media = calcular_media(a,b,c,d,e)
    maiores = maiores_media(a1,a2,a3,a4,a5,media)
    return maiores

main()