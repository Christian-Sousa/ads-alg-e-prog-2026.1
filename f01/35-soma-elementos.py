n = int(input("Digite um numero de 3 dígitos: "))
centena = n // 100
dezena = ((n % 100) // 10)
unidade = ((n % 100) % 10)
soma = centena + dezena + unidade
print(f" > A soma dos elementos do nº {n} é igual a {soma}") 