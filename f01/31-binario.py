binario = int(input("Digite 4 dígitos em binário: "))
int1 = (binario // 1000)*2**3
int2 = ((binario % 1000) // 100)*2**2 
int3 = ((binario % 100) // 10)*2**1 
int4 = ((binario % 10) // 1)*2**0 
soma = int1 + int2 + int3 + int4
print(f"> O valor de {binario} na base binária é igual a {soma} na base decimal.")