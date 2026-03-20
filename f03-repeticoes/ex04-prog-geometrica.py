def main():
    Valor_inicial = int(input("Valor inicial: "))
    Limite = int(input("Limite: "))
    Razao = int(input("Razão: "))
    Termo_atual=Valor_inicial
    while Termo_atual<Limite:
        print(Termo_atual)
        Termo_atual=Termo_atual*Razao

main()