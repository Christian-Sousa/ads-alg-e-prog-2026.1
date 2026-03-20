def main():
    numero = int(input('Número: '))
    LimiteInferior = int(input('Limite Inferior: '))
    LimiteSuperior = int(input('Limite Superior: '))
    for i in range(LimiteInferior,LimiteSuperior+1):
        if i%numero==0:
            print(i, end="; ")
main()
