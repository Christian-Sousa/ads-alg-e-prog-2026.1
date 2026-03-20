num = int(input("Digite um número: "))
centena=num//100
resto=num%100
dezena=resto//10 * 10
unidade=resto%10 * 100
soma=unidade+dezena+centena
print(f"O número {num} ao contrário é {soma}")