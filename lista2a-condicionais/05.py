def obter_numeros():
    primeiro = int(input("Digite o 1º número: "))
    segundo = int(input("Digite o 2º número: "))
    terceiro = int(input("Digite o 3º número: "))
    return primeiro, segundo, terceiro

def ordem_crecente(a,b,c):
    if a < b < c:
        ordem = print(f"Ordem crescente: {a},{b},{c}")
    elif a < c < b:
        ordem = print(f"Ordem crescente: {a},{c},{b}")
    elif b < a < c:
        ordem = print(f"Ordem crescente: {b},{a},{c}")
    elif b < c < a:
        ordem = print(f"Ordem crescente: {b},{c},{a}")
    elif c < b < a:
        ordem = print(f"Ordem crescente: {c},{b},{a}")
    else:
        ordem = print(f"Ordem crescente: {c},{a},{b}")
    return ordem

def main():
    n1,n2,n3=obter_numeros()
    return ordem_crecente(n1,n2,n3)

main()