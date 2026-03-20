def main():
    LimiteInferior = int(input('Limite Inferior: '))
    LimiteSuperior = int(input('Limite Superior: '))
    for i in range(LimiteInferior,LimiteSuperior+1):
        if i%i == 0 and i%2!=0 and i%3!=0 and i%4!=0 and i%5!=0:
            print(i, end="; ")
main()
