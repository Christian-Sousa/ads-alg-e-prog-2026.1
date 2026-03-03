def obter_numeros():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    return n1, n2, n3

def verificar_iguais(n1,n2,n3):
    if n1 == n2 == n3:
        escrever("Existem 3 números iguais.")
    elif (n1==n2!=n3) or (n1!=n2==n3) or (n1==n3!=n2):
        escrever("Existem 2 números iguais.")
    else:
        escrever("Todos os números são diferentes.")

def escrever(argumento):
    mensagem = print(argumento)
    return mensagem

def main():
    n1,n2,n3 = obter_numeros()
    verificar_iguais(n1,n2,n3)
    
main()