def main():
    Valor_inicial = int(input("Valor inicial: "))
    Limite = int(input("Limite: "))
    Razao = int(input("Razão: "))

    for i in range(Valor_inicial, Limite, Razao):
        print(i, end=" ")

main()