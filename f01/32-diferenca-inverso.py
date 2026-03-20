n = int(input("Digite um numero de 3 dígitos: "))
centena = n // 100
dezena = ((n % 100) // 10)*10
unidade = ((n % 100) % 10)*100
soma = unidade+dezena+centena
diferenca = n - soma
print(f"> {n} - {soma} = {diferenca}")