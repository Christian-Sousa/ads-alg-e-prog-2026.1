def main():
    LimiteInferior = int(input('Limite Inferior: '))
    LimiteSuperior = int(input('Limite Superior: '))
    for i in range(LimiteInferior,LimiteSuperior+1):
        if i%2==0:
            print(i, end="; ")
main()
