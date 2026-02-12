n = int(input("Digite um numero de 3 dígitos: "))
centena = n // 100
dezena = ((n % 100) // 10)*10
unidade = ((n % 100) % 10)*100
soma_n = unidade+dezena+centena
soma = n + soma_n
print(f"> {n} + {soma_n} = {soma}")