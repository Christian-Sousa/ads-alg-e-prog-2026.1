anos = int(input("Há quantos anos você fuma? "))
numero_dia = int(input("Quantos cigarros você fuma por dia? "))
valor_carteira = float(input("Quanto custa uma carteira de cigarros? "))
total_cigarros = (anos*365*numero_dia) / 20
total_gasto = total_cigarros*valor_carteira
print(f" > Você ja fumou {total_cigarros} cigarros e já gastou R${total_gasto:.2f} em cigarros.")