custo_carro = float(input("Digite o custo de fábrica do carro: "))
percentagem_distribuidor = custo_carro*28/100
percentagem_impostos = custo_carro*45/100
soma = custo_carro + percentagem_distribuidor + percentagem_impostos
print(f" > O custo final do carro é de R${soma:.2f}")