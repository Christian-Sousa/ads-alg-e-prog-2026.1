total_dias = int(input("Digite quantos dias de vida você tem: "))
anos = total_dias // 365
meses = (total_dias % 365) // 30
dias = (total_dias % 365) % 30
print(f" > {total_dias} dias é igual a {anos} anos, {meses} meses e {dias} dias. ")