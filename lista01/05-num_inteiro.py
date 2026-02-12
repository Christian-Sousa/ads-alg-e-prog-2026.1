num = int(input("Digite um número inteiro de 3 dígitos: "))
centena = num//100
resto = num%100
dezena = resto//10
unidade = resto%10
soma = centena+dezena+unidade
print(f"A soma das centenas ({centena}), dezenas ({dezena}) e unidades ({unidade}) do número {num} é igual a {soma}.")